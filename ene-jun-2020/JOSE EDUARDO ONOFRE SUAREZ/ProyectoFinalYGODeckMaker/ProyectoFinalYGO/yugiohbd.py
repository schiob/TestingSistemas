import sqlite3
##Crear Base o conectarse
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

#Crear Tabla Card

    try:
        conexion = sqlite3.connect('YugiohDB.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = """CREATE TABLE IF NOT EXISTS Cards(
                Id INTEGER PRIMARY KEY,
                Name TEXT NOT NULL,
                Type TEXT,
                Desc TEXT,
                Atk TEXT,
                Def TEXT,
                Level TEXT,
                Race TEXT,
                Attribute TEXT,
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

def insertarC(Card):
    try:
        conexion = sqlite3.connect('YugiohDB.db')
        cursor = conexion.cursor()
        print('Conectado')
        query = """INSERT INTO Cards VALUES 
                ('{}', '{}', '{}', '{}', '{}','{}','{}','{}','{}','{}')""".format(Cards._id, Cards._name, Cards._types, Cards._desc, Cards._atk, Cards._defs, Cards._level, Cards._attribute, Cards._price)
        resultado = cursor.execute(query)
        conexion.commit()
        print('Valor Insertado Correctamente', resultado)
        cursor.close()

    except sqlite3.Error as error:
            print('Error con la conexion',error)

    finally:
        if(conexion):
            conexion.close()
# Mostrar datos 
def Visualizar():
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
            print('Id: {}\nName: {}\nType: {}\nDesc: {}\nAtk: {}\nDef: {}\nLevel: {}\nRace: {}\nAttribute: {}\nPrice: {}' .format(*row))
        
        cursor.close()

    except sqlite3.Error as error:
        print('Error con la conexion',error)

    finally:
        if(conexion):
            conexion.close()

#Crear Tabla Card

    try:
        conexion = sqlite3.connect('YugiohDB.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = """CREATE TABLE IF NOT EXISTS MainDeck(
                Id INTEGER PRIMARY KEY,
                Name TEXT NOT NULL,
                NdC INTEGER,
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

def insertarMain(Card):
    try:
        conexion = sqlite3.connect('YugiohDB.db')
        cursor = conexion.cursor()
        print('Conectado')
        query = """INSERT INTO MainDeck VALUES 
                ('{}', '{}', '{}', '{}')""".format(MainDeck._id,MainDeck._name,MainDeck._NdC,MainDeck._price)
        resultado = cursor.execute(query)
        conexion.commit()
        print('Valor Insertado Correctamente', resultado)
        cursor.close()

    except sqlite3.Error as error:
            print('Error con la conexion',error)

    finally:
        if(conexion):
            conexion.close()
# Mostrar datos 
def Visualizar1():
    try:
        conexion = sqlite3.connect('YugiohDB.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = 'SELECT * FROM MainDeck;'
        cursor.execute(query)
        rows = cursor.fetchall()
        print('Total de registros: ', len(rows))

        print('------------Registros-------------')

        for row in rows:
            print('Id: {}\nName: {}\nNdC: {}\nPrecio: {}' .format(*row))
        
        cursor.close()

    except sqlite3.Error as error:
        print('Error con la conexion',error)

    finally:
        if(conexion):
            conexion.close()

#Crear Tabla Card

    try:
        conexion = sqlite3.connect('YugiohDB.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = """CREATE TABLE IF NOT EXISTS ExtraDeck(
                Id INTEGER PRIMARY KEY,
                Name TEXT NOT NULL,
                NdC INTEGER,
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

def insertarExtra(Card):
    try:
        conexion = sqlite3.connect('YugiohDB.db')
        cursor = conexion.cursor()
        print('Conectado')
        query = """INSERT INTO ExtraDeck VALUES 
                ('{}', '{}', '{}', '{}')""".format(ExtraDeck._id, ExtraDeck._name, ExtraDeck._NdC, ExtraDeck._price)
        resultado = cursor.execute(query)
        conexion.commit()
        print('Valor Insertado Correctamente', resultado)
        cursor.close()

    except sqlite3.Error as error:
            print('Error con la conexion',error)

    finally:
        if(conexion):
            conexion.close()
# Mostrar datos 
def Visualizar2():
    try:
        conexion = sqlite3.connect('YugiohDB.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = 'SELECT * FROM ExtraDeck;'
        cursor.execute(query)
        rows = cursor.fetchall()
        print('Total de registros: ', len(rows))

        print('------------Registros-------------')

        for row in rows:
            print('Id: {}\nName: {}\nNdC: {}\nPrecio: {}' .format(*row))
        
        cursor.close()

    except sqlite3.Error as error:
        print('Error con la conexion',error)

    finally:
        if(conexion):
            conexion.close()

#Crear Tabla Card

    try:
        conexion = sqlite3.connect('YugiohDB.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = """CREATE TABLE IF NOT EXISTS SideDeck(
                Id INTEGER PRIMARY KEY,
                Name TEXT NOT NULL,
                NdC INTEGER,
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

def insertarSide(Card):
    try:
        conexion = sqlite3.connect('YugiohDB.db')
        cursor = conexion.cursor()
        print('Conectado')
        query = """INSERT INTO SideDeck VALUES 
                ('{}', '{}', '{}', '{}')""".format(SideDeck._id, SideDeck._name, SideDeck._NdC, SideDeck._price)
        resultado = cursor.execute(query)
        conexion.commit()
        print('Valor Insertado Correctamente', resultado)
        cursor.close()

    except sqlite3.Error as error:
            print('Error con la conexion',error)

    finally:
        if(conexion):
            conexion.close()
# Mostrar datos 
def Visualizar3():
    try:
        conexion = sqlite3.connect('YugiohDB.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = 'SELECT * FROM SideDeck;'
        cursor.execute(query)
        rows = cursor.fetchall()
        print('Total de registros: ', len(rows))

        print('------------Registros-------------')

        for row in rows:
            print('Id: {}\nName: {}\nNdC: {}\nPrecio: {}' .format(*row))
        
        cursor.close()

    except sqlite3.Error as error:
        print('Error con la conexion',error)

    finally:
        if(conexion):
            conexion.close()