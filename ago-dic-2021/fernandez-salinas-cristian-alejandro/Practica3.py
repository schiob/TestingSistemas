from unittest import result


def contarNumeros(n,numeros):
    numeros = list(map(int,numeros.split()))
    positivos = 0
    negativos = 0
    pares = 0
    impares = 0

    for i in range(len(numeros)):

        if numeros[i] > 0:
            positivos += 1
        elif numeros[i] < 0:
            negativos += 1

        if (numeros[i] % 2) == 0:
            pares += 1
        else:
            impares += 1

    resultado = "{} número(s) positivo(s)\n{} número(s) negativo(s)\n{} número(s) par(es)\n{} número(s) impar(es)".format(positivos,negativos,pares,impares)
    print(resultado)
    return resultado
        

if __name__ == '__main__':
    contarNumeros(5,"51 -12 -3 0 2")