def Horarios(horas):
    hora=int(tiempo[0:2])
    minuto=(tiempo[3:5])
    segundo=(tiempo[6:8])

    if tiempo[7:55]=="AM":    
        if hora==12:
            hora="00"
    elif tiempo[7:55]=="PM":
        if hora>=1 and hora<=11:
            hora+=12

    Horasde24= str(hora) + ":" + str(minuto) + ":" + str(segundo)
    return Horasde24

if __name__ == '__main__':
    tiempo=input("Agrega la hora a convertir, escrito asi (hh:mm:ss AM/PM): ")
    resultado = Horarios(tiempo)
print(resultado)