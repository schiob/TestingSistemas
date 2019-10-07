def calcular(lista):
	par = impar = positivo = negativo = 0

	for num in lista:
		if num % 2 == 0:
			par += 1
		else:
			impar += 1
		if num < 0:
			negativo += 1
		elif num >= 0:
			positivo += 1
	return par, impar, negativo, positivo

if __name__ == '__main__':
	#cantidadYnumeros
	n = int(input('Teclea los numeros'))
	#convierte el input en entero
	
	nums = list(map (int, input().split(" ")))

	#Resultado de la funcion
	cantidad = calcular(nums)

	print ("número(s) par(es): {}".format(cantidad[0]))
	print ("número(s) impar(es): {}".format(cantidad[1]))
	print ("número(s) negativo(s): {}".format(cantidad[2]))
	print ("número(s) positivo(s): {}".format(cantidad[3]))