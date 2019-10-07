positivos,negativos,par,impar,ceros= 0,0,0,0,0

cantidad = int(input("Camtidad de numeros a ingresar: "))
lista = list(map(int, input().split(' ')))#El metodo split genera una lista a partir de los datos ingresasados separados por un espacio
#Aunque se pueden ingresar mas numeros, solo se tomaran en cuenta la cantidad ingresada
#debido a que el for solo toma en cuenta la cantidad que se le dio sin importar que en el arreglo esten mas valores
print(lista)

for x in range(0,cantidad):
        if (lista[x]>0):
            positivos=positivos+1
            pass
        if(lista[x]<0):
            negativos=negativos+1
            pass
        if (lista[x]==0):
            ceros=ceros+1
            pass
        if (lista[x]!=0 and lista[x]%2==0):
            par=par+1
            pass
        if (lista[x]%2!=0):
            impar=impar+1

print("Positivos: "+str(positivos))
print("Negativos: "+str(negativos))
print("Pares: "+str(par))
print("Impares: "+str(impar))
print("Ceros: "+str(ceros))
