from estadisticas import *
import requests
from Metodos import mostrar_mob
from Interfaces import Mostrar_detalles_del_mob
class menu:
    #Primer capa del menu
    def opciones_1(self, opciones: int):
        #1 = consultar mob, 2 = Mostrar la lista de mobs, 3 = actualizar mob, 4 = Mostrar estadisticas del mob
        if(opciones == 1):
            print("Escribe el nombre del mob que deseas consultar: ", Introducir_datos)
            mostrar_mob(Introducir_datos)
        elif(opciones == 2):
            print("Esta es la lista de mobs: ", show_mobs_list)
        elif(opciones == 3):
            print("Que mob deseas actualizar?:", nombre_del_mob_en_str)
        elif(opciones == 4):
            print("Estas son las estadisticas de los mobs: ", estadisticas)
    
    #Segunda capa del menu
    def opciones_2(self, opciones: int):
        #
        pass