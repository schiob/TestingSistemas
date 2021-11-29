class uber:
    cliente = {
            'Tom': 4,
            'Susana': 2,
            'Andres': 10,
            'Pepe': 3,
            'Luis': 2
        }
    cont = len(cliente)
    viajes = {}
######Funcion Principal#####
    def funcion_principal(self):
        viaje = self.viajes_disponibles()
        cadena = ''

        for i in range(self.cont-1):
            cliente = self.siguiente_usuario()
            viaje_id = min(viaje, key=viaje.get)
            if i == len(cliente):
                cadena += str(f'Usuario: {cliente}, ID del viaje: {viaje_id}')
            elif i < len(cliente):
                cadena += str(f'Usuario: {cliente}, ID del viaje: {viaje_id}\n')

            del viaje[viaje_id]
        return cadena.split('\n')
####2da Funcion####
    def siguiente_usuario(self):
        min_value = min(self.cliente, key=self.cliente.get)
        self.cliente.pop(min_value)

        return min_value

####3ra Funcion####
    def viajes_disponibles(self):
        y = 1
        for x in range(len(self.calcular_tarifa())):
            tarifa = self.calcular_tarifa()
            self.viajes[y] = tarifa[x]
            y += 1
        return self.viajes
####4ta Funcion####
    def extraer_conductores(self):
        archivo = open(
            'conductores2.txt', 'r')
        contenido = archivo.read().split()
        archivo.close()
        print(contenido)
        return contenido
####5ta Funcion####
    def calcular_tarifa(self):
        tarifa = []
        cuota = []
        antiguedad = self.extraer_conductores()
        for x in range(len(antiguedad)):
            if x % 2 != 0:
                tarifa.append(antiguedad[x])
        tarifas_int = list(map(int, tarifa))

        for i in range(len(tarifas_int)):
            cuota.append(20 + (10 * tarifas_int[i]))
        return cuota

if __name__ == '__main__':
    cliente = uber()
    cliente.principal()