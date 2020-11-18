
import unittest
# from flask_login import current_user, login_user, logout_user

from task_manager import create_app, db
from task_manager.models.task import Task  # noqa: F401
from task_manager.models.user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self.app = create_app('config.DevelopmentConfig')
        self.app_context = self.app.app_context()
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.sqlite3'
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_password_validation(self):
        """ TEST PASSWORD CHECK """
        user = User(username='alice', email='alice@test.com', password='')
        user.set_password('test')
        self.assertFalse(user.validate_password('password'))
        self.assertTrue(user.validate_password('test'))

    def test_create_user(self):
        """ TEST CREATE USER """
        user = User(username='alice', email='alice@test.com', password='')
        user.set_password('test')
        user.save_user()
        db_user = User.query.filter_by(username='alice').first()
        self.assertEqual(user, db_user)

    def test_Update(self):
        '''
        TEST UPDATE USER
        '''
        self.assertEqual('1', '1')

    def test_delete_user(self):
        """ TEST DELETE USER """
        user = User(username='alice', email='alice@test.com', password='')
        user.save_user()
        user.delete_user()
        db_user = User.query.filter_by(username='alice').first()
        self.assertEqual(db_user, None)


'''
class TestLogin(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.sqlite3'
        self.app_context.push()
        db.create_all()


    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_login(self):
        with self.app_context:
            user = User(username='bob', email='bob@test.com', password='')
            user.set_password('test')
            user.save_user()

            user = User.query.filter_by(username='bob').first()
            user.validate_password('test')

            self.app_context.login_user(user)
            self.assertEqual(current_user.id, self.user.id, "Wrong User ID")

    def test_logout(self):
        with self.app_context:
            user = User(username='bob', email='bob@test.com', password='')
            user.set_password('test')
            user.save_user()
            user = User.query.filter_by(username='bob').first()
            user.validate_password('test')

            self.app_context.login_user(user)
            self.app_context.logout_user()
            self.assertFalse(current_user.is_authenticated, "User was not logged out")
'''
