_AnaCazares_ = u"dime"

import sqlite3
#conectar con bd

conexion = sqlite3.connect('dime.db')
cursor = conexion.cursor()


#crear tabla VIDEO
cursor.execute('''CREATE TABLE VIDEO
                (ID_VIDEO TEXT NOT NULL,
                NOMBRE_VIDEO TEXT NOT NULL,
                DURACION INTEGER NOT NULL,
                CANAL TEXT NOT NULL,
                CATEGORIAS TEXT NOT NULL,
                FECHA TEXT NOT NULL,
                LIKES INTEGER NOT NULL,
                VISITAS INTEGER NOT NULL,
                DESCRIPCION TEXT NOT NULL)''')

#crear tabla CATEGORIA
cursor.execute('''CREATE TABLE CATEGORIA
                (ID_CATEGORIA TEXT NOT NULL,
                NOMBRE_CATEGORIA TEXT NOT NULL)''')


#cerramos conexion
conexion.close()