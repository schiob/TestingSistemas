import sqlite3

class Mascota():
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    def __str__(self):
        return "Nombre de la mascota: {} Especie: {} Edad: {}".format(self.nombre, self.especie, self.edad)

    def __eq__(self, taco):
        if Mascota.nombre != self.nombre:
            return False

        if Mascota.especie != self.especie:
            return False

        if Mascota.edad != self.edad:
            return False
        return True

class sqlite():
    def __init__(self, archivo):
        self.conn = sqlite3.connect(archivo)

    def save(self, Mascota):
        cur = self.conn.cursor()
        values = (Mascota.nombre, Mascota.especie, Mascota.edad)
        cur.execute("INSERT INTO mascotas (id,nombre, especie, edad) VALUES (null,?,?,?)", values)
        self.connection.commit()

    def getAllMascota(self):
        cur = self.conn.cursor()
        mm = cur.execute("SELECT * FROM MASCOTA").fetchall()

        mascota = []
        for m in mm:
            mascota.append(Mascota(m[1], m[2], m[3]))
        return mascota


def saveMascota(Mascota, db):
    db.save(Mascota)

def showMascota(db):
    mascota = db.getAllMascotas()
    return mascota

if __name__ == "__main__":
    mascota1 = Mascota("Sorullo", "perro", 10)
    mascota2 = Mascota("Sorulla", "perro", 2)
    mascota3 = Mascota("Gigio", "perro", 18)
    mascota4 = Mascota("Rex", "perro", 10)
    mascota5 = Mascota("Gigin", "perro", 12)
    mascota6 = Mascota("Taco", "perro", 3)
    mascota7 = Mascota("Zeus", "perro", 3)
    mascota8 = Mascota("Bodoque", "perro", 3)

    db = sqlite("Mascotas.db")
    # cur = db.conn.cursor()
    # cur.execute("CREATE TABLE TACOS (id INTEGER PRIMARY KEY AUTOINCREMENT,tortilla TEXT, guiso TEXT, salsa TEXT)")


    saveMascota(mascota1, db)
    saveMascota(mascota2, db)
    saveMascota(mascota3, db)
    saveMascota(mascota4, db)
    saveMascota(mascota5, db)
    saveMascota(mascota6, db)
    saveMascota(mascota7, db)
    saveMascota(mascota8, db)

    print(*showMascota(db), sep="\n")