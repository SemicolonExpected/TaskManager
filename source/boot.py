'''
Bootstrap program
'''

from flask import Flask
from flask import request

from flask_restplus import Resource, Api

app = Flask(__name__)                  # Create a Flask WSGI application
api = Api(app)                         # Create a Flask-RESTPlus API


@api.route('/hello')                   # Create a URL route to this resource
class HelloWorld(Resource):            # Create a RESTful resource
	def get(self):                     # Create GET endpoint
		return {'hello':'world'}


@api.route('/task/create', methods=['GET', 'POST'])
def createTask():  # i honestly dont know what to do here yet
	if request.method == 'POST':
		return {'create': 'task'}
	else:
		return {'Show':'Form'}


@api.route('/task/')
@api.route('/task/<int:task_id>')
def getTask(task_id = -1):
	return 'Task %d' % task_id


@api.route('/task/edit/<int:task_id>', methods=['GET', 'POST'])
def updateTask(task_id):  # i honestly dont know what to do here yet
	if request.method == 'POST':
		return {'update':'task'}
	else:
		return {'Show': 'Form'}


@api.route('/task/delete/<int:task_id>', methods=['PUT', 'DELETE'])
def deleteTask(task_id):
	return 'Task %d' % task_id


@api.route('/CreateUser', methods=['GET', 'POST'])
def createUser():  # i honestly dont know what to do here yet
	if request.method == 'POST':
		return {'create':'user'}
	else:
		return {'Show':'Form'}


@api.route('/user/')
@api.route('/user/<int:user_id>')
def getUser(user_id = -1):
	return 'User %d' % user_id


@api.route('/user/edit/<int:user_id>', methods=['GET', 'POST'])
def updateUser(user_id):  # i honestly dont know what to do here yet
	if request.method == 'POST':
		return {'update':'user'}
	else:
		return {'Show':'Form'}


@api.route('/user/delete/<int:user_id>', methods=['PUT', 'DELETE'])
# I dont know if I want to do DELETE or PUT
def deleteUser(user_id):
	return 'User %d' % user_id

#def initialize_app(flask_app):

	#api.add_namespace()
	#api.add_namespace()

#def main():
#    initialize_app(app)
#    app.run(debug=True) # Start a development server


if __name__ == '__main__':
	app.run(debug=True)	 # Start a development server
	#main()
