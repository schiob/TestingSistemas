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

def BuscarVideo(claseYoutube, anaRepo):
    # Mostrar lista
    lista = anaRepo.MostrarLista()
    # Buscar Video en la lista por nombre
    print("Escriba para buscar video por id\n")
    id = input()
    if id in lista:
        return claseYoutube.MostrarVideo
    else:
        print("No se ha podido encontrar el video en la lista")

def EditarVideo(claseYoutube, anaRepo, id, categorias, nombre, descripcion):
    # Mostrar lista
    lista = claseYoutube.MostrarLista()
    # Buscar el video a editar
    print("Escriba para buscar video por id y editarlo\n")
    id = input()
    if id in lista:
        print("¿Qué es lo que quiere editar?")
        editar = input()
        video = claseYoutube.InfoVideo(url)
        # Los demás elementos se actualizan directamente de Youtube
        if editar == 'nombre':
            print("Escriba nuevo nombre")
            nombre = input()
            video.Nombre = nombre
        elif editar == 'categoria':
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


def BorrarVideo():
    # Mostrar lista
    lista = claseYoutube.MostrarLista()
    # Buscar el video a borrar
    print("Escriba para buscar video por id y borrarlo\n")
    id = input()
    if id in lista:
        print("Está seguro que quiere borrar el video "+ anaRepo.Nombre(id) + ' ?')
        resp = input('Escriba Y o N\n')
        if resp == 'y':
            elim_video = anaRepo.BorrarVideo(id)
        elif resp == 'n':
            print('No se eliminó el video')
        else:
            print('Comando invalido')

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


if __name__ == '__main__':
main()
