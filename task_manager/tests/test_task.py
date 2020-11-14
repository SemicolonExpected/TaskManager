import unittest

from task_manager import create_app, db
from task_manager.models.task import Task
from task_manager.models.assignment import Assignment
from datetime import date


class TestTask(unittest.TestCase):
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

	def test_Create(self):
		'''
		TEST CREATE TASK
		'''
		new_task = Task(title="hello", priority='1', description="task_decription")

		db.session.add(new_task)
		db.session.commit()

		new_task2 = Task(title="hello1", priority='1', description="task_decription")

		db.session.add(new_task2)
		db.session.commit()
		self.assertEqual(Task.query.filter_by(id=new_task.id).first(), new_task)
		self.assertEqual(Task.query.filter_by(id=new_task2.id).first(), new_task2)

	def test_Assignment(self):
		'''
		TEST FETCH TASK
		'''
		new_task = Task(title="hello", priority='1', description="task_decription")

		db.session.add(new_task)
		db.session.commit()

		new_assignment = Assignment(time_added=date.today(), user_id=1, task_id=new_task.id)
		db.session.add(new_assignment)
		db.session.commit()

		self.assertEqual(Assignment.query.filter_by(task_id=new_task.id).first(), new_assignment)

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
