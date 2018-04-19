from dime import *

class SQlite(AbstractSQlite):
   
#conectar con bd

conexion = sqlite3.connect('dime.db')
cursor = conexion.cursor()

def Guardar_VIDEOdime(self, video):
    cursor.execute("INSERT INTO VIDEO (ID_VIDEO ,NOMBRE_VIDEO, DURACION,CANAL,CATEGORIA,FECHA,LIKES,VISITAS,DESCRIPCION)\ VALUES (https://www.youtube.com/watch?v=X9A1Ny6B310,video,123,youtube,musica,12/02/2018,344,34,video)")
    conexion.commit()
    print "se guardo correctamente"

def MostrarLista(self, id):
    cursor.execute("SELECT ID_VIDEO,NOMBRE_VIDEO,CANAL,VISITAS,FECHA,CATEGORIA")
    
    for i in cursor:
        print "ID_VIDEO=",i[0]
        print "NOMBRE_VIDEO=",i[1]
        print "CANAL=",i[2]
        print "VISITAS=",i[3]
        print "FECHA=",i[4]
        print "CATEGORIA=",i[5],"\n"

    print "OPERACION EXITOSA"

def Categoria(self, id, nombre):
    cursor.execute("INSERT INTO CATEGORIA (ID_CATEGORIA, NOMBRE_CATEGORIA)\ VALUES (1,musica)")
    conexion.commit()
    print "se guardo correctamente"

def MostrarVideo(self, id):
    cursor.execute("SELECT ID_VIDEO,NOMBRE_VIDEO,CANAL,VISITAS,FECHA,CATEGORIA")
    
   ID_VIDEO=INT(input("INSERTE EL ID del VIDEO A ELIMINAR :"))
   Buscar_VIDEOdime="SELECT VIDEOdime.ID_VIDEO from  ID_VIDEO=ID_VIDEO"
   cursor.execute(Buscar_VIDEOdime)
   busqueda_completa=cursor.fetchone()
   if len(busqueda_completa)>0:
    print("ID_VIDEO encontrado:{}".format(busqueda_completa[0]))
     print("NOMBRE_VIDEO{}".format(busqueda_completa[1]))
        print("DURACION{}".format(busqueda_completa[2]))
        print("CANAL{}".format(busqueda_completa[3]))
        print("CATEGORIA{}".format(busqueda_completa[4]))
        print("FECHA{}".format(busqueda_completa[5]))
        print("LIKES{}".format(busqueda_completa[6]))
        print("VISITAS{}".format(busqueda_completa[7]))
        print("DESCRIPCION{}".format(busqueda_completa[8]))

    else:
            print ("no existe")

    def BorrarVide(self, id):
        cursor.execute("DELET from VIDEOdime WHERE ID_VIDEO=0")
        conexion.commit()
        print "Borrado",conexion.commit.total_changes
    cursor.execute("SELECT ID_VIDEO,NOMBRE_VIDEO,CANAL,VISITAS,FECHA,CATEGORIA")
    
    for i in cursor:
        print "ID_VIDEO=",i[0]
        print "NOMBRE_VIDEO=",i[1]
        print "CANAL=",i[2]
        print "VISITAS=",i[3]
        print "FECHA=",i[4]
        print "CATEGORIA=",i[5],"\n"

    print "OPERACION EXITOSA"


    conexion.close()
   
if __name__ == '__main__':
    main()
    conexion = SQlite()
    conexion.agregar("ID_VIDEO")

    idvideo = conexion SQlite
    idvideo.ID_VIDEO("https://www.youtube.com/watch?v=X9A1Ny6B310")

    video =conexion SQlite
    video.NOMBRE_VIDEO("Video")

    conexion = SQlite()
    conexion.agregar("NOMBRE_VIDEO")

    duracion = conexion SQlite
    duracion.DURACION("1123")

    conexion = SQlite()
    conexion.agregar("DURACION")

    canal =conexion SQlite
    canal.CANAL("werwber")

    conexion = SQlite()
    conexion.agregar("CANAL")
  
    categoria= conexion SQlite
    categoria.CATEGORIA("musica")

    conexion = SQlite()
    conexion.agregar("CATEGORIA")

    visitas = conexion SQlite
    visitas.VISITAS("1234")

    conexion = SQlite()
    conexion.agregar("VISITAS")

    fechas = conexion SQlite
    fechas.FECHA("12/02/2018")

    conexion = SQlite()
    conexion.agregar("FECHA")

    descripcion= conexion SQlite
    descripcion.DESCRIPCION("video youtube")

    conexion = SQlite()
    conexion.agregar("DESCRIPCION")
