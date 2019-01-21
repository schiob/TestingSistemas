def CalcularLeds(numero):
    ListaNumero=[]
    i=0
    Leds=0
    numero=str(numero)
    while i < len(numero):
        ListaNumero.append(numero[i])
        i += 1
    for i in ListaNumero:
        if i == '1':
            Leds += 2
        if i == '2':
            Leds += 5
        if i == '3':
            Leds += 5
        if i == '4':
            Leds += 4
        if i == '5':
            Leds += 5
        if i == '6':
            Leds += 6
        if i == '7':
            Leds += 3
        if i == '8':
            Leds += 7
        if i == '9':
            Leds += 6
        if i == '0':
            Leds += 6


    print('El numero',numero, 'Tiene la cantidad de:"{}"leds'.format(Leds))
    return Leds

if __name__=='__main__':
    numero=int(input('ingrese numero:'))
    resultado=CalcularLeds(numero)
