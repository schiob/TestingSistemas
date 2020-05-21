import sqlite3
import Card

class dataBase():

    def CreateDatabase(self):
        try:
            conexion = sqlite3.connect('YugiohDB.db')
            cursor = conexion.cursor()
            print('Conectado a SQLite')

            query = 'SELECT sqlite_version();'
            cursor.execute(query)
            rows = cursor.fetchall()
            print('Version de SQLite: ', rows)
            cursor.close()
        except sqlite3.Error as error:
            print('Error con la conexión!', error)
        finally:
            if (conexion):
                conexion.close()
                print('Conexión a SQLite cerrada\n')
    

    #Crear Tabla Card (De API a DB)
    def CardTable(self):
        try:
            conexion = sqlite3.connect('YugiohDB.db')
            cursor = conexion.cursor()
            print('Conectado')

            query = """CREATE TABLE IF NOT EXISTS Cards(
                    Id INTEGER PRIMARY KEY,
                    Name TEXT NOT NULL,
                    Type TEXT,
                    Desc TEXT,
                    Price FLOAT
                
                    );"""
            cursor.execute(query)
            conexion.commit()
            print('Tabla creada con exito')
            cursor.close()

        except sqlite3.Error as error:
            print('Error con la conexion',error)

        finally:
            if(conexion):
                conexion.close()

    # Inserción de carta desde API a la tabla de DB
    def insertarC(self,Card):
        try:
            conexion = sqlite3.connect('YugiohDB.db')
            cursor = conexion.cursor()
            print('Conectado')
            query = """INSERT INTO Cards VALUES 
                    ('{}', '{}', '{}', '{}', '{}')""".format(Card._Id, Card._Name, Card._Type, Card._Desc, Card._Price)
            resultado = cursor.execute(query)
            conexion.commit()
            print('Valor Insertado Correctamente', resultado)
            cursor.close()

        except sqlite3.Error as error:
                print('Error con la conexion',error)

        finally:
            if(conexion):
                conexion.close()

    def Visualizar(self):
        try:
            conexion = sqlite3.connect('YugiohDB.db')
            cursor = conexion.cursor()
            print('Conectado')

            query = 'SELECT * FROM Cards;'
            cursor.execute(query)
            rows = cursor.fetchall()
            print('Total de registros: ', len(rows))

            print('------------Registros-------------')

            for row in rows:
                print('Id: {}\nName: {}\nType: {}\nDesc: {}\nPrice: {}' .format(*row))
                print("---------------------------------------------------------------")
        
            cursor.close()

        except sqlite3.Error as error:
            print('Error con la conexion',error)

        finally:
            if(conexion):
                conexion.close()

if __name__ == "__main__":
    x = dataBase()

    x.CreateDatabase()
    x.Visualizar()
    
    ## Agregar Tabla Deck ##
    ## Insertar en Deck ##


    #########################


    ## Agregar Tabla ExtraDeck ##
    ## Insertar en ExtraDeck ##


    #########################


    ## Agregar Tabla SideDeck ##
    ## Insertar en SideDeck ##


    #########################

    
    