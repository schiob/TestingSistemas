import math
numero=int(input("ingrese total de numeros: "))
if numero>0:
    par=0
    impar=0
    negativo=0
    positivo=0

    for i in range(numero):

        ListaNumeros=int(input("Ingrese numero: "))
        if ListaNumeros % 2 == 0:
            par = par + 1
        else:
            impar = impar + 1
        if ListaNumeros > 0:
            positivo += 1
        elif ListaNumeros < 0:
            negativo += 1


print(positivo, " " , "numero(s) positivo(s)")
print(negativo, " " , "numero(s) negativo(s)")
print(par, " ",  "numero(s)  par(es)")
print(impar, " ",  "numero(s) impar(es)")
