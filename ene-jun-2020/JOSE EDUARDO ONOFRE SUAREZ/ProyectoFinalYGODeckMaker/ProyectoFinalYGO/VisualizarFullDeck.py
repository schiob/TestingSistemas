import sqlite3
import MainDeck, ExtraDeck, SideDeck
from abc import ABC, abstractclassmethod

class VisualizarDeckInterface(ABC):

    def visualizarMainDeck(deckname):
        pass

    def visualizarExtraDeck(deckname):
        pass

    def visualizarSideDeck(deckname):
        pass




class VisualizarDeckFull(VisualizarDeckInterface):

    def __init__(self,dbname):
        self._database = dbname

    
    def visualizarMainDeck(self,deckname):

        try:
            conexion = sqlite3.connect(self._database)
            cursor = conexion.cursor()
            print('Conectado')
            
            query = "SELECT * FROM {};".format(deckname)
            cursor.execute(query)
            rows = cursor.fetchall()
            

            print('------------CARTAS EN MAIN DECK-------------')

            for row in rows:
                print("-------------------------INFORMACION DE LA CARTA------------------------")
                print('Id: {}\nName: {}\nType: {}\nDesc: {}\nPrice: {}' .format(*row))
                print("---------------------------------------------------------------")
                    
            cursor.close()
            
        except sqlite3.Error as error:
            print('Error con la conexion',error)

        finally:
            if(conexion):
                conexion.close()

    
    def visualizarExtraDeck(self,deckname):

        try:
            conexion = sqlite3.connect(self._database)
            cursor = conexion.cursor()
            print('Conectado')
            
            query = "SELECT * FROM {};".format(deckname)
            cursor.execute(query)
            rows = cursor.fetchall()
            

            print('\n------------CARTAS EN EXTRADECK-------------')

            for row in rows:
                print("-------------------------INFORMACION DE LA CARTA------------------------")
                print('Id: {}\nName: {}\nType: {}\nDesc: {}\nPrice: {}' .format(*row))
                print("---------------------------------------------------------------")
                    
            cursor.close()
            
        except sqlite3.Error as error:
            print('Error con la conexion',error)

        finally:
            if(conexion):
                conexion.close()
    

    def visualizarSideDeck(self,deckname):

        try:
            conexion = sqlite3.connect(self._database)
            cursor = conexion.cursor()
            print('Conectado')
            
            query = "SELECT * FROM {};".format(deckname)
            cursor.execute(query)
            rows = cursor.fetchall()
            

            print('\n------------CARTAS EN SIDEDECK-------------')

            for row in rows:
                print("-------------------------INFORMACION DE LA CARTA------------------------")
                print('Id: {}\nName: {}\nType: {}\nDesc: {}\nPrice: {}' .format(*row))
                print("---------------------------------------------------------------")
                    
            cursor.close()
            
        except sqlite3.Error as error:
            print('Error con la conexion',error)

        finally:
            if(conexion):
                conexion.close()
    


def RetrieveAll():
    
    try:
        DataB = 'YugiohDB.db'

        MainDeck = VisualizarDeckFull(DataB)
        MainDeck.visualizarMainDeck('MainDeck')

        ExtraDeck = VisualizarDeckFull(DataB)
        ExtraDeck.visualizarExtraDeck('ExtraDeck')

        SideDeck = VisualizarDeckFull(DataB)
        SideDeck.visualizarSideDeck('SideDeck')
    except:
        print("Al parecer no hay un Deck Existente")




