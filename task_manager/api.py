from flask import current_app as app, render_template, make_response
from flask_restx import Resource, Namespace, Api
from flask_login import login_required

import task_manager.routes.tasks as tasks
import task_manager.routes.users as users
import task_manager.routes.auth as auth

api = Api(app, title="Task Manager App",
          description="A productivity tool")

user_ns = Namespace('user', description='User API endpoints')
task_ns = Namespace('task', description='Task API endpoints')


@api.route('/index')
class Index(Resource):
    @login_required
    def get(self):
        return make_response(render_template("index2.html", title='Home Page'))


@api.route('/register')
class Register(Resource):
    def get(self):
        return auth.register()

    def post(self):
        return auth.register()


@api.route('/login')
class Login(Resource):
    def get(self):
        return auth.login()

    def post(self):
        return auth.login()


@api.route('/logout')
class Logout(Resource):
    @login_required
    def get(self):
        return auth.logout()


@task_ns.route('/create', methods=['GET', 'POST'])
class CreateTask(Resource):
    ''' CREATE NEW TASK '''

    def get(self):
        return tasks.model_get_create_task()

    def post(self):
        return tasks.model_post_create_task()


@task_ns.route('/')
@task_ns.route('/<int:task_id>')
class FetchTask(Resource):
    ''' FETCH TASK '''

    def get(self, task_id=-1):
        return tasks.model_fetch_task(task_id)


@task_ns.route('/edit/<int:task_id>', methods=['GET', 'POST'])
class UpdateTask(Resource):
    ''' UPDATE TASK '''

    def get(self, task_id):
        return tasks.model_get_update_task(task_id)

    def post(self, task_id):
        return tasks.model_post_update_task(task_id)


@task_ns.route('/delete/<int:task_id>', methods=['GET', 'POST'])
class DeleteTask(Resource):
    def get(self, task_id):
        return tasks.model_delete_task(task_id)


@task_ns.route('/create', methods=['GET', 'POST'])
class CreateUser(Resource):
    def get(self):
        return users.model_get_create_user()

    def post(self):
        return users.model_post_create_user()

@user_ns.route('/')
@user_ns.route('/<int:user_id>')
class GetUser(Resource):
    def get(self, user_id):
        return users.model_get_user(user_id)


@user_ns.route('/edit/<int:user_id>', methods=['GET', 'POST'])
class UpdateUser(Resource):
    def get(self, user_id):
        return users.model_get_update_user(user_id)

    def post(self, user_id):
        return users.model_post_update_user(user_id)


@user_ns.route('/delete/<int:user_id>', methods=['PUT', 'DELETE'])
class DeleteUser(Resource):
    def delete(self, user_id):
        return users.model_delete_user(user_id)
