import os.path
from csv import reader

def funcion_principal(archivo):
    
    if os.path.isfile(archivo):

        if len(archivo) > 0 or len(archivo) < 100:

            lista = open(archivo, 'r')
            mayor = 0.0
            juguete = []
            
            for a in lista:
                juguete = a.split(' ')
                print(juguete[0])
                if mayor <= float(juguete[1]):
                    mayor = float(juguete[1])
                    cosa = str(juguete[0])
            return cosa

        return "El tamaño del archivo no esta dentro de los requerimentos"
    return "Lo que has entregado no es un archivo"

if __name__ == '__main__':
    print(funcion_principal("ene-jun-2021\David-Navoa-Acevedo\Extra\Problema-2\cosa.txt"))