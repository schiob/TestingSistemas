listaNumeros = []

def juanita(cantidadNumeros: int):
    integerToAppend = 0
    for i in range(cantidadNumeros):
        integerToAppend = input('Inserte el numero que le gustaria almacenar: ')
        listaNumeros.append(integerToAppend)
    
    return listaNumeros

def numerosPositivos(lista: list):
    numerosPositivos = 0
    for i in range(len(lista)):
        if (sign(int(lista[i]))):
            numerosPositivos += 1

    return numerosPositivos

def numerosNegativos(lista: list):
    numerosNegativos = 0
    for i in range(len(lista)):
        if (not sign(int(lista[i]))):
            if (int(lista[i]) != 0):
                numerosNegativos += 1

    return numerosNegativos

def numerosPares(lista: list):
    numerosPares = 0
    for i in range(len(lista)):
        if (abs(int(lista[i])) % 2 == 0):
            numerosPares += 1

    return numerosPares

def numerosImpares(lista: list):
    numerosImpares = 0
    for i in range(len(lista)):
        if (abs(int(lista[i])) % 2 != 0):
            numerosImpares += 1

    return numerosImpares

def sign(x):
    return int(x>0) 

if (__name__ == '__main__'):
    cantidadNumeros = int(input('Inserte la cantidad de n numeros: '))
    print(juanita(cantidadNumeros))
    print('Numeros positivos: ', numerosPositivos(listaNumeros))
    print('Numeros negativos: ', numerosNegativos(listaNumeros))
    print('Numeros pares: ', numerosPares(listaNumeros))
    print('Numeros impares: ', numerosImpares(listaNumeros))