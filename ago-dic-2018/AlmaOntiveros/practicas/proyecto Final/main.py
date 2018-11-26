from Youtube import *
from base_de_datos import SQlite
from dos_youtube import AppYoutube
from dos_youtube import videos
from time import sleep
import sqlite3
import random
conexion = sqlite3.connect('Youtube.db')
cursor = conexion.cursor()

def GuardarVideo(AppYoutube, SQlite, url, Compartidas):
    # Buscar video en youtube
    vid = AppYoutube.InfoVideo(url)
    # Agregar las categorias
    # Guardar
    new_video = SQlite.GuardarVideo(vid)
    # Mostrar el id con el que se guardó
    #return new_video.Id


def MostrarLista():
    lista = SQlite.MostrarLista()
    return lista

def MostrarVideo(id):
    # recibiendo el ID del video, te debe mostrar el video con sus demás datos
    muestra_video=SQlite.MostrarVideo(id)
    return muestra_video

def ModificarVideo(id,Compartidas):
    modificar = SQlite.ModificarVideo(id,Compartidas)
    return modificar

def BorrarVideo(id):
    borrar = SQlite.BorrarVideo(id)
    return borrar


def main():
    BD = SQlite()
    YT= AppYoutube()
    while True:
        bienvenido = "------------- Bienvenido ------------"
        opcion = int(input("---Menu Principal--- \n1.Guardar \n2.Ver Lista \n3.Ver Video \n4.Modificar Video \n5.Borrar Video \n0.Salir\n"))
        if opcion == 1:
            url = input("Ingresa URL para guardar un video :"+"\n")
            Compartidas = input("Ingresa numero de veces compartidas :"+"\n")
            GuardarVideo(YT,BD,url,Compartidas)


            continue

        elif opcion == 2:
            if MostrarLista() == None:
                print("No hay videos agregados, regresando al menú...")
                sleep(1)
                continue
            else :
                w=MostrarLista()
                for x in w:
                    print(x)

                continue


        elif opcion == 3:

            id=input("inserte id de video: ")
            print (MostrarVideo(id))

            continue

        elif opcion == 4:
            id=input("inserte id de video a modificar:")
            Compartidas=int(input("ingrese el numero de veces compartido"))
            ModificarVideo(id,Compartidas)



            continue


        elif opcion == 5:
            id=input("inserte id de video a eliminar:")
            BorrarVideo(id)

        elif opcion == 0:
            print("Saliendo del menú...")
            sleep(1)
            break

if __name__ == '__main__':
    main()
