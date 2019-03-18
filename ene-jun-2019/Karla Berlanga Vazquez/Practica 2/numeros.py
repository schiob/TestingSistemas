"""Funcion que requiere la cantidad de numeros de una lista y los numeros enteros de la lista separados por espacios.
Retorna la los numeros enteros clasificados por negativos, positivos, pares e impares """
#Pedimos la cantidad de elementos de la lista
#cantidad = input("Cantidad de numeros en la lista")
def clasificacion(num_enteros):
    #Revisamos que la entrada de datos sea correcta
    try:
        lista = list(map(int, num_enteros.split())) #convetimos la lista string a int
        pass
    except ValueError:
        return ("Entrada de datos inválida")

    resultados= [ #Se gurdan los resultados en una lista
    [i for i in lista if i > 0], #cuando los números son positivos
    [i for i in lista if i < 0], #Cuando los numeros son negativos
    [i for i in lista if i % 2 == 0], #Cuando los números son pares
    [i for i in lista if i % 2 != 0], #Cuando los numeros son impares
    [i for i in lista if i == 0] #Cuando los números son cero
    ]

    #Se retorna el string con los resultados
    return """
    {} número(s) positivo(s) \n{} número(s) negativo(s)\n{} número(s) par(es)\n{} número(s) impar(es)
    """.format(len(resultados[0]), len(resultados[1]), len(resultados[2]), len(resultados[3])).strip()
