def par(x):
	if x%2==0:
		return True
	return False
#
numeros=[1,2,3,4,5,6,7,8,9,10]
#resultado=list(filter(par,numeros))
resultado=list(filter(lambda x:x%2!=0,numeros))
print(resultado)
