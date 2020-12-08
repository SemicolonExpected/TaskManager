import unittest

from task_manager.models.user import User
from task_manager import create_app, db
from task_manager.models.task import Task
from task_manager.models.assignment import Assignment
from datetime import datetime, timedelta

import logging

logger = logging.getLogger(__name__)


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

    def create_task(self, title, priority, description, start_date,
                    end_date):
        return self.client.post('/task/create',
                                data={'title': title,
                                      'priority': priority,
                                      'description': description,
                                      'start_date': start_date,
                                      'end_date': end_date},
                                follow_redirects=True)

    def test_create_task_view(self):
        '''TEST CREATE TASK'''
        user = User(username='create_task_user', email='create@test.com',
                    password='pass123')
        user.set_password('pass123')
        user.save_user()

        self.client.post('/login', data=dict(username='create_task_user',
                                             password='pass123'),
                         follow_redirects=True)

        get_create_task_view_response = self.client.get('/task/create')
        self.assertEqual(get_create_task_view_response.status_code, 200)

        start_date = datetime.now()
        end_date = start_date + timedelta(minutes=10)

        response = self.create_task(title='create task',
                                    priority=1,
                                    description='testing create task',
                                    start_date=start_date.strftime("%Y-%m-%dT%H:%M"),  # noqa: E501
                                    end_date=end_date.strftime("%Y-%m-%dT%H:%M"))  # noqa: E501
        self.assertEqual(response.status_code, 200)

        invalid_form = self.create_task(title=None,
                                        priority=1,
                                        description='testing create task',
                                        start_date=start_date.strftime("%Y-%m-%dT%H:%M"),  # noqa: E501
                                        end_date=end_date.strftime("%Y-%m-%dT%H:%M"))  # noqa: E501

        self.assertEqual(invalid_form.status_code, 200)

    def test_Assignment(self):
        '''
        TEST ASSIGNMENT
        '''
        new_task = Task(title="hello", priority=1,
                        description="task description",
                        start_time=datetime.now(),
                        end_time=datetime.now())

        db.session.add(new_task)
        db.session.commit()

        new_assignment = Assignment(time_added=datetime.today(), user_id=1,
                                    task_id=new_task.id)
        db.session.add(new_assignment)
        db.session.commit()

        self.assertEqual(
            Assignment.query.filter_by(task_id=new_task.id).first(),
            new_assignment)

    def update_task(self, task_id, title, priority, description, start_date,
                    end_date):
        path = '/task/update/{}'.format(task_id)
        return self.client.post(path, data={'title': title,
                                            'priority': priority,
                                            'description': description,
                                            'start_date': start_date,
                                            'end_date': end_date},
                                follow_redirects=True)

    def test_update_task_view(self):
        '''TEST UPDATE TASK'''
        user = User(username='update_task_user', email='update@test.com',
                    password='pass123')
        user.set_password('pass123')
        user.save_user()

        self.client.post('/login', data=dict(username='update_task_user',
                                             password='pass123'),
                         follow_redirects=True)

        task = Task(title="old task", priority=1,
                    description="old task description",
                    start_time=datetime.now(),
                    end_time=datetime.now())

        db.session.add(task)
        db.session.commit()
        path = '/task/update/{}'.format(task.id)

        get_task_view_response = self.client.get(path)
        self.assertEqual(get_task_view_response.status_code, 200)

        start_date = datetime.now()
        end_date = start_date + timedelta(minutes=10)

        response = self.update_task(task_id=task.id,
                                    title='new task',
                                    priority=5,
                                    description='new task description',
                                    start_date=start_date.strftime("%Y-%m-%dT%H:%M"),  # noqa: E501
                                    end_date=end_date.strftime("%Y-%m-%dT%H:%M"))  # noqa: E501

        self.assertEqual(response.status_code, 200)

        end_date = start_date + timedelta(minutes=-10)
        invalid_form = self.update_task(task_id=task.id,
                                        title=None,
                                        priority=5,
                                        description='new task description',
                                        start_date=start_date.strftime("%Y-%m-%dT%H:%M"),  # noqa: E501
                                        end_date=end_date.strftime("%Y-%m-%dT%H:%M"))  # noqa: E501

        self.assertEqual(invalid_form.status_code, 200)

        # This doesnt actually check whether the updated task has the right info though, just whether it'll break stuff

    def test_delete_task_view(self):
        '''
        TEST DELETE TASK
        '''
        task = Task(title="delete task", priority=1,
                    description="delete task description",
                    start_time=datetime.now(),
                    end_time=datetime.now())
        db.session.add(task)
        db.session.commit()

        task = Task.query.filter_by(title='delete task').first()

        path = '/task/delete/{}'.format(task.id)
        response = self.client.get(path, follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        db_user = Task.query.filter_by(id=task.id).first()
        self.assertEqual(db_user, None)

    #@unittest.expectedFailure
    def test_delete_multiple_tasks(self):
        tasks = [Task(title=str(i), priority=1,
                      description="delete task description",
                      start_time=datetime.now(),
                      end_time=datetime.now()) for i in range(5)]
        [db.session.add(i) for i in tasks]
        db.session.commit()
        ids = [str(tasks[i].id) for i in range(len(tasks))]
        path = '/task/delete/{}'.format(",".join(ids))
        response = self.client.get(path, follow_redirects=True)
        self.assertEqual(response.status_code, 200, path)

        for i in ids:
            db_user = Task.query.filter_by(id=i).first()
            self.assertEqual(db_user, None, id)
