listmarcas = []
listprecios = []
n = int(input("Dame el numero de pantalones en el ropero: "))
x = int(input("Dame el numero de pantalones al que deseas llegar: "))

for i in range(n):
    listmarcas.append(input("marca del pantalon: "))
    listprecios.append(int(input("precio del pantalon: ")))

for i in range(n):
    print(listmarcas[i],listprecios[i])

marcas = {}

for i in range(n):
    if listmarcas[i] in marcas:
        marcas[listmarcas[i]] += 1
    else:
        marcas[listmarcas[i]] = 1

print(marcas)

nombremarcas = list(marcas.keys())

numeromarca = list(marcas.values())

print(nombremarcas,numeromarca)

for i in range(n):
    for j in range(n):
        if listprecios[i] > listprecios[j]:
            marcas = listmarcas[i]
            listmarcas[i] = listmarcas[j]
            listmarcas[j] = marcas
            precios = listprecios[i]
            listprecios[i] = listprecios[j]
            listprecios[j] = precios

for i in range(n):
    print(listmarcas[i],listprecios[i])

vent_total = int()

#for i in range(n):
#    if listmarcas[i] in marcas:
#        if n > x:
#            vent_total = listprecios[i]
            #marcas[listmarcas[i]] -= 1
#            del listmarcas[i]
#            del listprecios[i]
#            n -= 1
#            i -= 1

listmarcasvend = []
listpreciosvent = []

while i < len(nombremarcas):
    if n > x:
        for j in range(n):
            if nombremarcas[j] == listmarcas[i]:
                if numeromarca[i] > 1:
                    listmarcasvend[j] = listmarcas[j]
                    listpreciosvent[j]  = listprecios[j]
                    vent_total = listprecios[j]
                    del listmarcas[j]
                    del listprecios[j]
                    j -= 1
                    n -= 1

for i in range(len(listmarcasvend)):
    print(listmarcasvend[i],listpreciosvent[i])

print(marcas)

for i in range(n):
    print(listmarcas[i],listprecios[i])

print(vent_total)
