def numerosxd(esperado):
    positivos = 0
    negativos = 0
    pares = 0
    impares = 0
    for i in esperado:
        if i > 0:
            positivos = positivos + 1
            if i % 2 == 0:
                pares = pares + 1
            else:
                impares = impares + 1
        elif i < 0:
            negativos = negativos + 1
            if i % 2 == 0:
                pares = pares + 1
            else:
                impares = impares + 1
        elif i == 0:
            pares = pares + 1

    return(f'{positivos} positivos, {negativos} negativos, {pares} pares, {impares} impares')

if __name__ == '__main__':
    num = int(input('Tamaño lista:'))
    esperado = []
    for i in range(num):
        i = int(input("Ingrese el numero:"))
        esperado.append(i)
        