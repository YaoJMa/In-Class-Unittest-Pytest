import pytest 
from wordcount import wordcount

@pytest.mark.parametrize("str1", [
	('hello world', 2),
	('hello there how are you', 5),
	('how are you doing on this fine day?', 8)
])

def test_wordcount(self):
	assert wordcount("hello there") == 3
