from flask import Flask
from flask import request

from flask_restx import Resource, Api


# api =Api(version = 'alpha', title = 'Task Manager', description = 'Another Productivity App')

# task = api.namespace('task', description = "Task Related Functions")


def model_get_create_task():
    return {'Show': 'Form'}


def model_post_create_task():
    return {'Create': 'Task'}


def model_fetch_task(task_id):
    return 'Task %d' % task_id


def model_get_update_task(task_id):
    return {'Show': 'Form'}


def model_post_update_task(task_id):
    return {'Update': 'Task'}


def model_delete_task(task_id):
    return 'Task %d' % task_id
