conteoImpar = 0
conteoPar = 0
conteoPositivos = 0
conteoNegativos = 0

n = int(input("Cantidad de numeros en la lista: "))
lista=[int(i) for i in (input("Ingresa los numeros: ").split(' '))]

for i in lista[:n]:
    if i % 2:
        conteoImpar = conteoImpar + 1
    else:
        conteoPar = conteoPar + 1

for i in lista[:n]:
    if i==0:
        i=i+1
    else:
        if i>0 and i != 0:
            conteoPositivos = conteoPositivos + 1
        else:
            conteoNegativos = conteoNegativos + 1

print("%d número(s) positivo(s)" % conteoPositivos)
print("%d número(s) negativo(s)" % conteoNegativos)
print("%d número(s) par(es)" % conteoPar)
print("%d número(s) impar(es)" % conteoImpar)
