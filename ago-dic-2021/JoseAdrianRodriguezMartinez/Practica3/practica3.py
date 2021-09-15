
def numeros_lista(cantidad, numeros):
    int_numeros = numeros.split(' ')
    return int_numeros        

if __name__ == '__main__':
    cantidad = int(input('Cantidad de numeros: '))
    numeros = str(input('Numeros separados por espacio: '))
    print(numeros_lista(cantidad, numeros))