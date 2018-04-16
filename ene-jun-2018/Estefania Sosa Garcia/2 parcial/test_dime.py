from dime import *

class ChioYoutube(AbstractYoutube):
    cat = 0
    vid = 0
    def __init__(self, algo):
        self.algo = algo

    def InfoVideo(self, url):
        return Video("nombre", "1234", "canal", "today", 123, 42, "una descripcion")

def GuardarVideo(claseYoutube, anaRepo, url, categorias):
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
    video = Video()

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
    saludo = "BIENVENIDO ".capitalize()
    mensaje1 = " BUSQUEDA YOUTUBE ".capitalize()
    mensaje2 = "MENU".capitalize()
    menu="(1)...Ingresar Url : \n(2)...MENU \n(3)...SALIR "
    print saludo.ljust(50, "=")
    while true:
        opcion = int(input(menu))
        if opcion == 1:
            print mensaje1.ljust(50, "=")
            urll = int(input("Ingresa URL del video :"))
            if MostrarLista == null:
                cat = str(input("ingrese categoria :"))
                categoria = Categoria(1,cat)
                GuardarVideo(video,categoria)
                returnn = int(input("ingresa 1 para continuar"))
                pass
                continue
            else :
                MostrarLista()
                cate=str(int("ingrese categoria :"))
                GuardarVideo(video,cate)
                pass
                continue
        elif opcion == 2:
            cons = str(input('''opciones
            1...{}
            2...{}
            3...{}
            4...{}
            5...{}
            6...{}
                '''.format("Guardar","ver Lista","ver videos","modificar","borrar","guardar"))
                if cons == 1:
                    ur = str(input("ingrese url del video:"))
                    a = str(input("ingrese categoria :"))

                    cate = Categoria(1,cat)
                    GuardarVideo(ur,a)
                elif cons == 2:
                elif cons == 3:
                elif cons == 4:
                elif cons == 5:
                elif cons == 6:
        elif opcion == 3:
            break
               
if __name__ == '__main__':
    main()
