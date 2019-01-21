def sumarNumerosImpares(numImpar):

    suma = 0
    lista =[int(i) for i in numImpar.split()]
    

    if lista[0] > lista[1]:
        x = lista[1]
        y = lista[0]
    else:
        x = lista[0]
        y = lista[1]

    x += 1
    for i in range(x,y):
         if i % 2:
            suma += i
    return suma

if __name__ == '__main__':
    numImpar = (input("Ingresa los números que deseas, separados por la tecla space: "))
    suma = sumarNumerosImpares(numImpar)
    print("Suma de Números Impares: {}".format(suma))