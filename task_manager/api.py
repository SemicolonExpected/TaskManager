from flask import render_template, make_response
from flask_restx import Resource, Namespace
from flask_login import login_required

from task_manager import apis
import task_manager.routes.tasks as tasks
import task_manager.routes.users as users
import task_manager.routes.auth as auth

user_ns = Namespace('user', description='User API endpoints')
task_ns = Namespace('task', description='Task API endpoints')


#@apis.route('/test', methods=['GET'])
#class Test(Resource):
#    def get(self):
#       return "Hello World"


@apis.route('/')
@apis.route('/dashboard')  # dashboard
class Index(Resource):
    '''If logged in display index, else display homepage'''

    @login_required
    def get(self):
        return make_response(render_template("dashboard.html",
                                             title='Home Page'))


@apis.route('/register')
class Register(Resource):
    '''SIGN UP'''

    def get(self):
        return auth.register()

    def post(self):
        return auth.register()


@apis.route('/login')
class Login(Resource):
    '''LOG USER IN'''

    def get(self):
        return auth.login()

    def post(self):
        return auth.login()


@apis.route('/logout')
class Logout(Resource):
    '''LOG USER OUT'''

    @login_required
    def get(self):
        return auth.logout()


@task_ns.route('/')
@task_ns.route('/<int:task_id>')
class FetchTask(Resource):
    ''' FETCH TASK '''

    def get(self, task_id=-1):
        return tasks.model_fetch_task(task_id)


@task_ns.route('/create', methods=['GET', 'POST'])
class CreateTask(Resource):
    ''' CREATE NEW TASK '''

    def get(self):
        return tasks.model_get_create_task()

    def post(self):
        return tasks.model_post_create_task()


@task_ns.route('/update/<int:task_id>', methods=['GET', 'POST'])
class UpdateTask(Resource):
    ''' UPDATE TASK '''

    def get(self, task_id):
        return tasks.model_get_update_task(task_id)

    def post(self, task_id):
        return tasks.model_post_update_task(task_id)


@task_ns.route('/delete/<task_id>', methods=['GET', 'POST'])
class DeleteTask(Resource):
    def get(self, task_id):
        return tasks.model_delete_task(task_id)


@user_ns.route('/<int:user_id>')
class GetUser(Resource):
    def get(self, user_id):
        return users.get_user(user_id)


#@user_ns.route('/')
#class GetUsers(Resource):
#    def get(self):
#        return users.get_users()


@user_ns.route('/edit/<int:user_id>', methods=['GET', 'POST'])
class UpdateUser(Resource):
    def get(self, user_id):
        return users.form_update_user(user_id)

    def post(self, user_id):
        return users.update_user(user_id)


@user_ns.route('/delete/<int:user_id>')
class DeleteUser(Resource):
    def get(self, user_id):
        return users.delete_user(user_id)

    def post(self, user_id):
        return users.delete_user(user_id)
