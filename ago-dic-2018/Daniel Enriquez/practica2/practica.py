
def contar(numbers):
    pares=impares=negativos=positivos=0
    for num in numbers :
        if num % 2 == 0:
            pares+=1
        else:
            impares+=1
        if num< 0:
                negativos +=1
        elif num>0:
                positivos+=1
    return pares, impares, negativos,positivos

if __name__ == '__main__':

    n = int(input())
    numbers = lis(map(int, input().split(' ')))

    resultado=contar(numeros)

    print("pares = {}".format(resultado[0]))
    print("impares = {}".format(resultado[1]))
    print("negativo = {}".format(resultado[2]))
    print("positivos = {}".format(resultado[3]))
