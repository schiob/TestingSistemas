def Ntriangular(n):
	nt=int((n*(n+1))/2)

	return nt

if __name__ == '__main__':
	n=int(input("Escribe el triangular que requieres"))
	resultado=Ntriangular(n)
	print("El numero triangular es: ",resultado)
