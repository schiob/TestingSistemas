
def crear_lista(cantidad_numeros: int):
    lista_numeros = []
    temp = 0
    for i in range(cantidad_numeros):
        temp = int(input('Número a insertar: '))
        lista_numeros.append(temp)

    return lista_numeros

def positivos(numeros_lista):
    positivos = 0
    for i in numeros_lista:    
        if i > 0:
            positivos += 1

    return positivos
        
def negativos(numeros_lista):
    negativos = 0
    for i in numeros_lista:
        if i < 0:
            negativos += 1

    return negativos

def pares(numeros_lista):
    pares = 0
    for i in numeros_lista:
        if i % 2 == 0:
            pares += 1

    return pares

def impares(numeros_lista):
    impares = 0
    for i in numeros_lista:
        if i %  2 != 0:
            impares += 1

    return impares


if __name__ == '__main__':
    cantidad = int(input('Cantidad de numeros: '))
    lista = crear_lista(cantidad)
    print(lista)
    print(f"Número(s) positivos: {positivos(lista)}")
    print(f"Número(s) negativos: {negativos(lista)}")
    print(f"Número(s) pares: {pares(lista)}")
    print(f"Número(s) impares: {impares(lista)}")
