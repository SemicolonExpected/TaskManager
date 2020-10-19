'''
Bootstrap program
'''

# import os
from flask_restx import Resource, Api
# from Models.task import Task
from .__init__ import db
from .__init__ import create_app
from .routes.tasks import model_get_create_task, model_post_create_task
from .routes.tasks import model_fetch_task, model_get_update_task
from .routes.tasks import model_post_update_task, model_delete_task
from .routes.users import model_get_create_user, model_post_create_user
from .routes.users import model_fetch_user, model_get_update_user
from .routes.users import model_post_update_user, model_delete_user


app = create_app()
api = Api(app)                          # Create a Flask-RESTPlus API

@api.route('/')
@api.route('/hello')                   # Create a URL route to this resource
class HelloWorld(Resource):            # Create a RESTful resource
	''' HOME PAGE '''
	def get(self):                     # Create GET endpoint
		return {'hello': 'world'}


@api.route('/task/create', methods=['GET', 'POST'])
class CreateTask(Resource):
	''' CREATE NEW TASK '''
	def get(self):
		# return {'Show': 'Form'}
		return model_get_create_task()

	def post(self):
		# return {'Create':'Task'}
		return model_post_create_task()


@api.route('/task/')
@api.route('/task/<int:task_id>')
class FetchTask(Resource):
	''' FETCH TASK '''
	def get(self, task_id = -1):
		return model_fetch_task(task_id)


@api.route('/task/edit/<int:task_id>', methods=['GET', 'POST'])
class UpdateTask(Resource):
	''' UPDATE TASK '''
	def get(self, task_id):
		# return {'Show': 'Form'}
		return model_get_update_task(task_id)

	def post(self, task_id):
		# return {'Update':'Task'}
		return model_post_update_task(task_id)


@api.route('/task/delete/<int:task_id>', methods=['GET', 'POST'])
class DeleteTask(Resource):
	def get(self, task_id):
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
	def get(self, user_id):
		# return {'Show':'Form'}
		return model_get_update_user(user_id)

	def post(self, user_id):
		# return {'update':'user'}
		return model_post_update_user(user_id)


@api.route('/user/delete/<int:user_id>', methods=['PUT', 'DELETE'])
# I dont know if I want to do DELETE or PUT
class DeleteUser(Resource):
	def delete(self,user_id):
		# return 'User %d' % user_id
		return model_delete_user(user_id)


if __name__ == '__main__':
	# db.create_all()
	app.run(debug=True)		# Start a development server
