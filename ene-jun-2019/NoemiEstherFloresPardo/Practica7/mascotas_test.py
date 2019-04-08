import unittest
import os
from unittest.mock import MagicMock
from Mascotas import showMascotas, Mascota, DataBase

class TestTacos(unittest.TestCase):
    def setUp(self):
        self.db = DataBase("testMascotas.db")
        cursor = self.db.connection.cursor()
        cursor.execute("CREATE TABLE mascotas (id INTEGER PRIMARY KEY AUTOINCREMENT,nombre TEXT, especie TEXT, edad TEXT)")
        #self.db.connection.close()
        self.db.guardarMascota(Mascota("Morita", "puerquito", "1 mes"))
        self.db.guardarMascota(Mascota("Mailo", "perro", "2 años"))

    def tearDown(self):
        self.db.connection.close()
        os.remove("testMascotas.db")

    def testShowAllMascotas(self):
        entrada = [Mascota("Morita", "puerquito", "1 mes"), Mascota("Mailo", "perro", "2 años")]
        salida_esperada = [Mascota("Morita", "puerquito", "1 mes"), Mascota("Mailo", "perro", "2 años")]

        dbMock = MagicMock()
        dbMock.getAllMascotas.return_value = entrada

        real = showMascotas(dbMock)
        self.assertEqual(salida_esperada, real)

    def test_integration(self):
        salida_esperada = [Mascota("Morita", "puerquito", "1 mes"), Mascota("Mailo", "perro", "2 años")]

        real = showMascotas(self.db)
        self.assertEqual(salida_esperada, real)

if __name__ == "__main__":
    unittest.main()