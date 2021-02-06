def contador(linea):
    if len(linea) > 5:
        print("Son mas de 5 valores")
        return

    positivos = negativos = pares = impares = 0
    
    for x in linea:
        if int(x) % 2 == 0:
            pares = pares + 1
        else:
            impares = impares + 1
        if int(x) < 0:
            negativos = negativos + 1
        else:
            positivos = positivos + 1
    print( positivos, "número(s) positivo(s) \n", negativos, "número(s) negativo(s) \n", pares, "número(s) par(s) \n", impares, "número(s) impar(s) \n")
    return

linea = input("Introdusca los 5 valores: ").split(" ")
contador(linea)

