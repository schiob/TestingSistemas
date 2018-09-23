def leds(str):
    led = 0
    for i in range(0, len(n)):
        if n[i] == '1':
            led = led + 2
        elif n[i] in '235':
            led = led + 5
        elif n[i] in '690':
            led = led + 6
        elif n[i] == '7':
            led = led + 3
        elif n[i] == '8':
            led = led + 7
        elif n[i] == '4':
            led = led + 4

    return led


if __name__ == '__main__':
    n=str(input('Dame el numero: '))
    res = leds(n)

    print("Usted nesesita {} leds".format(res))
