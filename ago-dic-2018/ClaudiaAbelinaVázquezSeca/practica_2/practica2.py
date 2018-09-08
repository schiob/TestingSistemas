def calcular(tamaño):
	par = impar = positivo = negativo = 0

	for num in tamaño:
		if num % 2 == 0:
			par += 1
		else:
			impar += 1
		if num < 0:
			negativo += 1
		elif num > 0:
			positivo += 1
	return par, impar, positivo, negativo

if __name__ == ' __main__':

	n = int(input())
	nums = list(map (int, input().split(" ")))
	cantidad = calc(entrada)

	print ("número(s) par(es): ".format(cantidad[0]))
	print ("número(s) impar(es): ".format(cantidad[1]))
	print ("número(s) negativo(s): ".format(cantidad[2]))
	print ("número(s) positivo(s): ".format(cantidad[3]))