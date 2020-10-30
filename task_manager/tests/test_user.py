import unittest


class TestUser(unittest.TestCase):
	def setup(self):
		pass

	def test_Create(self):
		'''
		TEST CREATE USER
		'''
		self.assertEqual('1', '1')

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
