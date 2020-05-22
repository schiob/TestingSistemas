from abc import ABC,abstractclassmethod
import DBCreate
import Card
import os
import sqlite3
import glob

class MainDeckInterface(ABC):
    @abstractclassmethod
    def insertarMain(name):
        pass

    @abstractclassmethod
    def savecardtoMain(CardObject):
        pass


    

def createlog(nombremain,bi): #Genera un archivo txt para tomar como referencia del deck creado
            
    nombre = nombremain
    path = r"C:\Users\Eduardo-PC\Desktop\8vo Semestre\CPS\ProyectoFinalYGO\Deck\{}".format(nombre)
    if os.path.isfile(path):
        print('Ya hay un deck existente')
            
    else:
        
        Numero=len(glob.glob(r"C:\Users\Eduardo-PC\Desktop\8vo Semestre\CPS\ProyectoFinalYGO\Deck\*.txt"))
        
        if Numero == 0:
            bi.insertarMain()
            file = open(r"C:\Users\Eduardo-PC\Desktop\8vo Semestre\CPS\ProyectoFinalYGO\Deck\{}".format(nombre), "w")
            file.write(nombre + os.linesep)
            file.close()
            
            limit = 3
            for i in range(0,limit):
                cartita = input("Escriba el nombre de la carta a agregar:")
                cord = bi.searchcardinDB(cartita)
                op = False
                seleccion = int(input("\nEsta seguro de agregar esta carta? - 1 = SI, 2 = NO "))

                if seleccion == 1:

                    print("Se agrego la carta al MainDeck")
                    bi.savecardtoMain(cord)
                if seleccion == 2:
                    print("No se agrego la carta!!!")


        if Numero !=0:
            print("Solo se puede tener un deck para calcular!!!")
            
        
    


class MainDeck(MainDeckInterface):
    
    def __init__(self,databasename):
        self.dbname = databasename
        
        
      
    def insertarMain(self):
        
        try:
            global conexion
            conexion = ""
            conexion = sqlite3.connect(self.dbname)
            cursor = conexion.cursor()
            print('Conectado')

            query = """CREATE TABLE IF NOT EXISTS Maindeck(
                    Id INTEGER PRIMARY KEY,
                    Name TEXT NOT NULL,
                    Type TEXT,
                    Desc TEXT,
                    Price FLOAT
                
                    );"""
            cursor.execute(query)
            conexion.commit()
            
            cursor.close()
        
            return ('Tabla creada con exito')
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

            query = "SELECT * FROM Cards where Name = '{}';".format(cardtoadd)
            cursor.execute(query)
            rows = cursor.fetchall()
            #print('Total de registros: ', len(rows))

            print('------------Registros-------------')

            for row in rows:
                print("-------------------------INFORMACION DE LA CARTA------------------------")
                print('Id: {}\nName: {}\nType: {}\nDesc: {}\nPrice: {}' .format(*row))
                print("---------------------------------------------------------------")
                cartota = Card.Card(row[0],row[1],row[2],row[3],row[4])
                return cartota
                #print(cartota)
                #MainDeck.savecardtoMain(cartota)
            cursor.close()

        except sqlite3.Error as error:
            print('Error con la conexion',error)

        finally:
            if(conexion):
                conexion.close()
    
    def savecardtoMain(self,Card):

        try:
            conexion = sqlite3.connect(self.dbname)
            cursor = conexion.cursor()
            print('Conectado')
            query = """INSERT INTO MainDeck VALUES 
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

    


def InsertaMainDeck():
    
    deckname = input("\nEscriba el nombre de su deck: ")

    
    cosa = MainDeck("YugiohDB.db")
    createlog('{}.txt'.format(deckname),cosa)

#if __name__ == "__main__":
    
#    InsertaMainDeck()