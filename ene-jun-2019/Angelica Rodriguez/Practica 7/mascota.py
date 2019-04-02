import sqlite3

# Clase para crear mascotas
class Mascota():
    # constructor con los atributos de la mascota
    def __init__(self, nombre, especie, edad, peso, color, genero, comidaFav):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.peso = peso
        self.color = color
        self.genero = genero
        self.comidaFav = comidaFav

    # imprime todos los datos de la mascota
    def __str__(self):
        return """Nombre: {}\nEspecie: {}\nEdad: {}\nPeso: {}\nColor: {}\nGénero: {}\nComida favorita: {}\n""".format(
        self.nombre, self.especie, self.edad, self.peso, self.color, self.genero, self.comidaFav)

    # compara cada atributo de la mascota para saber si son iguales
    def __eq__(self, mascota):
        if mascota.nombre != self.nombre:
            return False

        if mascota.especie != self.especie:
            return False

        if mascota.edad != self.edad:
            return False

        if mascota.peso != self.peso:
            return False

        if mascota.color != self.color:
            return False

        if mascota.genero != self.genero:
            return False

        if mascota.comidaFav != self.comidaFav:
            return False
        return True

class sqlite():
    # constructor para crear el archivo donde irá la base de datos
    def __init__(self, archivo):
        self.conn = sqlite3.connect(archivo)

    # método para guardar mascotas
    def guardar(self, mascota):
        cur = self.conn.cursor()
        cur.execute("""INSERT INTO MASCOTAS (nombre, especie, edad, peso,
        color, genero, comidaFav) VALUES ('{}', '{}', {}, {}, '{}', '{}',
        '{}')""".format(mascota.nombre, mascota.especie, mascota.edad,
        mascota.peso, mascota.color, mascota.genero, mascota.comidaFav))
        self.conn.commit()

    # función para mostrar todas las mascotas guardadas en la base de datos
    def getAllMascotas(self):
        cur = self.conn.cursor()
        mascotas = cur.execute("SELECT * FROM MASCOTAS").fetchall()
        listaMascotas = []
        for mascota in mascotas:
            listaMascotas.append(Mascota(mascota[1],mascota[2],mascota[3],mascota[4],mascota[5],mascota[6],mascota[7]))
        return listaMascotas

# método para guardar mascotas
def saveMascota(mascota, db):
    db.guardar(mascota)

# método para mostrar todas las mascotas
def showMascotas(db):
    mascotas = db.getAllMascotas()
    return mascotas

if __name__ == "__main__":
    # creación de tres mascotas
    mascota1 = Mascota("Linna", "reptil", "14", "0.9", "verde", "hembra", "charales")
    mascota2 = Mascota("Firulais", "mamifero", "3", "4", "cafe", "macho", "croquetas")
    mascota3 = Mascota("Zeus", "mamifero", "2", "3", "gris", "macho", "whiskas")

    db = sqlite("mascotasDataBase.db") # archivo donde irá la base de datos
    cur = db.conn.cursor()
    # creamos tabla mascotas para almacenar las mascotas
    cur.execute("""CREATE TABLE MASCOTAS (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nombre TEXT,
                   especie TEXT,
                   edad INT,
                   peso DOUBLE,
                   color TEXT,
                   genero TEXT,
                   comidaFav TEXT)""")
    # guardamos las mascotas
    saveMascota(mascota1, db)
    saveMascota(mascota2, db)
    saveMascota(mascota3, db)
    print(*showMascotas(db), sep="\n") # imprimimos las mascotas
