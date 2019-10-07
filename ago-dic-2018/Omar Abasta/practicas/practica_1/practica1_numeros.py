"""Codigo que permite la identificacion de numeros enteros, ya sean positivos o
negativos, al igual que saber si son pares o impares"""


import math
lista=int(input("Teclea la cantidad de numeros que deseeas analizar: "))


if lista>0:
    par=0
    impar=0
    negativo=0
    positivo=0  
                
    for i in range(lista):
        Numeros=int(input("Ingrese dichos numero: "))
        
        
        if Numeros > 0:
            positivo += 1
        elif Numeros < 0:
            negativo += 1
            
        if Numeros % 2 == 0:
            par = par + 1
        else:
            impar = impar + 1



print("Se ha(n) encontrado ", positivo, " numero(s) positivos")
print("Se ha(n) encontrado ",negativo, " numero(s) negativos")
print("Se ha(n) encontrado ",par, " numero(s) pares")
print("Se ha(n) encontrado ",impar, " numero(s) impares")


