import random

class Practica6:

    #Crear nuestro constructor
    def __init__(self) -> None:
        # Inicializar diccionarios usuarios y viajes, ademas de inicializar la lista nombres
        # self.usuarios = {}
        # self.conductores = {}
        self.usuarios = {'Tom' : 4, 'Susana' : 2, 'Andres' : 10, 'Pepe' : 3, 'Luis' : 2}
        self.conductores = {'Juan' : 3, 'Jesus' : 2, 'Maria' : 3, 'Tono' : 1, 'Pedro' : 4}
        self.viajes = {}
        self.resultados = []
        #Lista de posibles nombres que los usuarios y/o conductores pueden tomar
        self.nombres = ['Mario', 'Pepe', 'Angel', 'Joaquin', 'Jesus', 'Edson', 'Emilio', 'Eli', 'Francisco', 'Sergio', 
        'Erick', 'David', 'Liam', 'Noah', 'Oliver', 'William', 'James', 'Benjamin', 'Lucas', 'Henry', 'Alexander', 
        'Mason', 'Michael', 'Ethan', 'Mateo', 'Sebastian', 'Jack', 'Peter', 'Josh', 'Patricia', 'Luis', 'Gerardo', 'Carmen']
        print('Usuarios: \n', self.usuarios)
        print('\nConductores: \n', self.conductores)

    def funcion_principal(self, numero_usuarios):
        #Repetimos numero_usuarios, y agregamos a la lista el siguiente_usuario (el de mayor prioridad) con el siguiente_viaje (el de menor tarifa)
        for i in range(numero_usuarios):
            #Se hace un append a la lista resultados
            self.resultados.append('Usuario: ' + str(self.siguiente_usuario()) + ' | Viaje: ' + str(self.siguiente_viaje()))
        #DEBUG : Se imprimie la lista resultados
        print(self.resultados)

    def generar_diccionario_usuarios(self, numero_usuarios : int):
        #Generar un diccionario con nombres aleatorios (keys) y prioridad aleatorio (values)
        for nombre in random.sample(self.nombres, numero_usuarios):
            self.usuarios[nombre] = random.randint(1, numero_usuarios)
        #DEBUG : Imprimir nuestra lista usuarios
        # print(self.usuarios)

    def extraer_conductores(self, numero_conductores : int):
        #Generar un diccionario con nombres aleatorios (keys) y agnos de antiguedad aleatorio (values)
        for nombre in random.sample(self.nombres, numero_conductores):
            self.conductores[nombre] = random.randint(1, 10)
        #DEBUG : Imprimir nuestra lista conductores
        # print(self.conductores)
    
    def viajes_disponibles(self, numero_viajes : int):
        #Inicializamos id_viaje = 1
        id_viaje = 1
        #Generar un diccionario con id_viaje incrementando 1 en 1 (keys), y tarifa calculada (values)
        for i in range(numero_viajes):
            agnos_trabajando = self.obtener_agnos_trabajando()[1]
            self.viajes[id_viaje] = self.calcular_tarifa(agnos_trabajando)
            id_viaje += 1 
        #DEBUG : Imprimir nuestra lista viajes
        print(self.viajes)

    def siguiente_usuario(self):
        #Guardamos nuestro usuario con mas alta priorida en sig_usuario
        sig_usuario = min(self.usuarios, key = self.usuarios.get)
        #Eliminamos a sig_usuario del diccionario, por si hay dobles con la misma prioridad
        del self.usuarios[sig_usuario]
        #Regresamos el sig_usuario
        return sig_usuario

    def siguiente_viaje(self):
        #Guardamos nuestro viaje con mas baja tarifa
        sig_viaje = min(self.viajes, key = self.viajes.get)
        #Eliminamos a sig_viaje del diccionario
        del self.viajes[sig_viaje]
        #Regresamos el sig_viaje
        return sig_viaje

    def obtener_agnos_trabajando(self):
        #Obtenemos el conductor con menor agnos trabajando(key y value)
        sig_conductor_key_value = min(self.conductores.items(), key = lambda k : k[1])
        #DEBUG : Imprimir key y value del conductor con menor agnos trabajando
        # print(sig_conductor_key_value)
        #Borramos al conductor encontrado del diccionario
        del self.conductores[sig_conductor_key_value[0]]
        #DEBUG : Comprobamos que se elimino el conductor
        # print(self.conductores)
        #Regresamos el numero de agnos del conductor con menor agnos trabajando
        return sig_conductor_key_value

    def calcular_tarifa(self, agnos : int):
        return 20 + (10 * agnos)

if __name__ == '__main__':           
    practica = Practica6()
    n = 5
    #QUITAR COMENTARIOS PARA USAR CON ALEATORIEDAD
    # print('Usuarios:')
    # practica.generar_diccionario_usuarios(n)
    # print('\nConductores:')
    # practica.extraer_conductores(n)
    print('\nViajes:')
    practica.viajes_disponibles(n)
    print('\nResultados:')
    practica.funcion_principal(n)