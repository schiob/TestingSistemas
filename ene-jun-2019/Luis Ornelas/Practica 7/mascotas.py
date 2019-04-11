import sqlite3

class Mascota():
    #creamos el objeto
    def __init__(self, nombre, especie, raza, edad, genero):
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.edad = edad
        self.genero = genero

    def __str__(self):
        return str(f"Tu Mascota se llama {self.nombre} es un {self.especie} de raza {self.raza} con edad de {self.edad} su genero es {self.genero}")

    def __eq__(self, mascota):
        if mascota.nombre != self.nombre:
            return False

        if mascota.especie != self.especie:
            return False

        if mascota.raza != self.raza:
            return False

        if mascota.edad != self.edad:
            return False

        if mascota.genero != self.genero:
            return False

class sqlite():
    def __init__(self, archivo):
        self.conn = sqlite3.connect(archivo)

    def guardar(self, mascota):
        cur = self.conn.cursor()
        cur.execute("INSERT INTO mascotas VALUES ('{}','{}','{}','{}','{}')".format(mascota.nombre, mascota.especie, mascota.raza, mascota.edad, mascota.genero))
        self.conn.commit()

    def mostrar(self):
        cur = self.conn.cursor()
        mascotas = cur.execute("SELECT * FROM mascotas").fetchall()
        lista = []

        for m in mascotas:
            lista.append(Mascota(m[0], m[1], m[2], m[3], m[4]))
        return lista

def guardarMascota(mascota, db):
    db.guardar(mascota)

def mostrarMascota(db):
    mascotas = db.mostrar()
    return  mascotas

if __name__ == '__main__':
    mascota1 = Mascota("Scooby", "Perro", "Pastor Aleman", 6, "Macho")
    mascota2 = Mascota("Zeuz", "Perro", "Chuihuahua", 2, "Macho")
    mascota3 = Mascota("Hachi", "Perro", "Kunhao", 3, "Hembra")

    db = sqlite("MascotasDB.db")
    cur = db.conn.cursor()

    cur.execute(''' CREATE TABLE IF NOT EXISTS mascotas
    (nombre Text,
    especie Text,
    raza Text,
    edad Integer,
    genero Text)
    ''')

    guardarMascota(mascota1, db)
    guardarMascota(mascota2, db)
    guardarMascota(mascota3, db)
    print(*mostrarMascota(db), sep="\n")