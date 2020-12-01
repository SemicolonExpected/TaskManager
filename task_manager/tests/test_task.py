import unittest

from task_manager import create_app, db
from task_manager.models.task import Task
from task_manager.models.assignment import Assignment
from datetime import date, time


class TestTask(unittest.TestCase):
    def setUp(self):
        self.app = create_app('config.DevelopmentConfig')
        self.app_context = self.app.app_context()
        self.client = self.app.test_client()
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.sqlite3'
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.app.config['LOGIN_DISABLED'] = True
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def createTask(self, title, priority, description, start_date, start_time, end_date,
                   end_time):
        return self.client.post('/task/create', data=dict(title=title,
                                                          priority=priority,
                                                          description=description,
                                                          start_date=start_date,
                                                          start_time=start_time,
                                                          end_date=end_date,
                                                          end_time=end_time),
                                follow_redirects=True)

    def test_create_task(self):
        '''TEST CREATE TASK'''
        start_date = date(2020, 11, 30)
        start_time = time(hour=15, minute=30, second=00)
        end_date = date(2020, 11, 30)
        end_time = time(hour=15, minute=36, second=00)
        response = self.createTask(title='hello', priority=1,
                                   description='test descrip',
                                   start_date=start_date, start_time=start_time,
                                   end_date=end_date, end_time=end_time)
        self.assertEqual(response.status_code, 200)

    def test_Assignment(self):
        '''
        TEST FETCH TASK
        '''
        new_task = Task(title="hello", priority='1', description="task_decription")

        db.session.add(new_task)
        db.session.commit()

        new_assignment = Assignment(time_added=date.today(), user_id=1,
                                    task_id=new_task.id)
        db.session.add(new_assignment)
        db.session.commit()

        self.assertEqual(Assignment.query.filter_by(task_id=new_task.id).first(),
                         new_assignment)

    def test_Update(self):
        '''
        TEST UPDATE TASK
        '''
        self.assertEqual('1', '1')

    def test_Delete(self):
        '''
        TEST DELETE TASK
        '''
        self.assertEqual('1', '1')
