import unittest

from task_manager import create_app, db
from task_manager.models.task import Task  # noqa: F401
from task_manager.models.user import User


class TestAuth(unittest.TestCase):
    def setUp(self):
        self.app = create_app('config.DevelopmentConfig')
        self.app_context = self.app.app_context()
        self.client = self.app.test_client()
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.sqlite3'
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def login(self, username, password):
        return self.client.post('/login', data=dict(username=username,
                                                    password=password),
                                follow_redirects=True)

    def register(self, username, email, password, password2):
        return self.client.post('/register', data=dict(username=username,
                                                       email=email,
                                                       password=password,
                                                       password2=password2),
                                follow_redirects=True)

    def test_register(self):
        '''TEST REGISTER'''
        response = self.register(username='testregister',
                                 email='testregister@test.com',
                                 password='pass123',
                                 password2='pass123')
        self.assertEqual(response.status_code, 200)

    def test_login_logout(self):
        '''TEST LOGIN-LOGOUT'''
        user = User(username='testlogin', email='testlogin@test.com',
                    password='pass123')
        user.set_password('pass123')
        user.save_user()
        response = self.login('testlogin', 'pass123')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/logout')
        self.assertEqual(response.status_code, 302)

    def test_invalid_login(self):
        '''TEST INVALID LOGIN'''
        user = User(username='testlogin', email='testlogin@test.com',
                    password='pass')
        user.set_password('pass123')
        user.save_user()
        response = self.login('testlogin', 'pass')
        self.assertEqual(response.status_code, 200)
