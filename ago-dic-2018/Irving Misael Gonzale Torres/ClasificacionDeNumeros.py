positivo = 0
negativo = 0
par = 0
impar = 0
cero = 0

n = int(input("teclee la cantidad de números que tendra la lista: "))
lista=[int(i) for i in (input("teclee los numeros separados por espacio: ").split(' '))]

for i in lista[:n]:
	if i > 0 and i != 0:
	    positivo = positivo + 1
	    if (i % 2) == 0:
	        par = par + 1
	    else:
	        impar = impar + 1
	elif i < 0 and i != 0:
	    negativo = negativo + 1
	    if (i % 2) == 0:
	        par = par + 1
	    else:
	        impar = impar + 1
	else:
		cero = cero + 1
		
print(str(cero) + " cero(s)")
print(str(positivo) + " Número(s) Positivo(s).")
print(str(negativo) + " Número(s) Negativo(s).")
print(str(par) + " Número(s) Par.")
print(str(impar) + " Número(s) Impar.")
