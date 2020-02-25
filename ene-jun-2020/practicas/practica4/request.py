from abc import ABC, abstractclassmethod
import requests

class Anime():
    def __init__(self, title, episodes, desc):
        self.Title = title
        self.Episodes = episodes
        self.Description = desc

class BiblioAnime(ABC):
    @abstractclassmethod
    def Search(id):
        pass

def getAnime(id, bibliotec):
    anime = bibliotec.Search(id)

    return anime.Title


class Jikan(BiblioAnime):
    def __init__(self, url_base):
        self.url = url_base

    def Search(self, id):
        res = requests.get("{}/{}".format(self.url, id))
        json = res.json()
        return Anime(json['title'], json['episodes'], json['synopsis'])

if __name__ == "__main__":
    biblio = Jikan("https://api.jikan.moe/v3/anime")
    print(getAnime("5114", biblio))