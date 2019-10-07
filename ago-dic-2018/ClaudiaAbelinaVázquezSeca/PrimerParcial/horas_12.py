def convertir24(lista):
	  for nombre in lista:
        msg = nombre.title()
        print(msg)

def hora(lista)
	#for horaD12 in range(0, len(lista)):
    	for i in range(0, len(lista)):
        	lista[i] = "La hora es!!!: " + lista[i]
    	return lista #Return para hacer test
	#return hora
hora = ['02:23 p.m', '11:42 p.m', '12:00 a.m', '12:00 a.m', '12:00 p.m', '01:05 a.m', '11:59 p.m' ] 
convertir24(hora)
hora(hora)

if __name__ == '__main__':

	horaD12 = int(input("¡Que hora quieres convertir?:"))
	
	hora24 = calcularHora(horaD12)

	print("Hora!! : {}".format(hora24))

