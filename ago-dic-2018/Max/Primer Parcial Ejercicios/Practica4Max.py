def format_LEDs(led):
    num = [] #Lista vacia
    i = 0
    LEDsTotal = 0
    led = str(led) #tranformo un int a str
    while i < len(led): #teniendo el dato como str puedo usar "len"
        num.append(led[i]) #agrego el dato a la lista para poder manejarlo a gusto
        i += 1
#############################################
    for i in num: #recorro la lista
        if i == '1':
            LEDsTotal += 2
        if i == '2':
            LEDsTotal += 5
        if i == '3':
            LEDsTotal += 5
        if i == '4':
            LEDsTotal += 4
        if i == '5':
            LEDsTotal += 5
        if i == '6':
            LEDsTotal += 6
        if i == '7':
            LEDsTotal += 3
        if i == '8':
            LEDsTotal += 7
        if i == '9':
            LEDsTotal += 6
        if i == '0':
            LEDsTotal += 6
########################################################
    print('La cantidad de LEDs total que usara sera: "{}" LEDs'.format(LEDsTotal))
    LEDsTotal = led #regreso led de str a int
    return led

if __name__ == '__main__':
    led = int(input('Dame un numero: '))
    res = format_LEDs(led)
