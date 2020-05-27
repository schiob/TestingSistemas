from abc import ABC,abstractclassmethod
import DBCreate
from MainDeck import CardinDeck
import os
import sqlite3
import glob

class SideDeckInterface(ABC):
    @abstractclassmethod
    def insertarSide(name):
        pass

    @abstractclassmethod
    def savecardtoSide(CardObject):
        pass


    

def createlogSide(nombremain,bi): #Genera un archivo txt para tomar como referencia del deck creado
            
    nombre = nombremain
    path = r"C:\Users\Eduardo-PC\Desktop\8vo Semestre\CPS\ProyectoFinalYGO\Deck\{}".format(nombre)
    if os.path.isfile(path):
        print('Ya hay un deck existente')
            
    else:
        
        Numero=len(glob.glob(r"C:\Users\Eduardo-PC\Desktop\8vo Semestre\CPS\ProyectoFinalYGO\Deck\*.txt"))
        
        if Numero >= 1 and Numero <=2:
            bi.insertarSide()
            file = open(r"C:\Users\Eduardo-PC\Desktop\8vo Semestre\CPS\ProyectoFinalYGO\Deck\{}".format(nombre), "w")
            file.write(nombre + os.linesep)
            file.close()
            
            limit = 3 # Tamaño del deck
            for i in range(0,limit):
                cartita = input("Escriba el nombre de la carta a agregar:")
                cord = bi.searchcardinDB(cartita)
                op = False
                seleccion = int(input("\nEsta seguro de agregar esta carta? - 1 = SI, 2 = NO "))

                if seleccion == 1:

                    print("Se agrego la carta al SideDeck")
                    bi.savecardtoSide(cord)
                if seleccion == 2:
                    print("No se agrego la carta!!!")

                if i > limit:
                    print("Alcanzaste el Maximo de cartas permitidas!!!")


        if Numero >2:
            print("Solo se puede tener un deck para calcular!!!")
            
        
    


class SideDeck(SideDeckInterface):
    
    def __init__(self,databasename):
        self.dbname = databasename
        
        
      
    def insertarSide(self):
        
        try:
            global conexion
            conexion = ""
            conexion = sqlite3.connect(self.dbname)
            cursor = conexion.cursor()
            print('Conectado')

            query = """CREATE TABLE IF NOT EXISTS SideDeck(
                    Id INTEGER PRIMARY KEY,
                    Name TEXT NOT NULL,
                    Type TEXT,
                    Desc TEXT,
                    Price FLOAT,
                    Quantity INTEGER
                
                    );"""
            cursor.execute(query)
            conexion.commit()
            
            cursor.close()
        
            return('Tabla SideDeck creada con exito')
        except sqlite3.Error as error:
            return('Error con la conexion',error)

        finally:
            if(conexion):
                conexion.close()
    
    def searchcardinDB(self,cardtoadd):
        try:
            conexion = sqlite3.connect('YugiohDB.db')
            cursor = conexion.cursor()
            print('Conectado')
            cant = int(input("Escriba la cantidad de copias a agregar en el Side Deck: "))
            if cant <=3:
                query = "SELECT * FROM Cards where Name = '{}';".format(cardtoadd)
                cursor.execute(query)
                rows = cursor.fetchall()
                #print('Total de registros: ', len(rows))

                print('------------Registros-------------')

                for row in rows:
                    print("-------------------------INFORMACION DE LA CARTA------------------------")
                    print('Id: {}\nName: {}\nType: {}\nDesc: {}\nPrice: {}' .format(*row))
                    print("---------------------------------------------------------------")
                    cartotaS = CardinDeck(row[0],row[1],row[2],row[3],row[4],cant)
                    return cartotaS
                    #print(cartota)
                    #MainDeck.savecardtoMain(cartota)
                cursor.close()

        except sqlite3.Error as error:
            print('Error con la conexion',error)

        finally:
            if(conexion):
                conexion.close()
    
    def savecardtoSide(self,Card):

        try:
            conexion = sqlite3.connect(self.dbname)
            cursor = conexion.cursor()
            print('Conectado')
            query = """INSERT INTO SideDeck VALUES 
                    ('{}', '{}', '{}', '{}', '{}', '{}')""".format(Card._Id, Card._Name, Card._Type, Card._Desc, Card._Price, Card._Quantity)
            resultado = cursor.execute(query)
            conexion.commit()
            print('Valor Insertado Correctamente', resultado)
            cursor.close()

        except sqlite3.Error as error:
                print('Error con la conexion',error)

        finally:
            if(conexion):
                conexion.close()


def tableSideDeck():

    side =  SideDeck("YugiohDB.db")
    
    res = side.insertarSide()
    return res


def InsertaSideDeck():
    
    Maindeckname = input("\nEscriba el nombre del Main Deck a asignar Side Deck: ")

    
    cosa = SideDeck("YugiohDB.db")
    createlogSide('{}_Side.txt'.format(Maindeckname),cosa)

if __name__ == "__main__":
    
    print(tableSideDeck())