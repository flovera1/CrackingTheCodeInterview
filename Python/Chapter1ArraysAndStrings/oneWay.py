'''
There are three types of edits that can be performed on strings, insert, remove or replace a character.
Given two strings, write a function to check if they are one edit (or zero edits) away.
Example:
pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bake -> false
'''
def oneAway(s1, s2):
	"""
		check if a string (s1) can be converted to another string (s2) with
		edits, remove and insert.
	"""
	if len(s1) == len(s2):
		return checkEdit(s1, s2)
	elif len(s1) + 1 == len(s2):
		return checkInsert(s1, s2)
	elif len(s1) - 1 == len(s2):
		return checkInsert(s2, s1)

	return False

def checkEdit(s1, s2):
    edited = False
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            if edited:
                return False
            edited = True
	return True

def checkInsert(s1, s2):
	edited = False
	i, j = 0, 0
	while i < len(s1) and j < len(s2):
		if s1[i] != s2[j]:
			if edited:
				return False
			edited = True
			j += 1
		else:
			i += 1
			j += 1
	return True


print(oneAway("pale", "ple"))