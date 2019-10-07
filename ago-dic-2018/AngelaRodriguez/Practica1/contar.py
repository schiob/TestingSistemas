positivo=0
negativo=0
par=0
impar=0

n=int(input("Cantidad de numeros a ingresar: "))

numeros = input('Dime los numeros: ')

for num in [int(n) for n in numeros.split(" ")]:
	if num>0:
		positivo = positivo + 1
	else:
	 negativo = negativo + 1

	if num %2:
		impar = impar + 1
	else:
	 par = par + 1


print ("{}, numero(s) positivo(s)" .format(positivo))
print ("{}, numero(s) negativo(s)" .format(negativo))
print ("{}, numero(s) par(es)" .format(par))
print ("{}, numero(s) impar(es)" .format(impar))