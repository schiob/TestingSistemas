#creando una variable (numeros) de tipo 'lista'
numeros=list(map(int, input("Ingresa 5 números enteros separados por espacios: ").split()))
#imprimiendo la lista 'numeros'
print(numeros)
#creando variables acumuladores
positivos=0
negativos=0
pares=0
impares=0
#usando un ciclo para recorrer los 5 números ingresados
for x in numeros:
	if x >=0:
		positivos+=1
		if x%2==0:
			pares+=1
		else:
			impares+=1
	if x<0:
		negativos+=1
		if x%2==0:
			pares+=1
		else:
			impares+=1

print(positivos,"número(s) positivo(s)")
print(negativos,"número(s) negativos(s)")
print(pares,"número(s) par(es)")
print(impares,"número(s) impar(es)")
