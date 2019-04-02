import unittest
import os
from unittest.mock import MagicMock
from mascota import sqlite, Mascota, showMascotas

class TestMascotas(unittest.TestCase):
    # Método para crear base de datos y tabla mascotas
    def setUp(self):
        self.db = sqlite("TestMascotas.db")
        cur = self.db.conn.cursor()
        cur.execute("""CREATE TABLE MASCOTAS (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       nombre TEXT,
                       especie TEXT,
                       edad INT,
                       peso DOUBLE,
                       color TEXT,
                       genero TEXT,
                       comidaFav TEXT)""")

        # guardamos tres mascotas en la base de datos
        self.db.guardar(Mascota("Linna", "reptil", 14, 0.9, "verde", "hembra", "charales"))
        self.db.guardar(Mascota("Firulais", "mamifero", 3, 4, "cafe", "macho", "croquetas"))
        self.db.guardar(Mascota("Zeus", "mamifero", 2, 3, "gris", "macho", "whiskas"))

    # borramos archivo
    def tearDown(self):
        self.db.conn.close()
        os.remove("TestMascotas.db")

    # pruebas unitarias con mock
    def testShowAll(self):
        entrada = [Mascota("Linna", "reptil", 14, 0.9, "verde", "hembra", "charales"),
                   Mascota("Firulais", "mamifero", 3, 4, "cafe", "macho", "croquetas"),
                   Mascota("Zeus", "mamifero", 2, 3, "gris", "macho", "whiskas")]
        salida_esperada = [Mascota("Linna", "reptil", 14, 0.9, "verde", "hembra", "charales"),
                           Mascota("Firulais", "mamifero", 3, 4, "cafe", "macho", "croquetas"),
                           Mascota("Zeus", "mamifero", 2, 3, "gris", "macho", "whiskas")]

        dbMock = MagicMock()
        dbMock.getAllMascotas.return_value = entrada

        real = showMascotas(dbMock)
        self.assertEqual(salida_esperada, real)

    # test de integración
    def test_integration(self):
        salida_esperada = [Mascota("Linna", "reptil", 14, 0.9, "verde", "hembra", "charales"),
                           Mascota("Firulais", "mamifero", 3, 4, "cafe", "macho", "croquetas"),
                           Mascota("Zeus", "mamifero", 2, 3, "gris", "macho", "whiskas")]

        real = showMascotas(self.db)
        self.assertEqual(salida_esperada, real)

if __name__ == "__main__":
    unittest.main()
