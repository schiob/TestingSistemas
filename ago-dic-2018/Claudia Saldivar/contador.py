import math
lista=int(input("Cuantos numeros que quieres?: "))
if lista>0:
    par=0
    impar=0
    negativo=0
    positivo=0
    for i in range(lista):
        Numeros=int(input("Ingrese numero: "))
        if Numeros % 2 == 0:
            par = par + 1
        else:
            impar = impar + 1
        if Numeros > 0:
            positivo += 1
        elif Numeros < 0:
            negativo += 1
print(positivo, "positivo")
print(negativo, " negativo")
print(par, "par")
print(impar, "impar")
