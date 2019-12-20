# /run.py
import os

from blog_api.src.app import create_app


def set_environment_variable():
    os.environ["FLASK_ENV"] = "development"
    os.environ["DATABASE_URL"] = 'postgres://name:password@houst:port/blog_api_db'
    os.environ["JWT_SECRET_KEY"] = 'hhgaghhgsdhdhdd'


if __name__ == '__main__':
    set_environment_variable()
    env_name = os.getenv('FLASK_ENV')
    app = create_app(env_name)
# run app
    app.run()