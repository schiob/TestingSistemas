class viajes():

    def __init__(self, users):
        self.users = users

    def siguiente_usuario(self):

        usuarios = self.users
        clmenor = usuarios[0]
        menor = int(usuarios[0][1])

        for i, j in usuarios:
            if int(j) <= menor:
                menor = int(j)
                clmenor = i
                men = [clmenor, str(menor)]

        usuarios.remove(men)
        return clmenor

    def viajes_disponibles(self):
        num = 0
        viajes1 = []
        viaje = []

        for x in range(len(self.extraer_conductores())):

            anti = int(self.extraer_conductores()[x][1])
            tarifa = self.calcular_tarifa(anti)
            num = num + 1
            viajes1.append([num, tarifa])

        return viajes1

    def extraer_conductores(self):
        conductores = []
        fname = open("ago-dic-2021\Javier Eduardo Aleman Ortiz\Conductores.txt")
        for lineas in fname:
            conductores.append(lineas.split())

        return(conductores)

    def calcular_tarifa(self, antiguedad):
        self.antiguedad = antiguedad
        return 20 + (10*antiguedad)

    def funcion_Principal(self, viajes):
        clPio = self.siguiente_usuario()

        tarMen = (self.viajes_disponibles()[0][1])
        viajDisp = self.viajes_disponibles()[0][0]
        for x, y in viajes:
            if int(y) <= (tarMen):
                tarMen = int(y)
                viajDisp = x
        viajes.remove([viajDisp, tarMen])
        return(f'El cliente: {clPio} se va en el viaje {viajDisp}')


if __name__ == '__main__':

    usuarios = []
    users = open("ago-dic-2021\Javier Eduardo Aleman Ortiz\Clientes.txt")
    for linea in users:
        usuarios.append(linea.split())

    objeto = viajes(usuarios)

    viaje = objeto.viajes_disponibles()
    for x in range(len(objeto.viajes_disponibles())):
        print(objeto.funcion_Principal(viaje))