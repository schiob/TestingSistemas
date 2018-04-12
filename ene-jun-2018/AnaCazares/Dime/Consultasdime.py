from dime import *

class SQlite(AbstractSQlite):
   
#conectar con bd

conexion = sqlite3.connect('dime.db')
cursor = conexion.cursor()

def Guardar_VIDEOdime():
    cursor.execute("INSERT INTO VIDEO (ID_VIDEO ,NOMBRE_VIDEO, DURACION,CANAL,CATEGORIA,FECHA,LIKES,VISITAS,DESCRIPCION)\ VALUES ()")
    conexion.commit()
    print "se guardo correctamente"

def Buscar_VIDEOdime():
    cursor.execute("SELECT ID_VIDEO,NOMBRE_VIDEO,CANAL,VISITAS,FECHA,CATEGORIA")
    
    for i in cursor:
        print "ID_VIDEO=",i[0]
        print "NOMBRE_VIDEO=",i[1]
        print "CANAL=",i[2]
        print "VISITAS=",i[3]
        print "FECHA=",i[4]
        print "CATEGORIA=",i[5],"\n"

    print "OPERACION EXITOSA"

def Guardar_CATEGORIAdime():
    cursor.execute("INSERT INTO VIDEO (ID_VIDEO ,NOMBRE_VIDEO, DURACION,CANAL,CATEGORIA,FECHA,LIKES,VISITAS,DESCRIPCION)\ VALUES ()")
    conexion.commit()
    print "se guardo correctamente"

def Buscar_VIDEOdime():
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



    def Borrar_VIDEOdime():
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
