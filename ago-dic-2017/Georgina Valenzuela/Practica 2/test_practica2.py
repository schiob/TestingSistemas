import unittest
from practica2 import printFile, writeFile

class TestPractica2(unittest.TestCase):

    def setUp(self):
        file = open("testFile.txt","w")

    def test_printFileTaco(self):
        writeFile("testFile.txt","Hola taco!")
        self.assertEqual(printFile("testFile.txt"),"Hola taco!")

    def test_printFileEmpty(self):
        self.assertEqual(printFile("testFile.txt"), "")

    def test_printFileTamal(self):
        writeFile("testFile.txt","Hola\nsalto\ntamal")
        self.assertEqual(printFile("testFile.txt"),"Hola\nsalto\ntamal")

    def test_writeFileCharmander(self):
        writeFile("testFile.txt","Charmander")
        self.assertEqual(printFile("testFile.txt"), "Charmander")

    def test_writeFileFriday(self):
        writeFile("testFile.txt","Ya es viernes!!!")
        self.assertEqual(printFile("testFile.txt"), "Ya es viernes!!!")


if __name__ == '__main__':
    unittest.main()