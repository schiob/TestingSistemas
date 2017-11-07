import unittest
from p2 import imprimeFile
from p2 import escribeFile

class TPractica2(unittest.TestCase):

    def setUp(self):
        with open('TestParaEscribir.txt','w') as archivo2:
            archivo2.write("Ya es hora de irse")

    def test_printFile_caso1(self):
        escribeFile('TestParaImprimir.txt','tengo hambre')
        self.assertEqual(imprimeFile("TestParaImprimir.txt"),"tengo hambre")

    def test_printFile_caso2(self):
        self.assertEqual(imprimeFile("TestParaImprimir.txt"), "")

    def test_printFile_caso3(self):
        escribeFile('TestParaImprimir.txt','sigo\ncon\nhambre')
        self.assertEqual(imprimeFile("TestParaImprimir.txt"),"sigo\ncon\nhambre")

    def test_writeFile_caso1(self):
        escribeFile('TestParaImprimir.txt','hadoken')
        escribeFile('TestParaEscribir.txt','hadoken')
        self.assertEqual(imprimeFile("TestParaEscribir.txt"), imprimeFile("TestParaImprimir.txt"))

    def test_writeFile_caso2(self):
        escribeFile('TestParaImprimir.txt','Mi momento a llegado')
        escribeFile('TestParaEscribir.txt','Mi momento a llegado')
        self.assertEqual(imprimeFile("TestParaEscribir.txt"), imprimeFile("TestParaImprimir.txt"))


if __name__ == '__main__':
    unittest.main()
