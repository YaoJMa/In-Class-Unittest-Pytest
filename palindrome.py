def isPalindrome(s):
	#command to rev string to compare
	rev = ''.join(reversed(s))

	#checks word
	if(s==rev):
		return True
	return False

#asks user for input
s = input("Please enter a word: ")
ans = isPalindrome(s)

#displays to user if word is a palindrome or not
if(ans):
	print("Is a Palindrome")
else:
	print("Is not a Palindrome")
