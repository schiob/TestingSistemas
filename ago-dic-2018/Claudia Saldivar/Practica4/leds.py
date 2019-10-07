def Leds(led):
    numero = []
    i= TotalLeds = 0
    led = str(led)
    while i < len(led):
        num.append(led[i])
        i += 1

    for i in numero:

        if i == '1':
            TotalLeds += 2
        if i == '2' or '3' or '5':
            TotalLeds+= 5
        if i == '4':
            TotalLeds += 4
        if i == '6' or '9' or '0':
            TotalLeds += 6
        if i == '7':
            TotalLeds += 3
        if i == '8':
            TotalLeds += 7

    print('La cantidad de Leds: "{}" Leds'.format(TotalLeds))
    TotalLeds = led
    return led

if __name__ == '__main__':
    led = int(input('Dame un numero: '))
    resultado = Leds(led)
