file=open("file2.txt","w")
#for i in range(2):
#	palabra=input("Ingresa una palabra: ")
#	file.write(palabra+str("\n"))
lista=["linea1\n","linea2\n","linea3\n"]
file.writelines(lista)
