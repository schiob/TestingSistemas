from dime import *
from tkinter import *
txt=""
ventana = Tk()
ventana.geometry("600x600+0+0")
ventana.title("2 Parcial")
#barra de menus
barraMenu=Menu(ventana)
#creacion de menus
mnuBusqueda=Menu(barraMenu)
mnuOpciones=Menu(barraMenu)
mnuBusqueda.add_command(label="Busquedapor URL")
mnuOpciones.add_command(label="Guardar Video")
mnuOpciones.add_command(label="Mostrar Lista")
mnuOpciones.add_command(label="Mostrar Video")
mnuOpciones.add_command(label="Modificar Video")
mnuOpciones.add_command(label="Borrar Video")
barraMenu.add_cascade(label="busqueda youtube",menu=mnuBusqueda)
barraMenu.add_cascade(label="Opciones",menu=mnuOpciones)
ventana.config(menu=barraMenu)




class ChioYoutube(AbstractYoutube):
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
def opc1():
    vent=Tk()
    vent.geometry("200x200+100+1000")
    lblurl=label("ingresa url",font=("Arial"),18)
    entraurl=Entry(vent,textvariable=lblurl)
    btn=Button(vent,"accion")
    ventana.mainloop()
def main():




if __name__ == '__main__':
    main()
