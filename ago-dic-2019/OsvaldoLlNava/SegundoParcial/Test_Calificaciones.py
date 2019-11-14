import unittest
from unittest.mock import patch
import Calificaciones
from os import remove

class test(unittest.TestCase):

    file = open("testeo.txt", "w")
    file.write("""Juan matematicas 9
    Juan matematicas 8
    Luis matematicas 10
    Luis matematicas 9
    Enrique matematicas 9
    Enrique letras 8""")
    file.close()

    def test_Escrito(self):
        esp= ['Juan', 8.5, 'Luis', 9.5, 'Enrique', 8.5]
        res = Calificaciones.Calcular_promedios('testeo.txt')
        self.assertEqual(res, esp)

    def test_txt(self):
        esp = ['Juan', 8.95, 'Luis', 9.8, 'Enrique', 8.8]
        res = Calificaciones.Calcular_promedios('calificaciones_alumnos.txt')
        self.assertEqual(res, esp)

    remove('testeo.txt')

if __name__ == '__main__':
    unittest.main()