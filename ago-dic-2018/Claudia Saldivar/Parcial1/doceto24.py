import time
import datetime

def horario(doce,minutos):

    veinticuatro = doce + 12
    tiempo = datetime.time(veinticuatro, minutos)

    return tiempo

if __name__== "__main__":

    entrada= []
    entrada = input("Hora: ").split(":")
    doce= int(str(entrada[0]))
    minutos = int(str(entrada[1]))
    ok = horario(doce,minutos)

print(ok , "hrs")
