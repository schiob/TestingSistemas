#!/bin/python3

# HackerRank Problema 2: Mini-Max Sum.

import sys

def minMaxSum(arr):
	# Se guardan las sumas mínimas y máximas respectivamente.
	max_sum = 0
	# En el caso de la mínima se usa un número por default más alto que 4 veces el constraint de cada número (4x10^9).
	min_sum = 999999999999999999999999999
	s = sum(arr)
	for number in arr:
		# Para cada número de la lista:
		# Si la suma de los elementos de la lista menos el número actual es mayor a la suma máxima esta se reemplaza.
		if s - number > max_sum:
			max_sum = s - number
		# Si la suma de los elementos de la lista menos el número actual es menor a la suma mínima esta se reemplaza.
		if s - number < min_sum:
			min_sum = s - number

	r = '{} {}'.format(min_sum, max_sum)
	return r

if __name__ == '__main__':
	# Pone en una lista una serie de números separados por un espacio.
	arr = list(map(int, input().strip().split(' ')))
	result = minMaxSum(arr)
	# Imprime con formato ambas sumas, P. ej.: 13 25.
	print(result)
