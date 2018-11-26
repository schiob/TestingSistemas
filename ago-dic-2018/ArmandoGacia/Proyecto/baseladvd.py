import sqlite3
from Tweet import *

class basedb(Abstractbase):
    def __init__(self):
        self.conn=sqlite3.connect('social_data.db')
        self.cursor = self.conn.cursor()

    def insert_db(self,Tweeti):
        t = (Tweeti.user_id,Tweeti.handle,Tweeti.lugar,Tweeti.verificado,Tweeti.followers,Tweeti.numtweets,Tweeti.friends,Tweeti.description,Tweeti.lenguaje,Tweeti.profile,Tweeti.Ranking,Tweeti.Categoria,Tweeti.Victorias,Tweeti.Derrotas)
        self.cursor.execute(''' INSERT INTO tabla VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',t)
        self.conn.commit()
        return 'Datos Insertados ({}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {})'.format(Tweeti.user_id,Tweeti.handle,Tweeti.lugar,Tweeti.verificado,Tweeti.followers,Tweeti.numtweets,Tweeti.friends,Tweeti.description,Tweeti.lenguaje,Tweeti.profile,Tweeti.Ranking,Tweeti.Categoria,Tweeti.Victorias,Tweeti.Derrotas)

    def deleteUsuario(self,handle):
        self.cursor.execute("DELETE FROM tabla WHERE Nombre = ?",(handle,))
        self.conn.commit()
        return True

    def updateUsuario(self,handle,Ranking,Categoria,Victorias,Derrotas):
        self.cursor.execute("UPDATE tabla SET Ranking= ?,Categoria= ?,Victorias= ?,Derrotas= ? WHERE Nombre= ?",\
        (Ranking,Categoria,Victorias,Derrotas,handle,))
        self.conn.commit()
        print('El ususario: {} ,fue actualizado.'.format(handle))
        return True
    def selectUsuario(self,handle):
            usr = handle
            self.cursor.execute("SELECT * FROM tabla WHERE Nombre = ?",(usr,))
            datos = self.cursor.fetchone()
            if datos:
                return('ID: {} \nNombre: {} \nLugar: {} \nVerificado: {} \nFollowers: {} \nTweets y Retweets: {} \nFollowing: {} \nDescipcion: {} \nLenguaje: {} \nFoto: {} \nRanking: {} \nCategoria: {} \nVictorias: {} \nDerrotas: {}'.\
                format(datos[0],datos[1],datos[2],datos[3],datos[4],datos[5],datos[6],datos[7],datos[8],datos[9],datos[10],datos[11],datos[12],datos[13]))
            else:
                return('El usuario: {} ,no existe'.format(usr))
if __name__ == '__main__':
    db=basedb()
