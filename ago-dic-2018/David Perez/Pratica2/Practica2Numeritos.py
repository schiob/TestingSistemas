import sys
#Se importa sys para manejar como se cierra el programa
def numeritos(n,nli):
    Pares = Impares = Negativos = Positivos = 0
    lista=nli
    if (len(lista) != n):
        print('Error, vuelva a correr el programa e inserte la cantidad correcta')
        sys.exit()
    else:
        print(lista)
        for n in lista:
            if n%2==0:
                Pares+=1
            else:
                Impares+=1
            if n<0:
                Negativos+=1
            elif n>0:
                Positivos+=1
    return Positivos,Negativos,Pares,Impares

if __name__ == '__main__':
    n=int(input('Cuantos números tendrá la lista: '))
    nli=list(map (int, input('Introduzca los números de la lista (separados por espacio): ').split(" ")))

    res=numeritos(n,nli)
    print("{} Número(s) positivo(s).".format(res[0]))
    print("{} Número(s) negativo(s).".format(res[1]))
    print("{} Número(s) par(es).".format(res[2]))
    print("{} Número(s) impar(es).".format(res[3]))
