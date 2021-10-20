usuario = {
        'Tom': 4,
        'Susana': 2,
        'Andres': 10,
        'Pepe': 3,
        'Luis': 2
    }
cont = len(usuario)

def siguiente_usuario():
    min_value = min(usuario, key=usuario.get)
    usuario.pop(min_value)

    return min_value


def viajes_disponibles():
    y = 1
    viajes = {}
    for x in range(len(calcular_tarifa())):
        tarifa = calcular_tarifa()
        viajes[y] = tarifa[x]
        y += 1
    return viajes


def extraer_conductores():
    archivo = open(
        'ago-dic-2021\JESUS SALVADOR DE LA CRUZ DAVILA\PRACTICA_6\conductores.txt', 'r')
    contenido = archivo.read().split()
    archivo.close()
    return contenido


def calcular_tarifa():
    tarifa = []
    cuota = []
    antiguedad = extraer_conductores()
    for x in range(len(antiguedad)):
        if x % 2 != 0:
            tarifa.append(antiguedad[x])
    tarifas_int = list(map(int, tarifa))

    for i in range(len(tarifas_int)):
        cuota.append(20 + (10 * tarifas_int[i]))
    # cuota.sort(reverse=True)
    return cuota

def principal():
    viaje = viajes_disponibles()

    for i in range(cont-1):
        usuario = siguiente_usuario()
        viaje_id = min(viaje, key=viaje.get)
        print(f'Usuario: {usuario} ID del viaje: {viaje_id}')

        del viaje[viaje_id]



if __name__ == '__main__':
    principal()



# extraer_conductores()
# print()
# siguiente_usuario()
# calcular_tarifa()
# viajes_disponibles()
# main()