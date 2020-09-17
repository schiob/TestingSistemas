# Retornará un diccionario con las marcas de pantalones como llave y un número que indicará un contador el cual iniciará en 0 pues hasta el momento la venta inicia en 0.
# Este diccionario será clave para saber si el pantalón puede o no venderse en caso de que ya sólo quede un pantalón en la lista de la misma marca.
def obtener_pantalones_vendidos(lista_pantalones):
    pantalones_vendidos = {}
    for pantalon in lista_pantalones:
        pantalon = pantalon.split(' ')[0]
        pantalones_vendidos[pantalon] = 0
    return pantalones_vendidos

# Retornará un diccionario con las marcas de pantalones como llave y un número que indicará el total de veces que la marca se repite en la lista de pantalones.
# Este diccionario será clave para saber si el pantalón puede o no venderse en caso de que ya sólo quede un pantalón en la lista de la misma marca.
def obtener_pantalones_repetidos(lista_pantalones):
    pantalones_repetidos = {}
    for pantalon_principal in lista_pantalones:
        pantalon_principal = pantalon_principal.split(' ')[0]
        repetidos = 0
        for pantalon_secundario in lista_pantalones:
            pantalon_secundario = pantalon_secundario.split(' ')[0]
            if pantalon_principal == pantalon_secundario:
                repetidos = repetidos + 1
        pantalones_repetidos[pantalon_principal] = repetidos
    return pantalones_repetidos

# Función que venderá pantalones y retornará el total de pantalones vendidos y su ganancias dadas las siguientes reglas del cliente:
# Quiere disminuir la cantidad de pantalones de N a X
# No quiere dejar su ropero sin pantalones de una marca que ya tenía, (si tenía 2 pantalones de la marca Levice, se quiere quedar por lo menos con 1)
# Quiere vender primero los pantalones más caros.
# Y vender como máximo 5 pantalones de cada marca.
def vender_pantalones(lista_pantalones, x, n):
    diccionario_pantalones_repetidos = obtener_pantalones_repetidos(lista_pantalones)
    diccionario_pantalones_vendidos = obtener_pantalones_vendidos(lista_pantalones)
    total_ganancia = 0
    total_pantalones_vendidos = 0

    for pantalon in lista_pantalones:
        # Si ya se vendió la cantidad máxima permitida que el cliente desea vender entonces se parará el ciclo.
        if total_pantalones_vendidos == x-n:
            break
        # Obtengo las variables para que sea más entendible el código.
        pantalon = pantalon.split(' ')
        marca_pantalon = pantalon[0]
        precio_pantalon = pantalon[1]
        # Si la cantidad de pantalones vendidos es menor que la cantidad de pantalones repetidos se podrán sumar sus ganancias
        # y se le sumará al total de pantalones vendidos 1. De lo contrario significa que ya sólo queda un pantalón
        # por lo tanto no debe permitirse que se venda.
        if diccionario_pantalones_vendidos[marca_pantalon] < diccionario_pantalones_repetidos[marca_pantalon]-1:
            diccionario_pantalones_vendidos[marca_pantalon] = diccionario_pantalones_vendidos[marca_pantalon] + 1
            total_ganancia = total_ganancia + int(precio_pantalon)
            total_pantalones_vendidos = total_pantalones_vendidos + 1
        # Se están intentando vender más de 5 pantalones, lo cual no está permitido.
        elif diccionario_pantalones_vendidos[marca_pantalon] >= 5:
            return "0"
    if total_pantalones_vendidos != x-n:
        return "0"
    return '{} {}'.format(total_pantalones_vendidos, total_ganancia)

# Descomentar esto para hacer una prueba real, a mí me daba pereza escribir los valores así que lo dejé ordenado al final
# pero el resultado es el mismo.
# Entrada principal del programa.
#numero_pantalones = input("¿Cuántos pantalones tienes y cuántos deseas vender? \n").split(' ')
#n = int(numero_pantalones[0])
#x = int(numero_pantalones[1])

# Se guarda la información de cada pantalón en una lista dado un número total de pantalones como tamaño de la lista.
#lista_pantalones = list()
#for i in range(0, n):
#    pantalon = input("Ingresa la marca y el precio [{}:{}]\n".format(i+1,n))
#    lista_pantalones.append(pantalon)

# Se ordenan los pantalones basados en su precio del mayor al menor.
#lista_pantalones_ordenada = sorted(lista_pantalones, key= lambda pantalon: (int(pantalon.split(' ')[1])), reverse=True)
lista_pantalones_ordenada = ['Nike 20', 'Nike 18', 'Levice 15', 'Patito 5', 'Patito 5', 'Patito 4', 'Levice 4', 'Levice 3']
n = 8
x = 5
print(vender_pantalones(lista_pantalones_ordenada, n , x))