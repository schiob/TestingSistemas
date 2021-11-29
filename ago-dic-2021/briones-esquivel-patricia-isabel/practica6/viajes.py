class Practica_viajes():
    def __init__(self) -> None:
        self.lista_usuarios = [
            [4, 'Tom'],
            [2, 'Mario'],
            [10, 'Andres'],
            [3, 'Pepe'],
            [2, 'Luis'],
        ]

        self.lista_conductores = []

        self.lista_viajes_disponibles = []

    def extraer_conductores(self) -> list:
        lc = [
            ['Juan', 3],
            ['Jesus', 2],
            ['Maria', 3],
            ['Pedro', 1],
        ]
        return lc


    def calcular_tarifa(self, nombre_conductor: str) -> int:
        self.lista_conductores = self.extraer_conductores()
        antiguedad = 0
        for i in range (len(self.lista_conductores)):
            if nombre_conductor in self.lista_conductores[i][0]:
                antiguedad = self.lista_conductores[i][1]

        tarifa = 20 + (10 * antiguedad)
        return tarifa

    def viajes_disponibles(self):
        self.lista_conductores = self.extraer_conductores()
        lvd = []
        j = 0
        for i in range(len(self.lista_conductores)):
            j = self.calcular_tarifa(self.lista_conductores[i][0])
            lvd.append([i+1,j])
        return lvd


    def siguiente_usuario(self):
        self.lista_usuarios.sort(reverse = True)
        cont = 0
        for i in range(len(self.lista_usuarios)):
            cont += 1

        if cont > 0:
            sig_user = self.lista_usuarios[len(self.lista_usuarios)-1][1]
            self.lista_usuarios.pop()
            return sig_user
        else: 
            return 'No hay más usuarios'


    def clase_principal(self):
        tarifa_minima = []
        viajes = []
        self.lista_viajes_disponibles = self.viajes_disponibles()
        for i in range(len(self.lista_viajes_disponibles)):
            tarifa_minima.append([self.lista_viajes_disponibles[i][1],self.lista_viajes_disponibles[i][0]])
        tarifa_minima.sort()

        for i in range(len(self.lista_viajes_disponibles)):
            viajes.append(self.siguiente_usuario() + ' - viaje ' + str(tarifa_minima[i][1]))
        
        return viajes


if __name__ == "__main__":
    archivito = Practica_viajes()
    print(archivito.extraer_conductores())
    print(archivito.calcular_tarifa('Maria'))
    print(archivito.viajes_disponibles())
    #print(archivito.siguiente_usuario())
    print(archivito.clase_principal())