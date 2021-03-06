import csv
import os
 
"""usuario,correo,puntos
    Tom,    tomas@hotmail.com,       85
    Juan,   juan@hotmail.com,        75
    Maria,  maria84@gmail.com,       90
    Paco,   paquito123@outlook.com,  74
    Ana,    anaa22@gmail.com,        88
    Marcos, marcosss@hotmail.com,    92"""
def avg():  
    #archivo_nom = "files.csv"
    archivo = open("files.csv", "r")
    for linea in archivo:
         
        datos = linea.strip().split(",")
        #valores = list(map(float, datos[1:3]))
        #print(datos[1:3][0:2])
        print(datos[2:])
        #archivo.close()
 

avg()