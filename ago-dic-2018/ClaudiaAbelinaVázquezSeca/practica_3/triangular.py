def calcularTriangular(n):
	
	numeroTriangular= ((n+1)*n) / 2

	
	return numeroTriangular

if __name__ == '__main__':	

	entrada = int(input('Introduce el número de la posicion triangular que buscas:'))
	
	resultado = calcularTriangular(entrada)

	print("número triangular: {}".format(resultado))
	