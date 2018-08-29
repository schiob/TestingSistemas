import math
import random
N = int(input("Numeros que deseas clasificar: "))
Pos = 0
Neg = 0
Par = 0
Impar = 0
lista = [] #cree esta lista vacia para guardar los valores random y poder ver lo que me dio mas tarde
for n in N():
    x = randrange(-10,11)
    lista.append(x)
    if x >= 0:
        Pos = Pos + 1
        if (x % 2) == 0: #me marca un error de sintaxis en esta parte, solo me marca que el erro esta en el "0"
            Par = Par + 1 #ya use =0.0, ==0.0, (x%2) == 0 pero aun asi me marca ese error
        else:
            Impar = Impar + 1
    else:
        Neg = Neg + 1
        if (x % 2) == 0:
            Par = Par + 1
        else:
            Impar = Impar + 1
print("Numeros positivos: ",  Pos)
print("Numeros positivos: ",  Neg)
print("Numeros positivos: ",  Par)
print("Numeros positivos: ",  Impar)
print(lista)
