from apiclient.discovery import build
from Youtube import Video
from Youtube import AbstractYoutube

class AppYoutube(AbstractYoutube):
    def InfoVideo(self, url):

        API_KEY = 'AIzaSyBOcBaTZx4cZdVvrVdQujN4TuoC9vP0F8A'
        youtube = build('youtube', 'v3', developerKey=API_KEY)

        ids = url[32:43]
        results = youtube.videos().list(id=ids, part='snippet').execute()
        for result in results.get('items', []):
            NombreCanal = (result['snippet']['channelTitle'])
            Titulo = (result['snippet']['title'])
            Descripcion = (result['snippet']['description'])
            Fecha = result['snippet']['publishedAt']

        results1 = youtube.videos().list(id=ids, part='statistics').execute()
        for result2 in results1.get('items', []):
            Likes = result2['statistics']['likeCount']
            Vistas = result2['statistics']['viewCount']

        results4 = youtube.videos().list(id=ids, part='contentDetails').execute()
        for result5 in results4.get('items', []):
            Duracion = result5['contentDetails']['duration']

        return Video(Titulo, Duracion, NombreCanal, Fecha, Likes, Vistas, Descripcion)

class videos():
    y = AppYoutube()

    vid = y.InfoVideo('https://www.youtube.com/watch?v=Z58XTzv0ALQ')


if __name__ == '__main__':
    y = AppYoutube()
    url=input("Ingrese url: ")
    vid = y.InfoVideo(url)
    print(vid.Titulo)
    print(vid.Descripcion)
    print(vid.Duracion)
    print(vid.NombreCanal)
    print(vid.Fecha)
    print(vid.Likes)
    print(vid.Descripcion)
    print(vid.Vistas)
