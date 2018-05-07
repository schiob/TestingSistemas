from abc import ABC, abstractmethod


class Video():
    def __init__(self, nombre, duracion, canal, fecha, likes, vistas, descripcion, id=None, categorias=None):
        self.Id = id
        self.Nombre = nombre
        self.Duracion = duracion
        self.Canal = canal
        self.Categorias = categorias
        self.Fecha = fecha
        self.Likes = likes
        self.Vistas = vistas
        self.Descripcion = descripcion


class Categoria():
    def __init__(self, id, nombre):
        self.Id = id
        self.Nombre = nombre
    


class AbstractRepo(ABC):
    @abstractmethod
    def GuardarVideo(self, video):
        '''Toma como parámetro un video (instancia clase Video) y lo guarda en la BD.
        Regresa el video como tal, con el Id que se le asignó.
        '''
        pass

    @abstractmethod
    def MostrarLista(self):
        '''Regresa una lista (arreglo) de videos (instacia clase Video)'''
        pass

    @abstractmethod
    def MostrarVideo(self, id):
        '''Toma el id de un video y regresa el video'''
        pass

    @abstractmethod
    def ModificarVideo(self, video):
        '''Toma un video, con sus datos modificados y hace el update en la base de datos.
        Regresa el video como tal, con la nueva información que se guardó.
        '''
        pass

    @abstractmethod
    def BorrarVideo(self, id):
        '''Toma un id de un video y lo borra de la base de datos.
        Regresa un bool que determina si se pudo borrar o no.
        '''
        pass


class AbstractYoutube(ABC):
    @abstractmethod
    def InfoVideo(self, url):
        '''Toma como parámetro la url de un video y regresa un video (instancia de la clase Video)
        '''
        pass


if __name__ == "__main__":
    cat = Categoria(24, "algo")
    print(cat.Nombre)
