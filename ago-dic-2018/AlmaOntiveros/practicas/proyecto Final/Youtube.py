from abc import ABC, abstractmethod


class Video():
    def __init__(self, titulo, duracion, canal, fecha, likes, vistas, descripcion, id=None, compartidas=None):
        self.Id = id
        self.Titulo = titulo
        self.Duracion = duracion
        self.NombreCanal = canal
        self.Fecha = fecha
        self.Likes = likes
        self.Vistas = vistas
        self.Descripcion = descripcion
        self.Compartidas = compartidas


class Categoria():
    def __init__(self, id, nombre):
        self.Id = id
        self.Titulo = nombre


class AbstractRepo(ABC):
    @abstractmethod
    def GuardarVideo(self, video):
        pass

    @abstractmethod
    def MostrarLista(self):
        pass

    @abstractmethod
    def MostrarVideo(self, id):
        pass

    @abstractmethod
    def ModificarVideo(self, video):
        pass

    @abstractmethod
    def BorrarVideo(self, id):
        pass


class AbstractYoutube(ABC):
    @abstractmethod
    def InfoVideo(self, url):
        pass


if __name__ == "__main__":
    cat = Categoria(24, "algo")
    print(cat.Titulo)
