from pathlib import Path
import os
import unittest
from IMC import calcIMC

"""The setUp() and tearDown() methods allow you to define instructions that will
 be executed before and after each test method."""

class TestIMC(unittest.TestCase):

    def setUp(self):

        my_file = Path("IMC.txt")
        if my_file.is_file() == False:
            #Create the file
            file = open("IMC.txt", "w")
            file.close()

    def test_good(self):

        calcIMC(95, 1.83)
        f = open("IMC.txt", "r")
        msj = f.read()
        self.assertEqual(msj, "IMC=28.37")
        f.close()

    def test_skyscrapper(self):

        result = calcIMC(95, 3)
        self.assertEqual(result, 'Seguro que eres humano?.')

    def tearDown(self):

        os.remove("IMC.txt")


if __name__ == '__main__':
    unittest.main()
