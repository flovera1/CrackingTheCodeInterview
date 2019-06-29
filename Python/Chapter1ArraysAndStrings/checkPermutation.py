"""
Check Permutation: Given two strings, write a method to decide if one is a permutation of the
other.
"""
vPrimerString = str(input("primer string: "))
vSegundoString = str(input("segundo string: "))

def checkPermutation(valPrimerString, valSegundoString):
	if (len(valPrimerString) != len(valSegundoString)):
		return False
	else:
		vOrdenado1 = ''.join(sorted(valPrimerString))
		vOrdenado2 = ''.join(sorted(valSegundoString))
		if(vOrdenado1 == vOrdenado2):
			return True
		else:
			return False


print(checkPermutation(vPrimerString, vSegundoString))