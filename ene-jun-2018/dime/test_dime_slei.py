from dime import *
from time import sleep

class AppYoutube(AbstractYoutube):

    def __init__(self, algo):
        self.algo = algo

    def InfoVideo(self, url):

        API_KEY = 'AIzaSyAF3BIAdtEu6Y3NR_BtkhViMfOGRxCD84Q'
        youtube = build('youtube', 'v3', developerKey=API_KEY)

        ids = url[32:43]
        results = youtube.videos().list(id=ids, part='snippet').execute()
        for result in results.get('items', []):
            NombreCanal = emoji.demojize(result['snippet']['channelTitle'])
            Titulo = emoji.demojize(result['snippet']['title'])
            Descripcion = emoji.demojize(result['snippet']['description'])
            Publicacion = result['snippet']['publishedAt']


        results1 = youtube.videos().list(id=ids, part='statistics').execute()
        for result2 in results1.get('items', []):
            Likes = result2['statistics']['likeCount']
            Vistas = result2['statistics']['viewCount']


        results4 = youtube.videos().list(id=ids, part='contentDetails').execute()
        for result5 in results4.get('items', []):
            Duracion = result5['contentDetails']['duration']

        return Video(Titulo, NombreCanal, Descripcion, Publicacion, Likes, Vistas, Duracion)


def GuardarVideo(AppYoutube, anaRepo, url, categorias):
    # Buscar video en youtube
    video = AppYoutube.InfoVideo(url)
    # Agregar las categorias
    video.Categorias = categorias
    # Guardar
    new_video = anaRepo.GuardarVideo(video)
    # Mostrar el id con el que se guardó
    return new_video.Id


def MostrarLista(anaRepo):
    #regresar datos de ana_repo
    lista = anaRepo.MostrarLista()
    return lista

def MostrarVideo(anaRepo,id):
    # recibiendo el ID del video, te debe mostrar el video con sus demás datos
    muestra_video=anaRepo.MostrarVideo(id)
    return muestra_video

def ModificarVideo(anaRepo,id):
    modificar = anaRepo.ModificarVideo(video)
    return modificar

def BorarVideo(anaRepo,id):
    borrar = anaRepo.BorrarVideo(id)
    return borrar


def main():
    BD = anaRepo()
    YT= AppYoutube()
    while True:
        bienvenido = "------------- Bienvenido ------------"
        opcion = int(input("-----Menu----- 1... Guardar \n2... Ver Lista \n3... Ver Video \n4...  modificar \n5... Borrar \n0... Salir\n"))
        if opcion == 1:
            if MostrarLista() == None:
                print("No hay videos guardados")
            urll = int(input("Ingresa URL para guardar un video :"+"\n"))
            categ = str(input("Ingresa CATEGORIA :"+"\n"))
            print("Se creo el video con el ID: "+GuardarVideo(YT,BD,urll,x))
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
                F=input("Presiona cualquier tecla para continuar...")
                continue


        elif opcion == 3:
            """Para no hacer lo mismo que en la opc 2, se recomienda haber ido
            primero a la opc 2, copiar el id del video que quieres visualizar y
            darlo como parametro en el input de 'preg'
            """
            preg=str(input("Para ver un VIDEO ingresa el ID:"))
            print(MostrarVideo(preg))
            F=input("Presiona cualquier tecla para continuar...")
            continue

        elif opcion == 4:

            print("Escribe el ID del video a MODIFICAR \n\n")

            mod=int(input())
            print(AppYoutube.InfoVideo(mod)+"\n")
            ed=int(input("¿ Qué te gustaria editar ?\n---Descripción, ingresa 1\n---Categoria, ingresa 2\n"))
            #vd = Video()
            if ed == 1:
                vd.Descripcion=str(input("ingresa la nueva descripción :"))
                print("descripción editada")
            elif ed == 2:
                f=str(input("ingresa nueva categoria"))
                vd.Categorias = f
                print("Categoria editada")
                #vid_ed=anaRepo.ModificarVideo(vd)
            else:
                print("Teclea sólo 1 o 2, regresando al menú...")
                sleep(1)
            continue


        elif opcion == 5:
            MostrarLista()
            eliminar1 = int(input("Ingrese el ID del video a eliminar: "))
            vid = AppYoutube.InfoVideo(eliminar1)
            eliminar2=int(input("Reingrese ID para confirmar que quieres borrar este video: "))
            if eliminar2 == eliminar1:
                BorrarVideo(eliminar2)
            else :
                print("Los ID no coinciden, regresando al menú...")
                sleep(1)
                continue
        elif opcion == 0:
            print("Saliendo del menú...")
            sleep(1)
            break

if __name__ == '__main__':
    main()
