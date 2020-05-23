import sqlite3
import Card
from abc import ABC,abstractclassmethod



class ApiBD(ABC): # Clase Abstracta para la Interface de las funciones que trabajan con la info de la API hacia la Base de Datos
    @abstractclassmethod
    def CreateDatabase():
        pass

    def CreateTable():
        pass

    def insertarC():
        pass

    def Visualizar():
        pass
    



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
            count = 0
            for row in rows:
                print('Id: {}\nName: {}\nType: {}\nDesc: {}\nPrice: {}' .format(*row))
                print("---------------------------------------------------------------")
                count+=1
            cursor.close()
            return count
        except sqlite3.Error as error:
            print('Error con la conexion',error)

        finally:
            if(conexion):
                conexion.close()
    
if __name__ == "__main__":
    
    a = dataBase()

    a.Visualizar()