'''
Given a string write a function that decides if they are palindromes.
'''

def createReverse(string):
	new_string = ''
	size = len(string)
	for i in range(len(string), 0, -1):
		new_string += string[i-1]

	return new_string 

def isPalindrome(string):
	if len(string) == 0:
		return True
	else:
		if string == createReverse(string):
			return True
		else:
			return False

print(isPalindrome('121'))