from dime import *

class appYoutube(AbstractYoutube):
    def __init__(self, algo):
        self.algo = algo

    def InfoVideo(self, url):
        return Video("nombre", "1234", "canal", "today", 123, 42, "una descripcion")

def GuardarVideo(appYoutube, anaRepo, url, categorias):
    # Buscar video en youtube
    video = claseYoutube.InfoVideo(url)
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

    while True:
        bienvenido = "------------- Bienvenido ------------"
        opcion = int(input("-----Menu----- 1... Guardar \n2... Ver Lista \n3... Ver Video \n4...  modificar \n5... Borrar \n0... Salir\n"))
        if opcion == 1:
            if MostrarLista() == None:
                print("No hay informacion")
                urll = int(input("Ingresa URL para buscar un video :"+"\n"))
                video = appYoutube.InfoVideo(urll)
                x = str(input("Ingresa CATEGORIA :"+"\n"))
                video.Categorias = x
                print(GuardarVideo(video,x)+"\npara continuar ingresa cualquir valor")
                r=input()
                continue
            else:
                urll = int(input("Ingresa URL del video :"+"\n"))
                video = appYoutube.InfoVideo(urll)
                q=GuardarVideo(video)
                print(q+"\npara continuar ingresa cualquir valor")
                r=input()
                continue
        elif opcion == 2:
            if MostrarLista() == None:
                cat = str(input("no hay informacion : \ INGRESA VALOR X PARA REGRESAR"))
                print(cat)

            else :
                w=MostrarLista()
                print(w)
                F=input("PRESIONA CUALQUIER TECLA PARA CONTINUAR")
                continue


        elif opcion == 3:
            print("VIDEOS DISPONIBLES\n"+MostrarLista())
            r=input()
            preg=str(input("Para ver un VIDEO ingresa el ID :"))
            print(MostrarVideo(preg))
            t=input()
            continue
        elif opcion == 4:
            print("Busca el ID del video  MODIFICAR \n\n"+MostrarLista())
            g=input("teclea para continuar")
            uu=int(input("ingrese id :"))
            vd = claseYoutube.InfoVideo(uu)
            ed=int(input("para editar descipcion ingresa 1\npara categoria ingresa 2"))
            if ed == 1:
                vd.Descripcion=str(input("ingresa la nueva descripcion :"))
                print("descripcion editada")
            elif ed == 2:
                f=str(input("ingresa nueva categoria"))
                vd.Categorias = f
                print("Categoria editada")
            vid_ed=anaRepo.ModificarVideo(vd)


        elif cons == 5:
            MostrarLista()
            uu=int(input("ingrese id :"))
            vid = claseYoutube.InfoVideo(uu)
            u=int(input("ingrese id para confirmar que quieres borrar este video:"))
            BorrarVideo(u)
        else :
            continue

if __name__ == '__main__':
    main()
