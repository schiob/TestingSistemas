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
        minutos = int(minutos[0])
        h = 0
        m = 0
        masdoce = 0
        if horas == 0:
            horas = "00"
            h = 1
        if minutos == 0:
            minutos = "00"
            m = 1
        if horas > 12:
            horas = horas-12
            masdoce = 1
        #print(horas)

        if m == 1:
            if masdoce == 1:
                if horas < 12 and horas < 10:
                    return """0{}:{}p.m.""".format(horas, minutos).strip()
                if horas >9 and horas < 12:
                    return """{}:{}p.m.""".format(horas, minutos).strip()
            else:
                if horas < 10:
                    return """0{}:{}p.m.""".format(horas, minutos).strip()
                if horas > 9:
                    return """{}:{}p.m.""".format(horas, minutos).strip()
        else:
            if masdoce == 1:
                if horas < 12 and horas < 10 and minutos >10:
                    return """0{}:{}p.m.""".format(horas, minutos).strip()
                if horas < 12 and horas < 10 and minutos < 10:
                    return """0{}:0{}p.m.""".format(horas, minutos).strip()
                if horas >9 and horas < 12 and minutos > 10:
                    return """{}:{}p.m.""".format(horas, minutos).strip()
                if horas >9 and horas < 12 and minutos < 10:
                    return """{}:0{}p.m.""".format(horas, minutos).strip()

            else:
                if horas < 10 and minutos > 10:
                    return """0{}:{}a.m.""".format(horas, minutos).strip()
                if horas < 10 and minutos < 10:
                        return """0{}:0{}a.m.""".format(horas, minutos).strip()
                if horas > 9 and horas < 12 and minutos > 10:
                    return """{}:{}a.m.""".format(horas, minutos).strip()
                if horas > 9 and horas < 12 and minutos < 10:
                    return """{}:0{}a.m.""".format(horas, minutos).strip()


    except:
        return "Entrada incorrecta"

if __name__ == '__main__':
    print(convertHours('00:00hrs'))
