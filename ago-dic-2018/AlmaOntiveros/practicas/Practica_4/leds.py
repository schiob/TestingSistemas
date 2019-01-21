def focosleds(num):
    lista = []
    i = 0
    leds = 0
    num = str(num)
    while i < len(num):
        lista.append(num[i])
        i += 1

    for n in lista:
        if n == "0":
            leds += 6
        if n == "1":
            leds += 2
        if n == "2":
            leds += 5
        if n == "3":
            leds += 5
        if n == "4":
            leds += 4
        if n == "5":
            leds += 5
        if n == "6":
            leds += 6
        if n == "7":
            leds += 3
        if n == "8":
            leds += 7
        if n == "9":
            leds += 6
            
    print("El número", num, "necesita: {} leds".format(leds))
    return leds
    
if __name__ == '__main__':
    num = int(input("Ingresa el numero de entrada: "))
    resultado = focosleds(num)