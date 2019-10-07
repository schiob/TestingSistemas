def calculo(nums):
	positivo = 0
	negativo = 0
	par = 0
	impar = 0
	cero = 0
	for n in nums:
		if n > 0 and n != 0:
		    positivo = positivo + 1
		    if (n % 2) == 0:
		        par = par + 1
		    else:
		        impar = impar + 1
		elif n < 0 and 	n != 0:
		    negativo = negativo + 1
		    if (n % 2) == 0:
		        par = par + 1
		    else:
		        impar = impar + 1
		else:
			cero = cero + 1

	return cero, positivo, negativo, par, impar 

if __name__ == '__main__':
	n = int(input("teclee la cantidad de números que tendra la lista: "))
	nums = list(map(int, input("teclee los numeros separados por espacio: ").split(" ")))
	result = calculo(nums)

	print("ceros = {}".format(result[0]))
	print("positivos = {}".format(result[1]))
	print("negativos = {}".format(result[2]))
	print("pares = {}".format(result[3]))
	print("impares = {}".format(result[4]))
