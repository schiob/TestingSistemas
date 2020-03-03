
def convertir(hora_string):
    horas = hora_string[0] + hora_string[1] #En la variable de horas y minutos, determine la posicion de estos en la cadena de la hora"
    minutos = hora_string[3] + hora_string[4]  
    horas_entero = int(horas) #Converti la variable de horas y mintuos en entero para asi comparar"
    minutos_entero = int(minutos)
                                                
    if horas_entero < 12 :#Con este if determino las horas de la mañana
            return (f"{horas}:{minutos}A.M")

    if horas_entero == 12:
        return (f"{horas}:{minutos}P.M")#caso del medio dia

    if horas_entero == 00 or horas_entero == 0:
        medio_dia = "12"
        return ("{medio_dia}:{minutos}A.M") #caso de 12 de la madrugada
    
    if horas_entero > 12 and horas_entero <= 23:
        if horas_entero == 13:
            case1 = "01"
            return (f"{case1}:{minutos}P.M")
        if horas_entero == 14:
            case2 = "02"
            return (f"{case2}:{minutos}P.M")
        if horas_entero == 15:
            case3 = "03"
            return (f"{case3}:{minutos}P.M")
        if horas_entero == 16:
            case4 = "04"
            return (f"{case4}:{minutos}P.M")
        if horas_entero == 17:
            case5 = "05"
            return (f"{case5}:{minutos}P.M")
        if horas_entero == 18:
            case6 = "06"
            return (f"{case6}:{minutos}P.M")
        if horas_entero == 19:
            case7 = "07"
            return (f"{case7}:{minutos}P.M")
        if horas_entero == 20:
            case8 = "08"
            return (f"{case8}:{minutos}P.M")
        if horas_entero == 21:
            case9 = "09"
            return (f"{case9}:{minutos}P.M")
        if horas_entero == 22:
            case10 = "10"
            return (f"{case10}:{minutos}P.M")
        if horas_entero == 23:
            case11 = "11"
            return (f"{case11}:{minutos}P.M")
    if horas_entero == 24 and horas_entero == 00:
        media_noche = "12"
        return (f"{media_noche}:{minutos}A.M") #caso de la media noche


if __name__ == '__main__':
    hora = input("Escriba la hora en formato HH:MM :")
    print(convertir(hora))