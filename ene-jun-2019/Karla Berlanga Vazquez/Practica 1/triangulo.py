def clasificacion(lados):
    #Pedimos los lados del triangulo en un string separado por espacios
    #lados=input("Escribe las medidas de los lados de un triangulo ")
    #filtramos el string con la funcion split que nos devuelve una lista con los lados
    try:
        lista = list(map(int, lados.split())) #convetimos la lista string a int
        pass
    except ValueError:
        return ("Entrada de datos inválida")


    #Primera validación: que ningún lado sea cero, si alguno es cero termina el programa
    for i in range(3):
        if lista[i] == 0:
            return ("Los lados no forman un triángulo")
            #print("Los lados no forman un triángulo")
            exit()

    #Segunda validación: Revisamos la desigualdad triangular, es decir
    #que los lados formen un triángulo
    lista.sort() #ordenamos la lista para saber cuál lado es mayor
    #print(lista)
    if lista[0] + lista[1] <= lista[2]:
        return ("Los lados no forman un triángulo")
        #print("Los lados no forman un triángulo")
    else: #Tercera validacion: Clasificación de triángulos - ¿Equilátero? ¿Escaleno? ¿Isósceles?
        for elemento in lista:
            if lista.count(elemento) == 3:
                return ("Triangulo Equilátero")
                #print("Triangulo Equilátero")
                exit()
            elif lista.count(elemento) == 2:
                return ("Triangulo Isósceles")
                #print("Triangulo Isósceles")
                exit()
            else:
                return ("Triangulo Escaleno")
                #print("Triangulo Escaleno")
                exit()
