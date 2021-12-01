viajesList = {}
usuariosList = {'Tom':    4, 'Susan': 2, 'Andres':10, 'Pepe':   3, 'Luis':   2}

class Viajes:
    def siguiente_usuario():
        usuario = min(usuariosList, key=usuariosList.get)
        usuariosList.pop(usuario)
        return usuario

    def extraer_conductores():
        conductoresTXT = {'Juan' :  3, 'Jesus': 2, 'Maria': 3, 'Toño' : 1}
        return conductoresTXT

    def calc_tarifa():
        tarifa = []
        cuota = []
        antiguedad = Viajes().extraer_conductores()
        for x in range(len(antiguedad)):
            if x % 2 != 0:
                tarifa.append(antiguedad[x])
        antiguedad2 = list(map(int, tarifa))

        for i in range(len(antiguedad2)):
            cuota.append(20 + (10 * antiguedad2[i]))
        return cuota


    def viajes_disp():
        y = 1
        for x in Viajes().extraer_conductores():
            tarifa2 = Viajes().calc_tarifa()
            viajesList[y] = tarifa2[x]
            y = y + 1
        return viajesList

    xyz = len(usuariosList)
    def calcular():
        xyz = len(usuariosList)
        viaje2 = Viajes().viajes_disp()
        for x in range(xyz-1):
            usuario = Viajes().siguiente_usuario()
            numViaje = min(viaje2, key=viaje2.get)
            print(f'Datos: \nUsuario: ' + usuario + '\nNumero de Viaje: ' + {numViaje})

if __name__ == '__main__':
    Viajes().calcular()