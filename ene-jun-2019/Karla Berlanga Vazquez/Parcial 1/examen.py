""" Función que toma un string representando la hora en formato de 24 hrs HH:MM hrs
y regresa un string con el formato de un reloj de 12 """

def reloj(hora):
    lista_hora = hora.split(":") #separamos de esta manera HH, MMhrs
    minutos_separados = [i for i in lista_hora[1] if i.isdigit()] #le quitamos a los minutos la parte de 'hrs'
    minutos= minutos_separados[0]+minutos_separados[1] #juntamos los minutos de la lista anterior "minutos_separados"
    hora_separada=[int(lista_hora[0]), int(minutos)] #en una lista guardamos la hora y los minutos

    if(hora_separada[0]<12 and hora_separada[0]>0): #las horas que van desde las 1:00 hasta las 11:59 se quedan iguales
        if(hora_separada[0]>0 and hora_separada[0]<=9):
            hora_12 = "0"+str(hora_separada[0]) + ":" + minutos + "a.m." #las que van desde la 1:00 hasta las 9:00 agregamos un cero por formato
        else:
            hora_12 = str(hora_separada[0]) + ":" + minutos + "a.m."
    elif(hora_separada[0] == 0):
        hora_12 = "12"+ ":" + minutos + "a.m."
    elif(hora_separada[0] == 12):
        hora_12 = "12"+ ":" + minutos + "p.m."
    elif(hora_separada[0] > 12 and hora_separada[0] <= 23): #las horas que van desde las 13:00 hasta las 23:59 le quitamos 12 horas para ponerlo en formato de 12 hrs
        if(hora_separada[0] > 12 and hora_separada[0] <= 21): #las que van desde la 12:00 hasta las 21:59 agregamos un cero por formato
            hora_12= "0"+str(hora_separada[0]-12) + ":" + minutos + "p.m."
        else:
            hora_12= str(hora_separada[0]-12) + ":" + minutos + "p.m."

    return hora_12
