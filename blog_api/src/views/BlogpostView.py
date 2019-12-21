# /src/views/BlogpostView.py
from flask import request, g, Blueprint, json, Response
from ..shared.Authentication import Auth
from blog_api.src.models.BlogpostModel import BlogPostModel, BlogPostSchema

blogPost_api = Blueprint('blogPost_api', __name__)
blogPost_schema = BlogPostSchema()


@blogPost_api.route('/', methods=['POST'])
@Auth.auth_required
def create():
    """
    Create Blogpost Function
    """
    req_data = request.get_json()
    req_data['owner_id'] = g.user.get('id')
    data, error = blogPost_schema.load(req_data)
    if error:
        return custom_response(error, 400)
    post = BlogPostModel(data)
    post.save()
    data = blogPost_schema.dump(post).data
    return custom_response(data, 201)


@blogPost_api.route('/', methods=['GET'])
def get_all():
    """
    Get All Blogposts
    """
    posts = BlogPostModel.get_all_blogposts()
    data = blogPost_schema.dump(posts, many=True).data
    return custom_response(data, 200)


@blogPost_api.route('/<int:blogPost_id>', methods=['GET'])
def get_one(blogPost_id):
    """
    Get A BlogPost
    """
    post = BlogPostModel.get_one_blogpost(blogPost_id)
    if not post:
        return custom_response({'error': 'post not found'}, 404)
    data = blogPost_schema.dump(post).data
    return custom_response(data, 200)


@blogPost_api.route('/<int:blogPost_id>', methods=['PUT'])
@Auth.auth_required
def update(blogPost_id):
    """
    Update A Blogpost
    """
    req_data = request.get_json()
    post = BlogPostModel.get_one_blogPost(blogPost_id)
    if not post:
        return custom_response({'error': 'post not found'}, 404)
    data = blogPost_schema.dump(post).data
    if data.get('owner_id') != g.user.get('id'):
        return custom_response({'error': 'permission denied'}, 400)

    data, error = blogPost_schema.load(req_data, partial=True)
    if error:
        return custom_response(error, 400)
    post.update(data)

    data = blogPost_schema.dump(post).data
    return custom_response(data, 200)


@blogPost_api.route('/<int:blogPost_id>', methods=['DELETE'])
@Auth.auth_required
def delete(blogPost_id):
    """
    Delete A BlogPost
    """
    post = BlogPostModel.get_one_blogpost(blogPost_id)
    if not post:
        return custom_response({'error': 'post not found'}, 404)
    data = blogPost_schema.dump(post).data
    if data.get('owner_id') != g.user.get('id'):
        return custom_response({'error': 'permission denied'}, 400)

    post.delete()
    return custom_response({'message': 'deleted'}, 204)


def custom_response(res, status_code):
    """
    Custom Response Function
    """
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )