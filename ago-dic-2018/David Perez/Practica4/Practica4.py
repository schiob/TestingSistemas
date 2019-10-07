#Práctica 4: Problemita de leds.
def Led(n):
    n=str(n)
    leds = 0
    for i in range(0, len(n)):
        if n[i] == '1':
            leds = leds + 2
        elif n[i] in '235':
            leds = leds + 5
        elif n[i] in '690':
            leds = leds + 6
        elif n[i] == '7':
            leds = leds + 3
        elif n[i] == '8':
            leds = leds + 7
        elif n[i] == '4':
            leds = leds + 4

    return leds


if __name__ == '__main__':
    n=str(input('Número a representar: '))
    res = Led(n)

    print("Se nesesitan {} leds".format(res))
