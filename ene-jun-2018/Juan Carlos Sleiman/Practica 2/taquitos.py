def totalizar(orden):
	total = 0
	i = 0
	#len() me da el total de items en la lista
	while len(orden) < 31 and i < len(orden) :
		if orden[i] == 'cachete':
			total = total + 13
		elif orden[i] == 'lengua':
			total = total + 10
		elif orden[i] == 'tripitas':
			total = total + 9
		elif orden[i] == 'pastor':
			total = total + 15
		elif orden[i] == 'machito':
			total = total + 14	
		i+=1
	return total
if __name__ == '__main__':
	print('''¡Bienvenido!, teclee los taquitos que desee ordenar separados por espacio; cuando tu orden este lista, teclea enter.
          MENÚ:
		  cachete
		  lengua
		  tripitas
		  pastor
		  machito''' )
	print("Máximo 30 taquitos")
	taquitos = input()
	orden = taquitos.split(' ')
	x = totalizar(orden)
	print(x)