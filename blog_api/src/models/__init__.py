# src/models/__init__.py
# from .BlogpostModel import BlogpostModel, BlogpostSchema
# from blog_api.src.models.UserModel import UserModel, UserSchema
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
# initialize our db
db = SQLAlchemy()

#######
# existing code remains #
#######
bcrypt = Bcrypt()