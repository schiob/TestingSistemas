def NumLeds(led):
    num = [] 
    x = 0
    NLeds = 0
    led = str(led) 
    while x < len(led): 
        num.append(led[x]) 
        x += 1

    for x in num:
        if x == '1':
            NLeds += 2
        if x == '2':
            NLeds += 5
        if x == '3':
            NLeds += 5
        if x == '4':
            NLeds += 4
        if x == '5':
            NLeds += 5
        if x == '6':
            NLeds += 6
        if x == '7':
            NLeds += 3
        if x == '8':
            NLeds += 7
        if x == '9':
            NLeds += 6
        if x == '0':
            NLeds += 6
       
    print('La cantidad de LEDs totales son: "{}" LEDs'.format(NLeds))
    NLeds = led 
    return led

if __name__ == '__main__':
    led = int(input('Digita un numero para conocer la cantidad de leds necesarios: '))
    res = NumLeds(led)
