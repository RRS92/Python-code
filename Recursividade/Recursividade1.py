#Defina em Python uma função recursiva g1 que recebe como argumento uma lista de listas de números inteiros ‘w’ e devolve o número de elementos pares que existem nas sublistas de ‘w’.
def par(lista):
	if lista == [ ]:
		return 0
	else:
		if lista [0] % 2 == 0:
			return 1 + par(lista[1:])
		else:
			return par(lista[1:])


def g1(w):
	if w == [ ]:
		return 0
	else:
		return par(w[0]) + g1(w[1:])

g1([[1,4,3,1],[3,5,7],[],[8,5,6]])