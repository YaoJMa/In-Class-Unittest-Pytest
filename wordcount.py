def isWordcount(str1):
	word = 1
	for i in range(len(str1)):
		if(str1[i] == ' ' or str1 == '\n' or str1 == '\t'):
			word = word+1
	return word

string = input("Please enter a sentence to count: ")
len = isWordcount(string)
print("Total number of words is: ", len)
