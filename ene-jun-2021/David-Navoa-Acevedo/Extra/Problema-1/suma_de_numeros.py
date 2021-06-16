
def suma_de_impares(numeros):
    if range(numeros == 2):
        inicio = min(numeros[0], numeros[1])
        fin = max(numeros[0], numeros[1])
        lista = range(inicio + 1, fin)
        suma = 0
        for numero in lista:
            if numero % 2 != 0:
                suma += numero
        return suma
    return "Dame 2 numeros ni mas ni menos compadre"
