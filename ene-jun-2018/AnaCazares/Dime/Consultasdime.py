from dime import *

class SQlite(AbstractSQlite):
   
	#conectar con bd

	conexion = sqlite3.connect('dime.db')
	cursor = conexion.cursor()

	def Guardar_VIDEOdime(self, id_video,nombre,duracion,canal_video,categoria_video,fecha_video,likes,visitas_video,descripcion):
    	guardar_video=cursor.execute("INSERT INTO VIDEO VALUES (id_video,nombre,duracion,canal_video,categoria_video,fecha_video,likes,visitas_video,descripcion)")    	conexion.commit()
    	return guardar_video

	def MostrarLista(self, id):
    	mostrar_lista=cursor.execute("SELECT * from VIDEO")
    	conexion.commit()
    	return mostrar_lista
       	

	def ModificarVideo(self, id_video, nombre, canal_video,visitas_video,fecha_video,categori_video ):
    	modificar_video=cursor.execute("UPDATE VIDEO SET ID_VIDEO='id_video', NOMBRE_VIDEO='nombre', CANAL='canal_video', VISITAS=visitas_video, FECHA='fecha_video', CATEGORIA='categori_video' where NOMBRE_VIDEO='nombre'")
    	conexion.commit()
    	return modificar_video

	def MostrarVideo(self, id_video):
    	mostrar_video = cursor.execute("SELECT * from VIDEO where ID_VIDEO='id_video'")
    	conexion.commit()
    	return mostrar_video
    
   

    	def BorrarVide(self, id_video):
        	borrar_videocursor.execute("DELETE from VIDEO WHERE ID_VIDEO='id_video'", true)
        	conexion.commit()
        	return borrar_videocursor

             
    	

    conexion.close()
   
if __name__ == '__main__':
    main()
    """conexion = SQlite()
    	conexion.agregar("id")

    idvideo = conexion SQlite
    	idvideo.ID_VIDEO("id")

    nombre =conexion SQlite
    	nombre.NOMBRE_VIDEO("nombre")

    conexion = SQlite()
    	conexion.agregar("nombre")

    duracion = conexion SQlite
    	duracion.DURACION("likes")

    conexion = SQlite()
   		conexion.agregar("duracion")

    canal =conexion SQlite
    	canal.CANAL("canal")

    conexion = SQlite()
   		conexion.agregar("canal")
  
    categoria= conexion SQlite
    	categoria.CATEGORIA("categoria")

    conexion = SQlite()
    	conexion.agregar("categoria")

    visitas = conexion SQlite
    	visitas.VISITAS("visitas")

    conexion = SQlite()
    	conexion.agregar("visitas")

    fechas = conexion SQlite
    	fechas.FECHA("fecha")

    conexion = SQlite()
    	conexion.agregar("fecha")

    descripcion= conexion SQlite
    	descripcion.DESCRIPCION("descripcion")

    conexion = SQlite()
    conexion.agregar("DESCRIPCION")"""
