def cuadrado(x):
	return x**2
#
numeros=[1,2,3,4,5]
#resultado=list(map(cuadrado,numeros))
resultado=list(map(lambda x:x**3,numeros))
print(resultado)
