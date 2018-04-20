from dime import *

class ChioYoutube(AbstractYoutube):
    def __init__(self, algo):
        self.algo = algo

    def InfoVideo(self, url):
        return Video("nombre", "1234", "canal", "today", 123, 42, "una descripcion")

def GuardarVideo(claseYoutube, anaRepo, url, categorias):
    # Buscar video en youtube
    video = claseYoutube.InfoVideo(url)
    # Agregar las categorías
    video.Categorias = categorias
    # Guardar
    new_video = anaRepo.GuardarVideo(video)

    # Mostrar el id con el que se guardó
    return new_video.Id

def BuscarVideo(claseYoutube, anaRepo, id):
    # Mostrar lista
    lista = anaRepo.MostrarLista()
    print("Escriba para buscar video por id\n")
    id = input()
    if id in lista:
        return anaRepo.MostrarVideo(id)
    else:
        return "No se ha podido encontrar el video en la lista"
    # Buscar Video en la lista por nombre


def EditarVideo(claseYoutube, anaRepo, id, categorias, nombre, descripcion):
    # Mostrar lista
    lista = claseYoutube.MostrarLista()
    # Buscar el video a editar
    print("Escriba el id del video para editarlo\n")
    id = input()
    if id in lista:
        print("¿Qué es lo que quiere editar?")
        editar = input()
        video = claseYoutube.InfoVideo(url)
        # Los demás elementos se actualizan directamente de Youtube

        if editar == 'categoria':
            print("Escriba la categoria del video")
            categoria = input()
            video.Categorias = categoria
        elif editar == 'descripcion':
            print("Editar la descripcion del video")
            descripcion = input()
            video.Descripcion = descripcion
        edited_video = anaRepo.ModificarVideo(id)
    else:
        print("No se ha podido encontrar el video en la lista")


def BorrarVideo(id):
    # Mostrar lista
    lista = claseYoutube.MostrarLista()
    # Buscar el video a borrar
    print("Escriba el id del video para borrarlo\n")
    id = input()
    if id in lista:
        print("Está seguro que quiere borrar el video "+ anaRepo.Nombre(id) + ' ?')
        resp = input('Escriba Y o N\n')
        if resp == 'y':
            elim_video = anaRepo.BorrarVideo(id)
        elif resp == 'n':
            return 'No se eliminó el video'
        else:
            return 'Comando invalido'

def menu():

    print("Selecciona una de las siguientes opciones\n")
    print("1 - Guardar Video\n")
    print("2 - Buscar Video\n")
    print("3 - Editar Video\n")
    print("4 - Borrar Video\n")
    print("0 - Salir\n")


def main():
    inter_youtube = ChioYoutube('algo')
    vi1 = inter_youtube.InfoVideo("https://www.youtube.com/watch?v=X9A1Ny6B310")
    print(vi1.Duracion)
    print(vi1.Categorias)

    # Opcion 1
    # Leer de la terminal la url
    print("pasame la url:")
    url = input()
    # Mostrar la opcion de agregar categorias
    print("quiere categoria primo?")
    cat = input()
    categorias_lista.append(cat)

    id_video = GuardarVideo(inter_youtube, ana_repo, url, categorias_lista)
    print("se guardó el video con el id {}".format(id_video))

    while True:

    	# Mostramos el menu
    	menu()

    	opcionMenu = input("Inserta un número >> ")

    	if opcionMenu=="1":

    		print ("")
    		input("Has pulsado la opción 1...\npulsa una tecla para continuar")
            GuardarVideo()

    	elif opcionMenu=="2":

    		print ("")
    		input("Has pulsado la opción 2...\npulsa una tecla para continuar")
            BuscarVideo()


    	elif opcionMenu=="3":

    		print ("")
    		input("Has pulsado la opción 3...\npulsa una tecla para continuar")
            EditarVideo()


        elif opcionMenu=="4":

    		print ("")
    		input("Has pulsado la opción 4...\npulsa una tecla para continuar")
            BorrarVideo()


    	elif opcionMenu=="0":

    		break

    	else:

    		print ("")
    		input("No has tecleado una opción valida...\npulsa una tecla para continuar")

    """
    anaRepo = SQLite()
    Youtube = ChioYoutube()
    Run(anaRepo, Youtube)

    inversion de dependencia
    inyeccion de dependencia
    """

if __name__ == '__main__':
    main()
