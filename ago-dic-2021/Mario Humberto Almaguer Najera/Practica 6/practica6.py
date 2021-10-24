class Practica6:

    # Crear nuestro constructor
    def __init__(self) -> None:
        # Inicializar diccionarios usuarios y viajes, ademas de inicializar la lista nombres
        self.usuarios = {'Tom': 4, 'Susana': 2,
                         'Andres': 10, 'Pepe': 3, 'Luis': 2}
        self.conductores = {'Juan': 3, 'Jesus': 2,
                            'Maria': 3, 'Tono': 1, 'Pedro': 4}
        self.viajes = {}
        self.resultados = []

    def funcion_principal(self, numero_viajes):
        # Repetimos numero_viajes, y agregamos a la lista el siguiente_usuario (el de mayor prioridad) con
        # el siguiente_viaje (el de menor tarifa)
        for i in range(numero_viajes):
            # Se hace un append a la lista resultados
            self.resultados.append('Usuario: ' + str(self.siguiente_usuario()) +
                                   ' | Viaje: ' + str(self.siguiente_viaje()))
        # Regresar una lista con los resultados finales
        return self.resultados

    def viajes_disponibles(self, numero_viajes: int):
        # Inicializamos id_viaje = 1
        id_viaje = 1
        # Generar un diccionario con id_viaje incrementando 1 en 1 (keys), y tarifa calculada (values)
        for i in range(numero_viajes):
            # Se usa obtener_agnos_trabajando()[1] porque nos regresa una lista con su nombre, agnos
            # y lo que nos importa son los agnos, por eso [1]
            agnos_trabajando = self.obtener_agnos_trabajando()[1]
            self.viajes[id_viaje] = self.calcular_tarifa(agnos_trabajando)
            id_viaje += 1
        # Regresar un diccionario con id_viaje : tarifa
        return self.viajes

    def siguiente_usuario(self):
        # Guardamos nuestro usuario con mas alta priorida en sig_usuario
        sig_usuario = min(self.usuarios, key=self.usuarios.get)
        # Eliminamos a sig_usuario del diccionario, por si hay dobles con la misma prioridad
        del self.usuarios[sig_usuario]
        # Regresamos el sig_usuario
        return sig_usuario

    def siguiente_viaje(self):
        # Guardamos nuestro viaje con mas baja tarifa
        sig_viaje = min(self.viajes, key=self.viajes.get)
        # Eliminamos a sig_viaje del diccionario
        del self.viajes[sig_viaje]
        # Regresamos el sig_viaje
        return sig_viaje

    def obtener_agnos_trabajando(self):
        # Obtenemos el conductor con menor agnos trabajando(key y value)
        sig_conductor_key_value = min(
            self.conductores.items(), key=lambda k: k[1])
        # Borramos al conductor encontrado del diccionario
        del self.conductores[sig_conductor_key_value[0]]
        # Regresamos el nombre y numero de agnos del conductor con menor agnos trabajando
        return sig_conductor_key_value

    def calcular_tarifa(self, agnos: int):
        # Regresamos la tarifa con la formula de Github
        return 20 + (10 * agnos)


if __name__ == '__main__':
    practica = Practica6()
    numero_viajes = 5
    print('\nUsuarios: ', practica.usuarios)
    print('\nConductores: ', practica.conductores)
    print('\nViajes:', practica.viajes_disponibles(numero_viajes))
    print('\nResultados:', practica.funcion_principal(numero_viajes))
