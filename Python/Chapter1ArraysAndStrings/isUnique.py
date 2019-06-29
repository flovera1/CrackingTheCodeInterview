"""
Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?
"""
lista 	= str(input("calcular caracteres unicos a: "))

MySet 	= set()
MyBool 	= False
for element in lista:
	if not(element in MySet):
		MySet.add(element)
		MyBool = False
	else:
		MyBool = True
		

if (MyBool):
	print("Si hay elementos repetidos")
else:	
	print("No hay elementos repetidos")