"""Programa que lee una lista de números y los clasifica en positivos,
negativos, pares e impares"""

def clasificacion_numeros(lista_numeros):
    #num_elementos_lista = input()
    positivos = negativos = pares = impares = 0  # inicializamos variables
    list = lista_numeros.split() # separamos cada elemento del string
    for x in list:
        x = int(x)
        if x % 2 == 0:
            pares += 1    # sumamos números pares
        if x % 2 != 0:
            impares += 1   # sumamos números impares
        if x < 0:
            negativos += 1    # sumamos números negativos
        if x > 0:
            positivos += 1    # sumamos números positivos
    return """
    {} número(s) positivo(s)\n{} número(s) negativo(s)\n{} número(s) par(es)\n{} número(s) impar(es)
    """.format(positivos, negativos, pares, impares).strip()

if __name__ == '__main__':
    input_string = input()
    print(clasificacion_numeros(input_string))
