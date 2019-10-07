#problema 1 : time-convertion
import sys

def timeConversion(s):
    formato = s[-2:] #variable que solo me trae los ultimos 2 caracteres
    th = s[:2] #variable que solo toma las horas (primeros 2 nums)
    #ciclo que revisa el formato de la hora (AM/PM)
    if formato == 'AM':
        if  th == '12': #ciclo que comprueba la hora
            return "00" + s[2:8]
        else:
            return s[:-2] #regresa todo el string, menos el formato
    #si no cumple con el ciclo anterior, solo se comprueba la hora
    elif th == '12':
            return s[:-2] #regresa todo el string, menos el formato
    else:
            i = int(th) + 12 #se transforma el string a int para efectuar la suma, y asignar el resultado a la var. i
            return  str(i) + s[2:8] #la variable i se vuelve a transformar a string para poder hacer la concatencacion de min y seg



s = input().strip()
result = timeConversion(s)
print(result)
