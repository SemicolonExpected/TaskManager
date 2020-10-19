import unittest


class Test_User(unittest.TestCase):
	def setup(self):
		pass

	def createTest(self):
		self.assertEqual('1','1')

	def getTest(self):
		self.assertEqual('1','1')

	def updateTest(self):
		self.assertEqual('1','1')

	def deleteTest(self):
		self.assertEqual('1','1')

if __name__ == '__main__':
    unittest.main()