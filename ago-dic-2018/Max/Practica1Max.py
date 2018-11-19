import math
N=int(input("Cantidad de numeros que deseas clasificar: "))
Pos = 0
Neg = 0
Par = 0
Impar = 0
lista = [] #cree esta lista vacia para guardar los valores y poder ver mas tarde
for n in range(N):
    x= int(input("Dame un numero" , n, " :" ))
    lista.append(x)
    if x >= 0:
        Pos= Pos + 1
        if (x%2)== 0:
            Par= Par + 1
        else:
            Impar= Impar + 1
    else:
        Neg= Neg + 1
        if (x%2)== 0:
            Par= Par + 1
        else:
            Impar= Impar + 1
print("Numero(s) positivo(s) : ",  Pos)
print("Numero(s) Negativo(s) : ",  Neg)
print("Numero(s) Pare(s)     : ",  Par)
print("Numero(s) Impare(s)   : ",  Impar)
print("Numeros ingresados: ", lista)
