from practica4_Main import obtenerPromedios,personas
import unittest

class testPractica4(unittest.TestCase):
    def test_practica4(self):
        nombreArchivo="testtexto.csv"
        resultado={'hotmail.com': 92.0, 'gmail.com': 55.5}
        self.assertEqual(obtenerPromedios(nombreArchivo),resultado)

if __name__ == "__main__":
    unittest.main()