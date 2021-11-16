def imprimir():
	print("esta es una funcion")
#
def imprimir_numero(num):
	print("el numero ingresado es: "+str(num))
#
def sumar(num1,num2):
	suma=num1+num2
	return suma
#
# programa principal
imprimir()
num=int(input("ingresa un numero: "))
imprimir_numero(num)
num1=int(input("ingresa el primer numero: "))
num2=int(input("ingresa el segundo numero: "))
resultado=sumar(num1,num2)
print(resultado)

