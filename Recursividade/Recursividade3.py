#Defina em Python uma função recursiva g3 que recebe como argumento uma lista de listas de números inteiros ‘w’ e devolve True se algumas das listas em ‘w’ tiver mais números pares do que ímpares e False em caso contrário.
def pares(lista):
	if lista == [ ]:
		return 0
	else:
		if lista [0] % 2 == 0:
			return 1 + pares(lista[1:])
		else:
			return 0 + pares(lista[1:])

def g3(w):
	if w == [ ]:
		return 0
	else:
		if pares(w[0]) == 1:
			return True + g3(w[1:])
		else:
			return False

g3([[2,4,3,1],[3,5,7],[8,1,6]])