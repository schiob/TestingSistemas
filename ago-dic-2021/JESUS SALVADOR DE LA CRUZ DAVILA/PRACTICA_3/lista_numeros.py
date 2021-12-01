def lista_de_numeros(numeros):
    positivos = 0
    negativos = 0
    pares = 0
    impares = 0
    
    for n in numeros:
        if n > 0:
            positivos += 1
        elif n < 0:
            negativos += 1
        if n % 2 == 0:
            pares +=1
        elif n % 2 == 1:
            impares += 1
    return f'numero(s) positivo(s): {positivos}\nnumero(s) negativo(s): {negativos}\nnumero(s) par(es): {pares}\nnumero(s) impar(es): {impares}'

if __name__ == '__main__':
    list = []
    numero = int(input("Ingresa la cantidad de numeros que deseas registrar: "))
    for n in range(numero):
        n += 1
        n = int(input(f'Ingrese el numero {n}: '))
        list.append(n)
    
    print(lista_de_numeros(list))
        


