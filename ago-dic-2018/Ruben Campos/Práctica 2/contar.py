def funcionpro(n, numeros):
    positivos = negativos = impares = pares = 0
    if len(numeros) != n:
        raise SystemExit("Error, tienes que teclear {} numero(s) para proceder".format(n))
    for x in numeros:
        if x > 0:
            positivos+=1
        elif x < 0:
            negativos+=1
        if x % 2:
            impares+=1
        else:
            pares+=1
    return positivos, negativos, pares, impares, n

if __name__ == '__main__':
    n = int(input('Elije la cantidad de numeros que tendrá la lista: '))
    numeros = [int(x) for x in input("Teclea {} numero(s) aquí (sepáralos con espacios): ".format(n)).split()]
    resultado=funcionpro(n, numeros)
    print('{} numero(s) positivo(s)'.format(resultado[0]))
    print('{} numero(s) negativos(s)'.format(resultado[1]))
    print('{} numero(s) par(es)'.format(resultado[2]))
    print('{} numero(s) impar(es)'.format(resultado[3]))
