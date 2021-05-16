import pytest
from palindrome import * 

@pytest.fixture
def is_palindrome()->List[str]:
	return ["a","aba"]

@pytest.fixture
def not_palindrome()->List[str]:
	return ["bacb", "car"]

def test_isPalindrome(is_Palindrome: List[str]):
	for value in isPalindrome:
		assert isPalindrome(value)

def test_notPalindrome(not_isPalindrome: List[str]):
	for value in isPalindrome:
		assert not isPalindrome(value)

