#Diccionario de leds
#leds = {"1": 2, "2": 5, "3": 5, "4": 4, "5": 5, "6": 6, "7": 3, "8": 7, "9": 6, "0": 6}
#Crear función
def calcularLeds(entrada):
	leds = 0
	
	for i in range(0,  len(entrada)):
		
		if entrada[i] == '1':
			leds += 2
		elif entrada[i] == '2':
			leds += 5
		elif entrada[i] == '3':
			leds += 5
		elif entrada[i] == '4':
			leds += 4
		elif entrada[i] == '5':
			leds += 5
		elif entrada[i] == '6':
			leds += 6
		elif entrada[i] == '7':
			leds += 3
		elif entrada[i] == '8':
			leds += 7
		elif entrada[i] == '9':
			leds += 6
		elif entrada[i] == '0':
			leds += 6

	return leds

if __name__ == '__main__':
	#Recibir una entrada
	entrada = str(input("Ingresa un número de entrada")).split(",")
	#iniciar la lista de strings
	#leds = entrada [0]
	salida = calcularLeds(entrada)
	print ("Número de LEDs que necesitará: {}".format(salida))
    