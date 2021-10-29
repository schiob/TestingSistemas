class Uber:
    usuario = {
            'Tom': 4,
            'Susana': 2,
            'Andres': 10,
            'Pepe': 3,
            'Luis': 2
        }
    cont = len(usuario)
    viajes = {}

    def siguiente_usuario(self):
        min_value = min(self.usuario, key=self.usuario.get)
        self.usuario.pop(min_value)

        return min_value


    def viajes_disponibles(self):
        y = 1
        for x in range(len(self.calcular_tarifa())):
            tarifa = self.calcular_tarifa()
            self.viajes[y] = tarifa[x]
            y += 1
        print(self.viajes)


    def extraer_conductores(self):
        archivo = open(
            'ago-dic-2021\JESUS SALVADOR DE LA CRUZ DAVILA\PRACTICA_6\conductores.txt', 'r')
        contenido = archivo.read().split()
        archivo.close()
        return contenido


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
        # cuota.sort(reverse=True)
        return cuota

    def principal(self):
        viaje = self.viajes_disponibles()
        cadena = ''

        for i in range(self.cont-1):
            usuario = self.siguiente_usuario()
            viaje_id = min(viaje, key=viaje.get)
            if i == len(usuario):
                cadena += str(f'Usuario: {usuario} ID del viaje: {viaje_id}')
            elif i < len(usuario):
                cadena += str(f'Usuario: {usuario} ID del viaje: {viaje_id}\n')

            del viaje[viaje_id]

        return(print(cadena))





if __name__ == '__main__':
    usuario = Uber()
    usuario.viajes_disponibles()



# extraer_conductores()
# print()
# siguiente_usuario()
# calcular_tarifa()
# viajes_disponibles()
# main()