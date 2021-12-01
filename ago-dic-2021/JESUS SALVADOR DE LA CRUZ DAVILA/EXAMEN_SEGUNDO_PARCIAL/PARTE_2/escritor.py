from escritor_Interfaz import *

class Escribiendo(Escritor):
    def numero_de_palabras(datos):
        variable = datos.count('e')
        return variable


if __name__ == '__main__':
    escribir = input('Escribe algo, lo que quieras: ')
    print(Escribiendo.numero_de_palabras(escribir))