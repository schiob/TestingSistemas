def conteoLeds(num):
    contador = 0
    digitos=list(map(int, str(num)))
    for digito in digitos:
        if digito == 1:
            contador += 2
        elif digito == 2:
            contador += 5
        elif digito == 3:
            contador += 5
        elif digito == 4:
            contador += 4
        elif digito == 5:
            contador += 5
        elif digito == 6:
            contador += 6
        elif digito == 7:
            contador += 3
        elif digito == 8:
            contador += 7
        elif digito == 9:
            contador += 6
        elif digito == 0:
            contador += 6

    return contador

if __name__ == '__main__':
    n=int(input("Introduce el numero que quieres representar: "))

    resultado=conteoLeds(n)

    print("{} leds".format(resultado))
