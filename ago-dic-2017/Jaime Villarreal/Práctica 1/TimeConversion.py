#!/bin/python3

# HackerRank Problema 1: Time Conversion.

import sys, time

def timeConversion(s):
	# http://strftime.org/
	# Crea un objeto time representado por el formato en los parámetros.
	t = time.strptime(s, "%I:%M:%S%p")
	# Crea de vuelta un string con el formato especificado en 24-h.
	conversion = time.strftime("%H:%M:%S", t)
	return conversion

if __name__ == '__main__':
	s = input().strip()
	result = timeConversion(s)
	print(result)
