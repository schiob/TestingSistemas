def mostrar(hora):

    hra = hora.split(":")
    if (len(hra) == 0) or (len(hra) > 3):
        return hora

    hour = int(hra[0]) % 24
    am = (hour >= 0) and (hour < 12)

    if am:
        hra[0] = ('12' if (hour == 0) else "%02d" % (hour))
    else:
        hra[0] = ('12' if (hour == 12) else "%02d" % (hour - 12))

    return ':'.join(hra) + (' AM' if am else ' PM')

if __name__ == '__main__':
    print("introduce la hora en formato de 24 horas:")
    reloj = input()
    print(mostrar(reloj))