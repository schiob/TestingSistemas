def contador(linea):
    #checa que no haya str en la linea de entrada
    if not isinstance(str(linea).split(" "), int):
        return "No es el tipo de dato pedido"
    #convertimos la lista en arreglo para facilitar manejo
    datos = str(linea).split(" ")
    #checa que el arreglo contenga solo 5 datos
    if len(datos) > 5 or len(datos) < 5:
        return "No es la cantidad de datos pedidos"
    
    positivos = negativos = pares = impares = 0
    
    for x in datos:
        if x % 2 == 0:
            pares = pares + 1
        else:
            impares = impares + 1
        if x < 0:
            negativos = negativos + 1
        else:
            positivos = positivos + 1

    print( positivos, "número(s) positivo(s) \n", negativos, "número(s) negativo(s) \n", pares, "número(s) par(s) \n", impares, "número(s) impar(s) \n")

#linea = input("Introdusca los 5 valores: ").split(" ")
 