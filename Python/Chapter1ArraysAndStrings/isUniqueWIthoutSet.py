"""
Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?
"""
lista = str(input("Introduzca el string a computar: "))
MyBool = False
for indx, val in enumerate(lista):
	i = 0
	temp = lista[indx]
	resto = lista[indx+1:]
	for val in resto:
		if val == temp:
			print("Si esta repetido")
			break
		else:
			print("No esta repetido")
