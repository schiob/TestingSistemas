import sys
#Se importa sys para manejar como se cierra el programa
n=int(input('Cuantos números tendrá la lista: '))
nli=input('Introduzca los números de la lista (separados por espacio): ')
lista=[int(n) for n in nli.split(" ")]
if (len(lista) != n):
    print('Error, vuelva a correr el programa e inserte la cantidad correcta')
    sys.exit()
else:
    print(lista)

Pares=int(0)
Impares=int(0)
Positivos=int(0)
Negativos=int(0)

i = 0

while(i < len(lista)):
    j = lista[i]

    if(j%2==0):
        Pares=Pares+1
    else:
        Impares=Impares+1

    if (j>0):
        Positivos=Positivos+1
    else:
        Negativos=Negativos+1

    i = i + 1

print("{} Número(s) positivo(s).".format(Positivos))
print("{} Número(s) negativo(s).".format(Negativos))
print("{} Número(s) par(es).".format(Pares))
print("{} Número(s) impar(es).".format(Impares))
