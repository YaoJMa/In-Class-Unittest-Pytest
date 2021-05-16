import unittest 
from palindrome import *

class TestPalindrome(unittest.TestCase):
	
	def test_mirrored(self):
		assert isPalindrome('') is True
		assert isPalindrome('A') is True
		assert isPalindrome('BB') is True
		assert isPalindrome('racecar') is True

	
	def test_capital(self):
		assert isPalindrome('rAcECaR') is True
		assert isPalindrome('Bb') is True

	def test_whitespace(self):
		assert isPalindrome('race car') is True

	def test_capital_whitespace(self):
		assert isPalindrome('Race Car') is True

	def test_punc(self):
		assert isPalindrome('race car!') is True

	def test_false(self):
		assert isPalindrome('word') is False
		assert isPalindrome('ABC') is False

if __name__ == '__main__':
	unittest.main()
