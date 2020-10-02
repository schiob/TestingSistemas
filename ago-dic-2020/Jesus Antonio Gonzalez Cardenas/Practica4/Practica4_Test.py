from Practica4 import getAverages
import unittest

class TestsAverage(unittest.TestCase):
    def testP4(self):
        file_for_test = 'Practica4TData.csv'
        Prueba = {'hotmail.com': 81.33, 'protonmail.com': 88.33}
        self.assertEqual(getAverages(file_for_test), Prueba)


if __name__ == "__main__":
    unittest.main()