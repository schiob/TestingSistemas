import Parcial2
import os
def Leer_Archivo(path):
    archivo = open(path, 'r')
    datos = archivo.readline()
    separador = datos.split(',')
    archivo.close()
    return separador

def Crear_Archivo(path):
    archivo = open(path, 'w')
    archivo.write('Jose_Lopez quimica 89.00, Jose_Lopez matematicas 85.34, Maria_Martinez fisica 95.50, Maria_Martinez espaÃ±ol 90.00')
    archivo.close()

def borrar_Archivo(path):
    os.remove(path)


def main():
    Leer_Archivo("C:\\Users\\jorge\\Documents\\Cursos\\TestingSistemas\\ago-dic-2019\\Jorge Alberto Hernandez Sanchez\\Practicas\\SegundoParcial\\CalificacionesPrueba.txt")
    Crear_Archivo("C:\\Users\\jorge\\Documents\\Cursos\\TestingSistemas\\ago-dic-2019\\Jorge Alberto Hernandez Sanchez\\Practicas\\SegundoParcial\\CalificacionesPrueba.txt")
    Parcial2.Calificaciones(Leer_Archivo("C:\\Users\\jorge\\Documents\\Cursos\\TestingSistemas\\ago-dic-2019\\Jorge Alberto Hernandez Sanchez\\Practicas\\SegundoParcial\\CalificacionesPrueba.txt"))
    borrar_Archivo("C:\\Users\\jorge\\Documents\\Cursos\\TestingSistemas\\ago-dic-2019\\Jorge Alberto Hernandez Sanchez\\Practicas\\SegundoParcial\\CalificacionesPrueba.txt")