'''
Bootstrap program
'''

# import os
from flask import Flask, Blueprint,render_template, make_response,request,redirect
# from flask import request

from flask_restx import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# from task_manager.routes.tasks import task as task_namespace
# from task_manager.routes.users import user as user_namespace

from routes.tasks import model_get_create_task, model_post_create_task, model_fetch_task, model_get_update_task, model_post_update_task, model_delete_task
from routes.users import *

app = Flask(__name__)                  # Create a Flask WSGI application
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
api = Api(app)                          # Create a Flask-RESTPlus API


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id


''' HELLO '''


@api.route('/hello')                   # Create a URL route to this resource
class HelloWorld(Resource):            # Create a RESTful resource
	def get(self):                     # Create GET endpoint
		return {'hello':'world'}


'''
CREATE NEW TASK
'''


@api.route('/task/create', methods=['GET', 'POST'])
class CreateTask(Resource):
	def get(self):
		# return {'Show': 'Form'}
		return model_get_create_task()

	def post(self):
		# return {'Create':'Task'}
		return model_post_create_task()


@api.route('/task/')
@api.route('/task/<int:task_id>')
class FetchTask(Resource):
	def get(self, task_id = -1):
		# return 'Task %d' % task_id
		task= Task.query.all()
		headers = {'Content-Type': 'text/html'}
		# return render_template('index.html', tasks=task)
		return make_response(render_template('index.html', tasks=task),200,headers)


@api.route('/task/edit/<int:task_id>', methods=['GET', 'POST'])
class UpdateTask(Resource):
	def get(self, task_id):
		# return {'Show': 'Form'}
		return model_get_update_task(task_id)

	def post(self, task_id):
		# return {'Update':'Task'}
		return model_post_update_task(task_id)


@api.route('/task/delete/<int:task_id>', methods=['PUT', 'DELETE'])
class DeleteTask(Resource):
	def delete(self, task_id):
		# return 'Task %d' % task_id
		return model_delete_task(task_id)


@api.route('/user/create', methods=['GET', 'POST'])
class CreateUser(Resource):
	def get(self):
		# return {'Show':'Form'}
		return model_get_create_user()

	def post(self):
		# return {'create':'user'}
		return model_post_create_user()


@api.route('/user/')
@api.route('/user/<int:user_id>')
class FetchUser(Resource):
	def get(self, user_id = -1):
		# return {'User': user_id}
		return model_fetch_user(user_id)


@api.route('/user/edit/<int:user_id>', methods=['GET', 'POST'])
class UpdateUser(Resource):
	def get(self):
		# return {'Show':'Form'}
		return model_get_update_user(user_id)

	def post(self):
		# return {'update':'user'}
		return model_post_update_user(user_id)


@api.route('/user/delete/<int:user_id>', methods=['PUT', 'DELETE'])
# I dont know if I want to do DELETE or PUT
class DeleteUser(Resource):
	def delete(self,user_id):
		# return 'User %d' % user_id
		return model_delete_user(user_id)


# def initialize_app(flask_app):
# 	blueprint = Blueprint('api', __name__, url_prefix = '/routes')
# 	api.init_app(blueprint)
# #	api.add_namespace(task_namespace)
# #	api.add_namespace(user_namespace)
# 	flask_app.register_blueprint(blueprint)


# def main():
# 	initialize_app(app)
# 	app.run(debug=True)  # Start a development server


if __name__ == '__main__':
	#app.run(debug=True)	 # Start a development server
	db.create_all()
	app.run(debug=True)
