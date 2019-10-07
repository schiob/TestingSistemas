	#!/bin/python3

import sys

#Encontrar el número mayor.
#Encontrar sus ocurrencias en el arreglo.


def birthdayCakeCandles(n, ar):
	ar.sort()
	mayor = ar[len(ar)-1]
	ocurrencias = 0
	for i in ar:
		if(mayor == i): ocurrencias+=1	
	return ocurrencias

