def switchleds(x):
    return {
        '1': 2,
        '2': 5,
        '3': 5,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 3,
        '8': 7,
        '9': 6,
        '0': 6
    }[x]

def cuentaleds(number):
    leds = 0
    number = str(number)
    for num in number:
        leds += switchleds(num)
    return leds
if __name__ == '__main__':
    try:
        number = int(input("Ingresa el número del que quieres conocer Led's: "))
        print("El numero de led's que necesitas para el número {} es: {}".format(number, cuentaleds(number)))
    except: ValueError(print('Error, tienes que teclear un numero válido para proceder'))
