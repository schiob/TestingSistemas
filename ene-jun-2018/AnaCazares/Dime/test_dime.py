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
