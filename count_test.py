import unittest
from wordcount import wordcount

class Test_Word_Count(unittest.Testcase):

	def test_count(self):
		self.assertEqual(
			isWordcount('hi'),
			{'hi':1}
		)

	def test_count_many(self):
		self.assertEqual(
			isWordcount('hi there hello'),
			{'hi':1, 'there':1, 'hello':1}
		)

	def test_multiple(self):
		self.assertEqual(
			isWordcount('one one two two'),
			{'one':1, 'two':1}
		)
	
	def test_punc(self):
		self.assertEqual(
			isWordcount('one: two: three:'),
			{'one':1, 'two':1, 'three':1}
		)

if __name__ == '__main__':
	unittest.main()
