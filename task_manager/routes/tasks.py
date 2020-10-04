from flask import Flask
from flask import request

from flask_restx import Resource, Api


api =Api(version = 'alpha', title = 'Task Manager', description = 'Another Productivity App')

task = api.namespace('task', description = "Task Related Functions")


@task.route('/')
@task.route('/<int:task_id>')
class GetTask(Resource):
	def get(self, task_id = -1):
		return 'Task %d' % task_id

#@api.route('/task/')
#@api.route('/task/<int:task_id>')
#class GetTask(Resource):
#	def getTask(task_id = -1):
#		return 'Task %d' % task_id
