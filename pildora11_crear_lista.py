lista=[]
for elemento in range(1,6):
	lista.append(elemento)
lista.insert(2,9)
print(lista)
for elemento in lista:
	print(elemento)
	if elemento==2:
		print("este es el numero: "+str(elemento))
