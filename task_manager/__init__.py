from flask import Flask
# from flask import request
# from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)                  # Create a Flask WSGI application
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
# api = Api(app)


def create_app():
    return app
