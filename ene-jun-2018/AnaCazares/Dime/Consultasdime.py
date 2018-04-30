
import sqlite3
from dime import *

class SQlite(AbstractSQlite):
   
	#conectar con bd

	conexion = sqlite3.connect('dime.db')
	cursor = conexion.cursor()

	def Guardar_Video(self, video):
    	cursor.execute("INSERT INTO VIDEO VALUES (ID_VIDEO)")    	
    	conexion.commit()#guarda cambios
    	Guardar_Video=cursor.execute("INSERT INTO VIDEO VALUES (ID_VIDEO)")
    	return Guardar_Video.fetchall()
    	cursor.close() 

	def MostrarLista(self):
    	cursor.execute("SELECT * from VIDEO")
    	conexion.commit()
    	MostrarLista=cursor.execute("SELECT * from VIDEO")
    	return MostrarLista.fetchall()
    	cursor.close() 

	def MostrarVideo(self, id):
    	cursor.execute("SELECT * from VIDEO where ID_VIDEO='id_video'")
    	conexion.commit()
    	MostrarVideo = cursor.execute("SELECT * from VIDEO where ID_VIDEO='id_video'")
    	return MostrarVideo.fetchall()
    	cursor.close()

       	
	def ModificarVideo(self, video ):
    	cursor.execute("UPDATE VIDEO SET ID_VIDEO='id_video', NOMBRE_VIDEO='nombre', CANAL='canal_video', VISITAS=visitas_video, FECHA='fecha_video', CATEGORIA='categori_video' where NOMBRE_VIDEO='nombre'")
    	conexion.commit()
    	ModificarVideo=cursor.execute("UPDATE VIDEO SET ID_VIDEO='id_video', NOMBRE_VIDEO='nombre', CANAL='canal_video', VISITAS=visitas_video, FECHA='fecha_video', CATEGORIA='categori_video' where NOMBRE_VIDEO='nombre'")
    	return ModificarVideo.fetchall()
    	cursor.close()


    def BorrarVide(self, id_video):
        cursor.execute("DELETE from VIDEO WHERE ID_VIDEO='id_video'", true)
        BorrarVide.execute("DELETE from VIDEO WHERE ID_VIDEO='id_video'", true)
        conexion.commit()
        return BorrarVide.fetchall()
        cursor.close()

             
    	

    conexion.close()
   
if __name__ == '__main__':
    main()
   
