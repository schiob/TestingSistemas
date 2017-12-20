#!/bin/python3

# HackerRank Problema 3: Birthday Cake Candles.

import sys

def birthdayCakeCandles(n, ar):
	# La lista que viene como parámetro es acomodada en orden descendente.
	ar.sort(reverse=True)
	# De este modo sabemos que número de tamaño más alto está en el índice 0.
	max = ar[0]
	# Se inicializa un contador de las velas que coincidan con el tamaño máximo.
	c = 0
	for item in ar:
		# Por cada número de la lista:
		# Si el tamaño máximo coincide con el actual lo cuenta.
		if max == item:
			c = c + 1
		# Si no, ya no tiene caso seguir checando los demás y termina el ciclo.
		else:
			break
	# Regresa la cuenta.
	return c

if __name__ == '__main__':
	n = int(input().strip())
	ar = list(map(int, input().strip().split(' ')))

	result = birthdayCakeCandles(n, ar)
	print(result)
