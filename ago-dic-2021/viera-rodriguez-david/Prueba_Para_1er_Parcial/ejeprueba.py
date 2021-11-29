def lectura_tabla(cantnums,numeros):
    pos = 0
    neg = 0 
    par = 0
    impar = 0

#Convierte a una lista
    numeros = list(map(int,numeros.split()))
    i = 0
    while i<cantnums:
        if numeros[i]>0:
            pos +=1
        elif numeros[i]<0:
            neg+=1
        if (numeros[i]%2) == 0:
            par+=1
        else:
            impar+=1
        i+=1
    a=(str(pos)+" Numero(s) Positivo(s)\n"+str(neg)+" Numero(s) Negativo(s)\n"+str(par)+" Numero(s) Par(es)\n"+str(impar)+" Numero(s) Impar(es)\n")
    print (a)
    return a
if __name__ == '__main__':
    lectura_tabla(6,"5 4 9 8 3 1")




