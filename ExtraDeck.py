from abc import ABC,abstractclassmethod
import DBCreate
from MainDeck import CardinDeck
import os
import sqlite3
import glob

class ExtraDeckInterface(ABC):
    @abstractclassmethod
    def insertarExtra(name):
        pass

    @abstractclassmethod
    def savecardtoExtra(CardObject):
        pass


    

def createlogExtra(nombremain,bi): #Genera un archivo txt para tomar como referencia del deck creado
            
    nombre = nombremain
    path = r"C:\Users\Eduardo-PC\Desktop\8vo Semestre\CPS\ProyectoFinalYGO\Deck\{}".format(nombre)
    if os.path.isfile(path):
        print('Ya hay un deck existente')
            
    else:
        
        Numero=len(glob.glob(r"C:\Users\Eduardo-PC\Desktop\8vo Semestre\CPS\ProyectoFinalYGO\Deck\*.txt"))
        
        if Numero == 1:
            bi.insertarExtra()
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

                    print("Se agrego la carta al MainDeck")
                    bi.savecardtoExtra(cord)
                if seleccion == 2:
                    print("No se agrego la carta!!!")

                if i > limit:
                    print("Alcanzaste el Maximo de cartas permitidas!!!")


        if Numero >=2:
            print("Solo se puede tener un deck para calcular!!!")
            
        
    


class ExtraDeck(ExtraDeckInterface):
    
    def __init__(self,databasename):
        self.dbname = databasename
        
        
      
    def insertarExtra(self):
        
        try:
            global conexion
            conexion = ""
            conexion = sqlite3.connect(self.dbname)
            cursor = conexion.cursor()
            print('Conectado')

            query = """CREATE TABLE IF NOT EXISTS Extradeck(
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
        
            print('Tabla creada con exito')
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
            cant = int(input("Escriba la cantidad de copias a agregar en el Extra Deck: "))
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
                    cartotaE = CardinDeck(row[0],row[1],row[2],row[3],row[4],cant)
                    return cartotaE
                    #print(cartota)
                    #MainDeck.savecardtoMain(cartota)
                cursor.close()

        except sqlite3.Error as error:
            print('Error con la conexion',error)

        finally:
            if(conexion):
                conexion.close()
    
    def savecardtoExtra(self,Card):

        try:
            conexion = sqlite3.connect(self.dbname)
            cursor = conexion.cursor()
            print('Conectado')
            query = """INSERT INTO ExtraDeck VALUES 
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



def InsertaExtraDeck():
    
    Maindeckname = input("\nEscriba el nombre del Main Deck a asignar Extra Deck: ")

    
    cosa = ExtraDeck("YugiohDB.db")
    createlogExtra('{}_Extra.txt'.format(Maindeckname),cosa)
