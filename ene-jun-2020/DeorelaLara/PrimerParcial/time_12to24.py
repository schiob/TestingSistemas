"""
ALUMNO(A) : Alvarado Lara Luz Deorela Sabas
Matricula: 10021265
"""
def time_to24(time):
    #VERIFICAMOS SI EL USUARIO INGRESO AM O PM RECORRIENDO 
    # DESDE LA PENULTIMA POSICION DE NUESTRA LISTA
    period = time[-2:]
    #OBTENEMOS LA PRIMERA POSICION DE NUESTRA LISTA, QUE ES LA HORA QUE QUEREMOS CONVERTIR
    hours = int(time.split(':')[0])
    #print(hours)
    if period == 'AM':
        if hours == 12:
            hours = 0
            #minutos
            #print(time[2:-2])
        return str(hours).zfill(2) + time[2:-2] + 'AM' #RELLENAMOS CON CEROS 
    elif period == 'PM':
        if hours != 12:
            hours += 12
        return str(hours).zfill(0) + time[2:-2] + 'PM' 


def main():
    
    print('Ingresa la hora que deseas convertir en formato 12Hrs -->  11:40 AM/PM')
    time = input().strip()
    print(time_to24(time))


if __name__ == '__main__':
    main()