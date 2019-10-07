def ContarLeds(leds):
	leds = str(leds)
	lista = []
	contador = 0
	i = 0
	while i < len(leds):
		lista.append(leds[i])
		i +=1

	for i in lista:
		if i == '0':
			contador += 6
		if i == '1':
			contador += 2
		if i == '2':
			contador += 5
		if i == '3':
			contador += 5
		if i == '4':
			contador += 4
		if i == '5':
			contador += 5
		if i == '6':
			contador += 6
		if i == '7':
			contador += 3
		if i == '8':
			contador += 7
		if i == '9':
			contador += 6

	
	print("El total de leds a usar es:",contador)
	return leds

if __name__ == '__main__':
	leds = int(input("Teclea el numero para calcular el total de leds: "))
	respuesta = ContarLeds(leds)