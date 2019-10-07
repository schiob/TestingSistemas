import unittest
from drawing_book import solve

class TestDrawingBook(unittest.TestCase):

    def test_1a_pag_par(self):
        self.assertEqual(solve(6, 1), 0)

    def test_1a_pag_impar(self):
        self.assertEqual(solve(5, 1), 0)

    def test_ultima_pag_par(self):
        self.assertEqual(solve(6, 6), 0)

    def test_ultima_pag_impar(self):
        self.assertEqual(solve(5, 5), 0)

    def test_pag_central_par(self):
        self.assertEqual(solve(10, 5), 2)

    def test_pag_central_impar(self):
        self.assertEqual(solve(9, 5), 2)

    def test_primera_mitad_par(self):
        self.assertEqual(solve(10, 3), 1)

    def test_primera_mitad_impar(self):
        self.assertEqual(solve(9, 3), 1)

    def test_segunda_mitad_par(self):
        self.assertEqual(solve(10, 7), 2)

    def test_segunda_mitad_impar(self):
        self.assertEqual(solve(9, 7), 1)


if __name__ == '__main__':
    unittest.main()
