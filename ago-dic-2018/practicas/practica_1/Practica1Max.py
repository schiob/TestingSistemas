import math
N= int(input("Numeros que deseas clasificar: "))
Pos= 0
Neg= 0
Par= 0
Impar= 0
lista= [] #cree esta lista vacia para guardar los valores random y poder ver lo que me dio mas tarde
for n in (0, N):
    x = int(input('Dame un valor: ')))
    lista.append(x)
    if x>= 0:
        Pos= Pos + 1
        if (x % 2) == 0:
            Par= Par + 1 
        else:
            Impar= Impar + 1
    else:
        Neg= Neg + 1
        if (x%2)== 0:
            Par= Par + 1
        else:
            Impar= Impar + 1
print("Numeros positivos: ",  Pos)
print("Numeros Negativos: ",  Neg)
print("Numeros Pares: ",  Par)
print("Numeros Impares: ",  Impar)
print(lista)
