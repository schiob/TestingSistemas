#!/bin/python3

import sys

def suma_nums(arr):
	contador =0
	lista = []	
	while contador < 5:		
		suma = 0		
		for i in arr:
			suma+=i					
		suma-=arr[contador]
		lista.append(suma)
		contador+=1
	lista.sort()

	resultado = "%d %d" %(lista[0],lista[len(lista)-1])	
	return resultado	


