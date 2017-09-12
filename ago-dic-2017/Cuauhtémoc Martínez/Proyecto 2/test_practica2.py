import unittest
from practica2 import printFile
from practica2 import writeFile

class TestPractica2(unittest.TestCase):

    # metodo setUp() se invoca antes de cada test.
    def setUp(self):
        # Se abren dos archivo vacío.
        fil = open("TestPrint.txt","w")
        fil2 = open("TestWrite.txt","w")

    def test_printFile_caso1(self):
        # El archivo vacío se sobreescribe con 'hola taco'.
        writeFile("TestPrint.txt","hola taco")
        # test Equal.
        self.assertEqual(printFile("TestPrint.txt"),"hola taco")

    def test_printFile_caso2(self):
        # Test.txt.txt está vacío por defecto.
        self.assertEqual(printFile("TestPrint.txt"), "")

    def test_printFile_caso3(self):
        # Test.txt se sobreescribe con 'hola\nsalto\ntamal'.
        writeFile("TestPrint.txt","hola\nsalto\ntamal")
        # test con saltos de línea".
        self.assertEqual(printFile("TestPrint.txt"),"hola\nsalto\ntamal")

    def test_writeFile_caso1(self):
        # Se sobreescribe TestPrint.txt y TestWrite.txt con "charmander".
        writeFile("TestPrint.txt","charmander")
        writeFile("TestWrite.txt","charmander")
        # Se usa printFile() para comparar contenido.
        self.assertEqual(printFile("TestWrite.txt"), printFile("TestPrint.txt"))

    def test_writeFile_caso2(self):
        # Se sobreescribe TestPrint.txt y TestWrite.txt con "Ya es viernes".
        writeFile("TestPrint.txt","Ya es viernes")
        writeFile("TestWrite.txt","Ya es viernes")
        # Se usa printFile() para comparar contenido.
        self.assertEqual(printFile("TestWrite.txt"), printFile("TestPrint.txt"))


if __name__ == '__main__':
    unittest.main()
