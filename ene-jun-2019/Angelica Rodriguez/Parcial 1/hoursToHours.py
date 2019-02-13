"""
Programa que lee un string representando la hora en formato de
24 horas: HH:MMhrs y regresa un string con el formato de un
reloj de 12.
"""

def convertHours(stringHora):
    """función que convierte la hora en un formato de 24 horas a uno de 12"""
    try:
        horas = stringHora.split(':')  # cortamos el string
        minutos = horas[1].split('hrs')  # cortamos el string
        horas = int(horas[0])  # obtenemos la hora
        minutos = int(minutos[0])  # obtenemos los minutos

        if horas > 12:
            horas = horas-12   # convertimos la hora a formato de 12 hrs
            return """0{}:{}p.m.""".format(horas, minutos).strip()
        elif horas < 12:
            return """0{}:{}a.m.""".format(horas, minutos).strip()
        else:  # cuando la hora sea 12
            return """{}:{}p.m.""".format(horas, minutos).strip()
    except:
        return "Entrada incorrecta"
