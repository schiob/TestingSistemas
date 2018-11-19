def calcular(numero):
    par = impar = negativo = positivo = 0

    for num in numero:

        if num % 2 == 0:
            par = par + 1
        else:
            impar = impar + 1
        if num > 0:
            positivo += 1
        elif num < 0:
            negativo += 1
    return par,impar,positivo,negativo

if __name__ == '__main__':
    numero=int(input("ingrese total de numeros: "))
    ListaNumeros=list(map(int,input().split(" ")))
    resultado=calcular(ListaNumeros)
    print("par = {}".format(resultado[0]))
    print("impar = {}".format(resultado[1]))
    print("positivo = {}".format(resultado[2]))
    print("negativo = {}".format(resultado[3]))
