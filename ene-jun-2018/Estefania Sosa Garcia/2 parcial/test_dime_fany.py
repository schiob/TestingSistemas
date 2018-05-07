from dime import *
from time import sleep

class AppYoutube(AbstractYoutube):
    def __init__(self, algo):
        self.algo = algo

    def InfoVideo(self, url):
        return Video("nombre", "1234", "canal", "today", 123, 42, "una descripcion")

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
    video = anaRepo.MostrarLista()
    return video

def MostrarVideo(anaRepo,ID):
    #mostrar video
    muestra_video=anaRepo.MostrarVideo(ID)
    return muestra_video

def ModificarVideo(anaRepo,video):
    modificas = anaRepo.ModificarVideo(video)
    return modificas

def BorarVideo(anaRepo,ID):
    elimina=anaRepo.BorrarVideo(ID)
    return elimina


def main():
    ana = anaRepo()
    youtube= AppYoutube()
    while True:
        bienvenido = "------------- Bienvenido ------------"
        opcion = int(input("-----Menu----- 1... Guardar \n2... Ver Lista \n3... Ver Video \n4...  modificar \n5... Borrar \n0... Salir\n"))
        if opcion == 1:
            if MostrarLista() == None:
                print("No hay informacion")
                urll = int(input("Ingresa URL para buscar un video :"+"\n"))
                x = str(input("Ingresa CATEGORIA :"+"\n"))
                print("Se creo el video con el ID :"+GuardarVideo(youtube,ana,urll,x))
                sleep(5)
                continue
            else:
                urll = int(input("Ingresa URL del video :"+"\n"))
                cat = int(input("Ingresa URL del video :"+"\n"))
                q=GuardarVideo(youtube,ana,urll,cat)
                sleep(5)
        elif opcion == 2:
            if MostrarLista() == None:
                cat = str(input("No hay informacion : \n INGRESA VALOR X PARA REGRESAR"))
                print(cat)
                imput()
                continue

            else :
                w=MostrarLista()
                for x  in w:
                    print(w)
                F=input("PRESIONA CUALQUIER TECLA PARA CONTINUAR")
                continue


        elif opcion == 3:
            w=MostrarLista()
            print("VIDEOS DISPONIBLES\n")
            for e in w:
                print("-->"+e)
            r=input()
            preg=str(input("Para ver un VIDEO ingresa el ID :"))
            print(MostrarVideo(preg))
            t=input()
            continue
        elif opcion == 4:
            print("Busca el ID del video a MODIFICAR \n\n")
            x=MostrarLista()
            for i in x:
                print(i)
            g=input("teclea para continuar")
            uu=int(input("ingrese url :"))
            print(AppYoutube.InfoVideo(uu)+"\n")
            ed=int(input("¡ Que te gustaria editar ?\n---descipcion ingresa 1\n---categoria ingresa 2\n"))
            #vd = Video()
            if ed == 1:
                youtube.Descripcion=str(input("ingresa la nueva descripcion :"))
                print("descripcion editada")
            elif ed == 2:
                f=str(input("ingresa nueva categoria"))
                youtube.categorias = f
                print("Categoria editada")
            t=AppYoutube.InfoVideo(uu)
            ModificarVideo(youtube,ana,t)
            sleep(3)
            continue


        elif opcion == 5:
            x=MostrarLista()
            for i in x:
                print(i)
            uu=int(input("ingrese id :"))
            vid = AppYoutube.InfoVideo(uu)
            u=int(input("ingrese id para confirmar que quieres borrar este video:"))
            BorrarVideo(u)
        else :
            continue

if __name__ == '__main__':
    main()
