def doce_to24(tiempo):    # Cambié el nombre porque me manda un error :v

    periodo = tiempo[-2:]
    horas = int(tiempo.split(':')[0])

    if periodo == 'AM':
        if horas == 12:
            horas = 0
        return str(horas).zfill(2) + tiempo[2:-2] + 'HRS'  #
    elif periodo == 'PM':
        if horas != 12:
            horas += 12
        return str(horas).zfill(0) + tiempo[2:-2] + 'HRS'


def main():
    print('Ingresa la hora que vas a convertir a form. de 12Hrs\nPor ejemplo: 07:00 PM')
    tiempo = input().strip()
    print(doce_to24(tiempo))


if __name__ == '__main__':
    main()
