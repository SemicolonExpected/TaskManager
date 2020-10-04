from flask import Flask
from flask import request

from flask_restx import Resource, Api

api = Api(version = 'alpha', title = 'Task Manager', description = 'Another Productivity App')

user = api.namespace('user', description = "User Related Functions")
