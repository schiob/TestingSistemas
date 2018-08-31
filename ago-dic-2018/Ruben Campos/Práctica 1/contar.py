import sys
positivos = 0
negativos = 0
impares = 0
pares = 0
n = int(input('Elije la cantidad de numeros que tendrá la lista: '))
numeros = [int(x) for x in input("Teclea {} numero(s) aquí (sepáralos con espacios): ".format(n)).split()]
if len(numeros) != n:
    print("Error, tienes que teclear {} numero(s) para proceder".format(n))
    raise SystemExit
for x in numeros:
    if x > 0:
        positivos+=1
    elif x < 0:
        negativos+=1
    if x % 2:
        impares+=1
    else:
        pares+=1
print('{} numero(s) positivo(s)'.format(positivos))
print('{} numero(s) negativos(s)'.format(negativos))
print('{} numero(s) par(es)'.format(pares))
print('{} numero(s) impar(es)'.format(impares))
