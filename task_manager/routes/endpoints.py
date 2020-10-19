from flask_restx import Resource, Namespace

#from task_manager.routes.users import get_user

user_api = Namespace('user', description='User API endpoints')
task_api = Namespace('task', description='Task API endpoints')


@user_api.route('/')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

@user_api.route('/create', methods=['POST'])
class CreateUser(Resource):
    def post(self):
        """ register a new user account """
        return {'create': 'user'}


@user_api.route('/<int:user_id>')
class GetUser(Resource):
    def get(self, user_id = -1):
        return {'User: ': user_id}


@user_api.route('/edit/<int:user_id>', methods=['GET', 'POST'])
class UpdateUser(Resource):
    def get(self):
        return {'Show': 'Form'}

    def post(self):
        return {'update': 'user'}


@user_api.route('/delete/<int:user_id>', methods=['PUT', 'DELETE'])
class DeleteUser(Resource):
    def delete(self, user_id = -1):
        return 'User %d' % user_id


@task_api.route('/create', methods=['GET', 'POST'])
class CreateTask(Resource):
    def get(self):
        return {'Show': 'Form'}

    def post(self):
        return {'Create': 'Task'}


@task_api.route('/<int:task_id>')
class FetchTask(Resource):
    def get(self, task_id=-1):
        return 'Task %d' % task_id


@task_api.route('/edit/<int:task_id>', methods=['GET', 'POST'])
class UpdateTask(Resource):
    ''' UPDATE TASK '''

    def get(self, task_id):
        return {'Show': 'Form'}

    def post(self, task_id):
        return {'Update': 'Task'}


@task_api.route('/delete/<int:task_id>', methods=['PUT', 'DELETE'])
class DeleteTask(Resource):
    ''' DELETE TASK '''

    def delete(self, task_id):
        return 'Task %d' % task_id
