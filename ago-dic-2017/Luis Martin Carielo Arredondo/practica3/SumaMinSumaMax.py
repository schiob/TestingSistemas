#Crear un archivo .py que calcule la suma mínima y la suma máxima entre un conjunto de 5 números.
import random

#Función para encontrar el elemento mayor de la lista de números.
def elemento_mayor(lista):
	mayor=lista[0]
	for x in range(1,5):
		if lista[x] > mayor:
			mayor = lista[x]
	return mayor

#Función para encontrar el elemento menor de la lista de números.
def elemento_menor(lista):
	menor=lista[0]
	for x in range(1,5):
		if lista[x] < menor:
			menor = lista[x]
	return menor

#Función para encontrar la suma máxima y la suma mínima de una lista de números.
def min_max(lista):
	#Obtener la suma total de los elementos de la lista de números.
	suma_total = sum(lista)
	#Obtener la suma máxima excluyendo el elemento menor de la lista de números.
	suma_max = suma_total - elemento_menor(lista)	
	#Obtener la suma mínima excluyendo el elemento mayor de la lista de números.
	suma_min = suma_total - elemento_mayor(lista)
	resultado = suma_min, suma_max
	return resultado

if __name__ == '__main__':
	lista=[]
	for x in range(5):
		lista.append(random.randint(1,10))
	print(lista)
	impresion = min_max(lista)
	print(impresion)