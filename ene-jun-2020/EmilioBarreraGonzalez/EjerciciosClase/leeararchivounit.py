import unittest
from leerarchivo import countChar
import os
class testArchivo(unittest.TestCase):
    ##SETUP
    def setUp(self):
        file = open("prueba.txt", "w+")
        file.write("asdasdasdasdasdasdasdasdasdasd")
        file.close()
        print("Se creo archivo para prueba")
    ##TESTCASES
    def test_file(self):
        salida_esperada=30
        salida_verdadera=countChar("prueba.txt")
        self.assertEqual(salida_esperada,salida_verdadera)
    ##TEARDOWN    
    def tearDown(self):
        os.remove("prueba.txt")
        print("Se removio el archivo prueba")

if __name__ == "__main__":
    unittest.main()