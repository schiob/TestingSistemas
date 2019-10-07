def leds(led):
    lista = []
    i = 0
    foquitos = 0
    led = str(led)
    while i < len(led):
        lista.append(led[i])
        i += 1

    for n in lista:
        if n == '0':
            foquitos += 6

        if n == '1':
            foquitos += 2

        if n == '2':
            foquitos += 5

        if n == '3':
            foquitos += 5

        if n == '4':
            foquitos += 4

        if n == '5':
            foquitos += 5

        if n == '6':
            foquitos += 6

        if n == '7':
            foquitos += 3

        if n == '8':
            foquitos += 7

        if n == '9':
            foquitos += 6

    print('El numero', led, 'necesita: {} leds'.format(foquitos))
    return foquitos

if __name__ == '__main__':
    led = int(input('Teclea el numero: '))
    res = leds(led)
