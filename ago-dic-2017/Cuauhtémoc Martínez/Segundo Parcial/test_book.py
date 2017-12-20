import unittest
from drawing_book import solve

class TestDB(unittest.TestCase):

    # Caso en que busca la primer pagina.
    def testPage1(self):
        self.assertEqual(solve(6,1), 0)
        self.assertEqual(solve(7,1), 0)

    # Caso en que busca la ultima pagina.
    def testLastPage(self):
        self.assertEqual(solve(6,6), 0)
        self.assertEqual(solve(7,7), 0)

    # Caso en que busca la pagina central.
    def testMidPage(self):
        self.assertEqual(solve(6,3), 1)
        self.assertEqual(solve(7,4), 1)

    # Caso en que busca una pagina en la primer mitad.
    def testF(self):
        self.assertEqual(solve(6,2), 1)
        self.assertEqual(solve(7,3), 1)

    # Caso en que busca una pagina en la segunda mitad.
    def testS(self):
        self.assertEqual(solve(6,4), 1)
        self.assertEqual(solve(7,5), 1)




if __name__ == '__main__':
    unittest.main()
