from Interfaces import Mostrar_detalles_del_mob
import requests

class mob:
    
    def mostrar_mob(self, nombre:str):
        response = requests.get("https://swarfarm.com/api/v2/monsters/?name=rakan").json()
        data = response['results']
        for i in data:
            print("name: ", i['name'], "element: ", i['element'], "runas: ", False, "skills: ", i['skills'])
        return Mostrar_detalles_del_mob(nombre)
    def mostrar_lista_de_mob(self):
        #codigo de para mostrar una lista de mobs
        #filtrar datos del request
        pass