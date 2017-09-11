import unittest
from practica2 import printFile
from practica2 import writeFile

class TestPractica2(unittest.TestCase):

    def test_printFile_caso1(self):
        # printFile_caso1.txt tiene escrito "hola taco".
        self.assertEqual(printFile("printFile_caso1.txt"),"hola taco")

    def test_printFile_caso2(self):
        # printFile_caso2.txt está vacío".
        self.assertEqual(printFile("printFile_caso2.txt"), "")

    def test_printFile_caso3(self):
        # printFile_caso3.txt tiene escrito "hola\ntaco\ntamal".
        self.assertEqual(printFile("printFile_caso3.txt"),"hola\nsalto\ntamal")

    def test_writeFile_caso1(self):
        # Al no existir inicial.txt se crea el archivo y se escribe "charmander" en el.
        writeFile("inicial.txt","charmander")
        # Se usa printFile() para comparar contenido con charmander.txt
        # el cual tiene escrito "charmander".
        self.assertEqual(printFile("inicial.txt"), printFile("charmander.txt"))

    def test_writeFile_caso2(self):
        # writeFile_caso2.txt está vacío y se escribe en el "Ya es viernes".
        writeFile("writeFile_caso2.txt","Ya es viernes")
        # Se usa printFile() para comparar contenido con Ya es viernes.txt
        # el cual tiene escrito "Ya es viernes".
        self.assertEqual(printFile("writeFile_caso2.txt"), printFile("Ya es viernes.txt"))


if __name__ == '__main__':
    unittest.main()
