from dime import *

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
