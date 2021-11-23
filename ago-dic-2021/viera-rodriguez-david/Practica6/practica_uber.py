cliente = {
        'Tom': 4,
        'Susana': 2,
        'Andres': 10,
        'Pepe': 3,
        'Luis': 2
    }
cont = len(cliente)
####Funcion Principal####
def funcion_principal():
    viaje = viajes_disponibles()

    for i in range(cont-1):
        cliente = siguiente_usuario()
        viaje_id = min(viaje, key=viaje.get)
        print(f'Usuario: {cliente} ID del viaje: {viaje_id}')

        del viaje[viaje_id]
####2da Funcion####
def siguiente_usuario():
    min_value = min(cliente, key=cliente.get)
    cliente.pop(min_value)

    return min_value

####3ra Funcion####
def viajes_disponibles():
    y = 1
    viajes = {}
    for x in range(len(calcular_tarifa())):
        tarifa = calcular_tarifa()
        viajes[y] = tarifa[x]
        y += 1
    return viajes

####4ta Funcion####
def extraer_conductores():
    file_conductor = open('conductores.txt','r')
    content = file_conductor.read().split()
    file_conductor.close()
    return content

####5ta Funcion####
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
    return cuota

if __name__ == '__main__':
    funcion_principal()
