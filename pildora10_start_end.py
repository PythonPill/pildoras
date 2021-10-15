str1="este es un video para youtube"
str2=input("inserta una palabra: ")
if str1.startswith(str2):
	print("la oraccion empieza por: "+str2)
elif str1.endswith(str2):
	print("la oraccion termina por: "+str2)
else:
	print("la oraccion no empieza y no termina por: "+str2)

