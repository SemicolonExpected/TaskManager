import unittest


from task_manager import create_app, db
from task_manager.models.task import Task  # noqa: F401
from task_manager.models.user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self.app = create_app('config.DevelopmentConfig')
        self.app_context = self.app.app_context()
        self.client = self.app.test_client()
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

    def test_update(self):
        '''
        TEST UPDATE USER
        '''
        user = User(username='carol', email='carol@test.com', password='')
        user.save_user()
        update_user = User.query.filter_by(username='carol').first()
        update_user.username = 'bob'
        update_user.save_user()
        self.assertEqual(update_user.username, 'bob')

    def test_delete_user(self):
        """ TEST DELETE USER """
        user = User(username='bob', email='bob@test.com', password='')
        user.save_user()
        user.delete_user()
        db_user = User.query.filter_by(username='bob').first()
        self.assertEqual(db_user, None)

    def test_get_user(self):
        '''TEST GET USER '''
        user = User(username='getUser', email='getUser@test.com', password='')
        user.save_user()
        test_id = user.id
        url = '/user/{}'.format(test_id)
        response = self.client.get(url)
        self.assertEqual(response.data,
                         b'{"user":{"id":1,"username":"getUser"}}\n')
