from datetime import datetime, date, time

def cambiarhora(horaActual):
    horario = "%H:%Mhrs"
    nuevoHorario = "%I:%M%p"
    hora=horaActual
    nuevaHora=datetime.strptime(hora,horario)
    #cambiohora=datetime.strptime(hora,nuevoHorario)
    strhora=datetime.strftime(nuevaHora,horario)

    #print(nuevaHora)

    return strhora
