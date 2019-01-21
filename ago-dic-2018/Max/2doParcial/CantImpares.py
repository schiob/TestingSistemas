import math

def cantImpar(x, y):
    if x < y:
        sumatotal = 0
        impar = 0
        i = x+1
        while i <= y:
            if i % 2 != 0:
                sumatotal = sumatotal + i
            i += 1
        print('Suma de los numeros impares: ' + str(sumatotal))
        return sumatotal
    else:
        sumatotal = 0
        impar = 0
        i = y+1
        while i <= x:
            if i % 2 != 0:
                sumatotal = sumatotal + i
                print(i)
            i += 1
        print('Suma de los numeros impares: ' + str(sumatotal))
        return sumatotal

if __name__ == '__main__':
    x = int(input('Numero entero 1: '))
    y = int(input('Numero entero 2: '))
    cantImpar(x, y)
