def contar_leds(num):
	Numero= []
	i=0
	cantLeds=0
	num=str(num)
	while i < len(num):
		Numero.append(num[i])

		i+=1

	for i in Numero:
		if i == '1':
			cantLeds += 2
		if i == '2':
			cantLeds += 5
		if i == '3':
			cantLeds += 5
		if i == '4':
			cantLeds += 4
		if i == '5':
			cantLeds += 5
		if i == '6':
			cantLeds += 6
		if i == '7':
			cantLeds += 3
		if i == '8':
			cantLeds += 7
		if i == '9':
			cantLeds += 6
		if i == '0':
			cantLeds += 6
	return cantLeds

if __name__ == '__main__':

	num=int(input('Ingrese el numero: '))

	resultado=contar_leds(num)

	print("Numero de leds = {}".format(resultado))
