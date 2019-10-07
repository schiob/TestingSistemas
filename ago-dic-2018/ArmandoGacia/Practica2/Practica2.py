def calcu(tam):
    impar=0
    par=0
    posi=0
    nega=0
    for num in tam:
        if num % 2:
            impar+=1
        else:
            par+=1
        if num < 0:
            nega+=1
        else:
            posi+=1
    return impar, par, nega, posi

if __name__ == '__main__':
    n=int(input('Dame el total de numeros a evaluar: '))
    tam=list(map(int,input('Dame los números a evaluar (separados por espacio):').split(" ")))
    gg=calcu(tam)
    #tam = int(input('Dame el total de numeros a evaluar: '))
    #ent=input('Dame los números a evaluar (separados por espacio): ')
    #lista = []
    #lista=[int(tam) for tam in ent.split(" ")]

    print("Numero(s) Par = {}".format(gg[1]))
    print("Numero(s) Impar = {}".format(gg[0]))
    print("Numero(s) Negativos = {}".format([2]))
    print("Numero(s) Positivos = {}".format([3]))
