import sqlite3
from Youtube import *
import random
from dos_youtube import AppYoutube
class SQlite(AbstractRepo):



    def GuardarVideo(self, video):
        # Insertar video
        conexion = sqlite3.connect('Youtube.db')
        cursor =conexion.cursor()
        ID=random.randrange(100000)
        y = AppYoutube()
        url=input("Ingrese url: ")
        Compartidas=int(input("Ingrese numero de veces compartido: "))
        vid = y.InfoVideo(url)
        cursor.execute("INSERT INTO VIDEO (ID,NOMBRE,DURACION,CANAL,FECHA,LIKES,VISTAS,DESCRIPCION,COMPARTIDAS) VALUES(?,?,?,?,?,?,?,?,?)",(ID,vid.Titulo,vid.Duracion,vid.NombreCanal,vid.Fecha,vid.Likes,vid.Vistas,vid.Descripcion,Compartidas))
        conexion.commit()#guarda cambios
        #Guardar_Video=cursor.execute("INSERT INTO VIDEO (ID,NOMBRE,DURACION,CANAL,FECHA,LIKES,VISTAS,DESCRIPCION,COMPARTIDAS) VALUES(?,?,?,?,?,?,?,?,?)",(ID,vid.Titulo,vid.Duracion,vid.NombreCanal,vid.Fecha,vid.Likes,vid.Vistas,vid.Descripcion,Compartidas))
        print("Se creo el video")
        conexion.commit()#guarda cambios)
        #return Guardar_Video
        #ID = self.cursor.lastrowid


        return video

    def MostrarLista():
        conexion = sqlite3.connect('Youtube.db')
        cursor =conexion.cursor()
        MostrarLista=cursor.execute("SELECT * from VIDEO")
        return MostrarLista.fetchall()

    def MostrarVideo(id):
        conexion = sqlite3.connect('Youtube.db')
        cursor =conexion.cursor()
        #X=input("Para ver un VIDEO ingresa el ID:")
        MostrarVideo=cursor.execute("SELECT * from VIDEO WHERE ID=?",(id,))
        return MostrarVideo.fetchall()


    def ModificarVideo(id,Compartidas):
        conexion = sqlite3.connect('Youtube.db')
        cursor =conexion.cursor()
        #X=input("Ingrese el id del video que desea modificar:")
        #Compartidas=int(input("ingrese el numero de veces compartido"))
        cursor.execute("Update VIDEO SET Compartidas=? WHERE ID=?",(Compartidas,id))
        conexion.commit()



    def BorrarVideo(id):
        conexion = sqlite3.connect('Youtube.db')
        cursor =conexion.cursor()
        #X=input("Ingrese el id del video que desea eliminar:")
        BorrarVideo=cursor.execute("DELETE FROM VIDEO WHERE ID=?",(id,))
        print("Video eliminado")
        conexion.commit()


    def Close(self):
        self.conexion.close()

if __name__ == '__main__':
    v = Video("1","nombre diferente", "13", "canal de prueba", "09/09/2018", 53, 100, "video", "152")

    base_de_datos = SQlite()

    #Guardar video
    db_video = base_de_datos.GuardarVideo(v)
    print(db_video)

     #Get one video
    video_de_query = base_de_datos.MostrarVideo()
    print(video_de_query.Id)
    print(video_de_query.Nombre)
    print(video_de_query.Categorias)

    base_de_datos.BorrarVideo(4)

    base_de_datos.ModificarVideo(v)

    # Get All videos
    videos = base_de_datos.MostrarLista()
    for vid in videos:
        print(vid.Id, vid.Nombre, vid.Categorias)

    base_de_datos.Close()
