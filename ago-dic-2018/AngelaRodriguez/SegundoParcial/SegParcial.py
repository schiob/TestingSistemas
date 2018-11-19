def suma(rango):
	SumaImpar=0
	#num1 = int(input("Escriba un número: "))
	#num2 = int(input("Escriba otro numero: "))

	if num1 > num2:
		for num in range((num2 + 1), (num1 - 1)):
			if num % 2 != 0:
				SumaImpar += num
		return SumaImpar
	else:
		for num in range((num1 + 1), (num2 - 1)):
			if num % 2 != 0:
				SumaImpar += num
		return SumaImpar


if __name__ == '__main__':

	num=int(input())
	num1 , num2= list(map(int,input('Escribe los números del rango separados con un espacio: ').split(" ")))

	resultado=suma(num)
	print('La suma de los numeros impares es: ', resultado)
