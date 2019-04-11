import unittest
import os
from unittest.mock import MagicMock
from mascotas import sqlite, Mascota, mostrarMascota

class TestMascotas(unittest.TestCase):
    #crear la base de datos y darle valores
    def setUp(self):
        self.db = sqlite("TestMascotas.db")
        cur = self.db.conn.cursor()
        cur.execute(''' CREATE TABLE IF NOT EXISTS mascotas
        (nombre Text,
        especie Text,
        raza Text,
        edad Integer,
        genero Text)
        ''')

        self.db.guardar(Mascota("Scooby", "Perro", "Pastor Aleman", 6, "Macho"))
        self.db.guardar(Mascota("Zeuz", "Perro", "Chuihuahua", 2, "Macho"))
        self.db.guardar(Mascota("Hachi", "Perro", "Kunhao", 3, "Hembra"))

    #borrar la base de datos
    def tearDown(self):
        self.db.conn.close()
        os.remove("TestMascotas.db")

    #pruebas unitarias con mock
    def testShowAll(self):
        entrada = [Mascota("Scooby", "Perro", "Pastor Aleman", 6, "Macho"),
                Mascota("Zeuz", "Perro", "Chuihuahua", 2, "Macho"),
                Mascota("Hachi", "Perro", "Kunhao", 3, "Hembra")]

        salida_esperada = [Mascota("Scooby", "Perro", "Pastor Aleman", 6, "Macho"),
                   Mascota("Zeuz", "Perro", "Chuihuahua", 2, "Macho"),
                   Mascota("Hachi", "Perro", "Kunhao", 3, "Hembra")]

        dbMock = MagicMock()
        dbMock.mostrar.return_value = entrada

        real = mostrarMascota(dbMock)
        self.assertEqual(salida_esperada, real)

    #test integracion
    def test_integration(self):
        salida_esperada = [Mascota("Scooby", "Perro", "Pastor Aleman", 6, "Macho"),
                        Mascota("Zeuz", "Perro", "Chuihuahua", 2, "Macho"),
                        Mascota("Hachi", "Perro", "Kunhao", 3, "Hembra")]

        real = mostrarMascota(self.db)
        self.assertEqual(salida_esperada, real)

if __name__ == '__main__':
    unittest.main()