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

        
print(positivo, " numeros positivos se han encontrado")
print(negativo, " numeros negativos se han encontrado")
print(par, " numeros pares se han encontrado")
print(impar, " numeros impares se han encontrado")
