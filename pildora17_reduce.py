from functools import reduce
#
def suma(a,b):
	return a+b
#
numeros=[2,1,4,3,5]
#resultado=reduce(suma,numeros)
resultado=reduce(lambda a,b: a if a > b else b,numeros)
print (resultado)
