import unittest


from task_manager import create_app, db
from task_manager.models.task import Task  # noqa: F401
from task_manager.models.user import User


def login(self):
    user = User(username='update_task_user', email='update@test.com',
                password='pass123')
    user.set_password('pass123')
    user.save_user()

    #ret = [user.id]
    response = self.client.post('/login', data=dict(username='update_task_user',
                                password='pass123'), follow_redirects=True)

    #ret.append(response.status_code)
    return [user.id, response.status_code]


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

    def test_login(self):
        self.assertEqual(login(self)[1], 200)

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

    @unittest.expectedFailure
    def test_update(self):
        '''
        TEST UPDATE USER
        '''
        login_ = login(self)
        path = '/user/edit/{}'.format(login_[0])

        response = self.client.get(path, follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        response = self.client.post(path, data={'username': "test_update",
                                                'email': "test_update@test.com",
                                                'password': "test1"},
                                    follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        update_user = User.query.filter_by(id=login_[0]).first()
        self.assertEqual(update_user.username, "test_update")
        self.assertEqual(update_user.email, "test_update@test.com")
        self.assertTrue(update_user.validate_password('test1'))
        #user = User(username='carol', email='carol@test.com', password='')
        #user.save_user()
        #update_user = User.query.filter_by(username='carol').first()
        #update_user.username = 'bob'
        #update_user.save_user()
        #self.assertEqual(update_user.username, 'bob')
        # ^ btw you just changed the variable should requery to check whether the change persisted in the database

    def test_delete_user(self):
        """ TEST DELETE USER """
        user = User(username='bob', email='bob@test.com', password='')
        user.save_user()
        #user.delete_user()  # removing this so that we can test our function instead
        path = '/user/delete/{}'.format(user.id)
        response = self.client.get(path, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        response = self.client.post(path, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
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
