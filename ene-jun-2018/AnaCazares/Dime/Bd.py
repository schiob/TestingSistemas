#base de datos con sqlite3
_AnaCazares_ = u"Proyecto"

import sqlite3

conexion = sqlite3.connect('proyecto.db')
cursor = conexion.cursor()

#crear tabla VIDEO
cursor.execute('''CREATE TABLE VIDEO
                (ID TEXT NOT NULL,
                NOMBRE TEXT NOT NULL,
                DURACION INTEGER NOT NULL,
                CANAL TEXT NOT NULL,
                CATEGORIAS TEXT NOT NULL,
                FECHA TEXT NOT NULL,
                LIKES INTEGER NOT NULL,
                VISTAS INTEGER NOT NULL,
                DESCRIPCION TEXT NOT NULL)''')

#crear tabla CATEGORIA
cursor.execute('''CREATE TABLE CATEGORIA
                (ID TEXT NOT NULL,
                NOMBRE TEXT NOT NULL)''')

conexion.close()
