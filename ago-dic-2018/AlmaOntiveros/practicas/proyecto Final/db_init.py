#base de datos con sqlite3

import sqlite3

def main():
    conexion = sqlite3.connect('Youtube.db')
    cursor = conexion.cursor()

    #crear tabla VIDEO

    cursor.execute('''CREATE TABLE VIDEO
                    (ID integer PRIMARY KEY,
                    NOMBRE TEXT NOT NULL,
                    DURACION TEXT NOT NULL,
                    CANAL TEXT NOT NULL,
                    FECHA TEXT NOT NULL,
                    LIKES INTEGER NOT NULL,
                    VISTAS INTEGER NOT NULL,
                    DESCRIPCION TEXT NOT NULL,
                    Compartidas INTEGER NOT NULL
                )''')




if __name__ == "__main__":
    main()
