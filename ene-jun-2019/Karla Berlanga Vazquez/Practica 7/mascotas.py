import sqlite3

#Creamos la clase Mascota, que tiene como atributos: nombre, especie y edad
class Mascota():
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    def __str__(self):
        return "{} es un {} y tiene {} de edad".format(self.nombre, self.especie, self.edad)

    def __eq__(self, mascota):
        if mascota.nombre != self.nombre:
            return False

        if mascota.especie != self.especie:
            return False

        if mascota.edad != self.edad:
            return False

        return True

#Creamos nuestra clase de la base de datos en donde tendremos los metodos
#asociados a guardar, mostrar y eliminar mascota
class DataBase():
    #En el método constructor recibimos el nombre del archivo de nuestra base de datos
    def __init__(self, archivo):
        self.connection = sqlite3.connect(archivo)

    #En el metodo de guardar mascota, se recibe un objeto como tal de mascota y se insertan sus atributos en la base de datos
    def guardarMascota(self, mascota):
        cursor = self.connection.cursor()
        values = (mascota.nombre, mascota.especie, mascota.edad)
        cursor.execute("INSERT INTO mascotas (id,nombre, especie, edad) VALUES (null,?,?,?)", values)
        self.connection.commit()

    #En el metodo de mostrar las mascotas, se hace una consulta a la base de datos para traer todos los registros de la base de datos y guardarlos en una lista
    def getAllMascotas(self):
        cursor = self.connection.cursor()
        registros = cursor.execute("SELECT * FROM mascotas").fetchall()

        #Lista en la que se guardan las mascotas que nos regresa la consulta a la base de datos
        mascotas = []
        for registro in registros:
            mascotas.append(Mascota(registro[1], registro[2], registro[3]))
        return mascotas


def saveMascota(mascota, db):
    db.guardarMascota(mascota)

def showMascotas(db):
    mascotas = db.getAllMascotas()
    return mascotas

if __name__ == "__main__":
    #Creamos los objetos que se guardaran en la base de datos
    mascota1 = Mascota("Morita", "puerquito", "1 mes")
    mascota2 = Mascota("Mailo", "perro", "2 años")
    mascota3 = Mascota("Conchita", "perro", "1 año")
    mascota4 = Mascota("Tocino", "puerquito", "5 meses")

    db = DataBase("mascotas.db")
    #cursor = db.connection.cursor()
    #cursor.execute("CREATE TABLE mascotas (id INTEGER PRIMARY KEY AUTOINCREMENT,nombre TEXT, especie TEXT, edad TEXT)")

    #saveMascota(mascota1, db)
    #saveMascota(mascota2, db)
    #saveMascota(mascota3, db)
    #saveMascota(mascota4, db)
    print(*showMascotas(db), sep="\n")
