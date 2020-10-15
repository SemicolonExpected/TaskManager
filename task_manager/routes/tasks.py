from flask import Blueprint
from flask import current_app as app
from flask_restx import Api, Resource

task_bp = Blueprint('task_bp', __name__, url_prefix='/task')
api = Api(task_bp)


@api.route('/create', methods=['GET', 'POST'])
class CreateTask(Resource):
    def get(self):
        # return {'Show': 'Form'}
        return model_get_create_task()

    def post(self):
        # return {'Create':'Task'}
        return model_post_create_task()


@api.route('/')
@api.route('/<int:task_id>')
class FetchTask(Resource):
    def get(self, task_id=-1):
        # return 'Task %d' % task_id
        return model_fetch_task(task_id)


@api.route('/edit/<int:task_id>', methods=['GET', 'POST'])
class UpdateTask(Resource):
    ''' UPDATE TASK '''

    def get(self, task_id):
        # return {'Show': 'Form'}
        return model_get_update_task(task_id)

    def post(self, task_id):
        # return {'Update':'Task'}
        return model_post_update_task(task_id)


@api.route('/delete/<int:task_id>', methods=['PUT', 'DELETE'])
class DeleteTask(Resource):
    ''' DELETE TASK '''

    def delete(self, task_id):
        # return 'Task %d' % task_id
        return model_delete_task(task_id)


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
