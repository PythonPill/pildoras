file=open("file1.txt","r")
#contenido=file.read()
#linea=file.readlines()
i=1
for linea in file.readlines():
	print ("Linea numero {0}: {1}".format(i,linea))
	i+=1
