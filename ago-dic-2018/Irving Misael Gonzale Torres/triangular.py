def Triangular(n):
	Ntriangular = ((n*(n+1)))/2
	return 	Ntriangular

if __name__ == '__main__':
	n = int(input("dame un número representando la posición del triangular. "))
	resultado = int(Triangular(n))
	print("{} - {}".format(n,resultado))
