import unittest
from task_manager import db
from task_manager.models.user import User
from flask import current_app as app


class TestUserModel(unittest.TestCase):
	def setUp(self):
		app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://test.sqlite3'
		db.create_all()

	def tearDown(self):
		db.session.remove()
		db.drop_all()

	def test_password_validation(self):
		user = User(username='alice', email='alice@test.com', password='')
		user.set_password('test')
		self.assertFalse(user.validate_password('password'))
		self.assertTrue(user.validate_password('test'))

	def test_create(self):
		user = User(username='alice', email='alice@test.com', password='')
		user.set_password('test')
		user.save_user()
		db_user = User.query.filter_by(username='alice').first()
		self.assertEqual(user, db_user)

	def test_Get(self):
		'''
		TEST FETCH USER
		'''
		self.assertEqual('1', '1')

	def test_Update(self):
		'''
		TEST UPDATE USER
		'''
		self.assertEqual('1', '1')

	def test_Delete(self):
		'''
		TEST DELETE USER
		'''
		self.assertEqual('1', '1')
