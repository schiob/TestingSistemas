from abc import ABC,abstractclassmethod

class BuildDecksInterfaces(ABC):
    @abstractclassmethod
    def createTableMain():
        pass
    
    @abstractclassmethod
    def insertarinMain():
        pass 

    @abstractclassmethod
    def VisualizarinMain():
        pass

    @abstractclassmethod    
    def insertarinExtra():
        pass 
        

    @abstractclassmethod
    def VisualizarinExtra():
        pass 
    
    @abstractclassmethod
    def insertarinSide():
        pass 

    @abstractclassmethod
    def VisualizarinSide():
        pass



class BuildDecks(BuildDecksInterfaces):

    def createTableMain():
        try:
            conexion = sqlite3.connect('YugiohDB.db')
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

    
    def insertarinMain():
        new = "ALGO"
        
        return new
    
    
    def VisualizarinMain():
        pass

       
    def insertarinExtra():
        pass 
        

    
    def VisualizarinExtra():
        pass 
    
   
    def insertarinSide():
        pass 

    
    def VisualizarinSide():
        pass


def llamada():
    
    print(BuildDecks.insertarinMain())