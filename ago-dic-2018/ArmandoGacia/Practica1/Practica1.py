tam = int(input('Dame el total de nuemros a evaluar: '))
lista = []
impar = 0
par = 0
nega = 0
posi = 0
ent=input('Dame los números a evaluar (separados por espacio): ')
lista=[int(tam) for tam in ent.split(" ")]
for i in range(0,tam):
    num=lista[i]
    if num % 2:
        impar= impar+1
    else:
         par = par+1
    if num < 0:
        nega = nega+1
    else:
          posi = posi+1

print(str(par) + " Numero(s) Par")
print(str(impar) + " Numero(s) Impar")
print(str(nega) + " Numero(s) Negativos")
print(str(posi) + " Numero(s) Positivos")
print(lista)
