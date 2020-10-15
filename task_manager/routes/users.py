from flask import Blueprint
from flask import current_app as app
from flask_restx import Api, Resource

user_bp = Blueprint('user_bp', __name__, url_prefix='/user')
api = Api(user_bp)


@api.route('/create', methods=['GET', 'POST'])
class CreateUser(Resource):
	def get(self):
		return {'Show' :'Form'}

	def post(self):
		return {'create' :'user'}


@api.route('/')
@api.route('/<int:user_id>')
class FetchUser(Resource):
	def get(self, user_id = -1):
		return {'User': user_id}


@api.route('/edit/<int:user_id>', methods=['GET', 'POST'])
class UpdateUser(Resource):
	def get(self):
		return {'Show' :'Form'}

	def post(self):
		return {'update' :'user'}


@api.route('/delete/<int:user_id>', methods=['PUT', 'DELETE'])
class DeleteUser(Resource):
	def delete(self ,user_id):
		return 'User %d' % user_id