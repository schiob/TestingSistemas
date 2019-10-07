import unittest
from practica2 import printFile, writeFile

class TestParaPractica2(unittest.TestCase):


    def setUp(self):
        with open ("wt.txt","w") as f:
            f.write("Ya es viernes")

    def prueba_Print1(self):
        self.assertEqual(printFile("pt.txt"),"hola tacos")

    def prueba_Print2(self):
        self.assertEqual(printFile("pt.txt"), "")

    def prueba_Print3(self):
        self.assertEqual(printFile("pt.txt"),"hola\nsalto\ntamal")

    def prueba_Write1(self):
        self.assertEqual(printFile("wt.txt"), printFile("pt.txt"))

    def prueba_Write2(self):
        self.assertEqual(printFile("wt.txt"), printFile("pt.txt"))

if __name__ == '__main__':
    unittest.main()
