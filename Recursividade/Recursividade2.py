#Defina em Python uma função g2 que recebe como argumento uma lista de listas de números inteiros ‘w’ e devolve True se em todas as sublistas de ‘w’ existir um número positivo. A função deve devolver False se em alguma lista não existir um número positivo.
def pos(lista):
	if lista == [ ]:
		return 0
	else:
		if lista [0] > 0:
			return 1 + pos(lista[1:])
		else:
			return 0

def g2(w):
	if w == [ ]:
		return 0
	else:
		if pos(w[0]) == 1:
			return True + g2(w[1:])
		else:
			return False

g2([[2,4,3,1],[3,-5,-7],[],[8,0,-6]])