import unittest
from practica2 import printFile
from practica2 import writeFile

class TestPractica2(unittest.TestCase):

    # metodo setUp() se invoca antes de cada test.
    def setUp(self):
        # Se abre un archivo vacío.
        fil = open("Test.txt","w")

    def test_printFile_caso1(self):
        # El archivo vacío se sobreescribe con 'hola taco'.
        writeFile("Test.txt","hola taco")
        # test Equal.
        self.assertEqual(printFile("Test.txt"),"hola taco")

    def test_printFile_caso2(self):
        # Test.txt está vacío por defecto.
        self.assertEqual(printFile("Test.txt"), "")

    def test_printFile_caso3(self):
        # Test.txt se sobreescribe con 'hola\nsalto\ntamal'.
        writeFile("Test.txt","hola\nsalto\ntamal")
        # test con saltos de línea".
        self.assertEqual(printFile("Test.txt"),"hola\nsalto\ntamal")

    def test_writeFile_caso1(self):
        # Se crea un archivo nuevo con 'charmander'
        writeFile("TestPrint.txt","charmander")
        # Se usa printFile() para comparar contenido.
        self.assertEqual(printFile("TestPrint.txt"), "charmander")

    def test_writeFile_caso2(self):
        # Se sobreescribe TestPrint.txt con "Ya es viernes".
        writeFile("Test.txt","Ya es viernes")
        # Se usa printFile() para comparar contenido.
        self.assertEqual(printFile("Test.txt"), "Ya es viernes")


if __name__ == '__main__':
    unittest.main()
