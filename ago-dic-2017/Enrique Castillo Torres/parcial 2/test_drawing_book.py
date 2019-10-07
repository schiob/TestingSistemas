import unittest
from drawing_book import solve

class TestBook(unittest.TestCase):

    def test_first_impar(self):
        self.assertEqual(solve(9, 1), 0)

    def test_first_par(self):
        self.assertEqual(solve(10, 1), 0)

    def test_last_par(self):
        self.assertEqual(solve(8, 8), 0)

    def test_last_impar(self):
        self.assertEqual(solve(7, 7), 0)

    def test_middle_par(self):
        self.assertEqual(solve(8, 5), 2)

    def test_middle_impar(self):
        self.assertEqual(solve(9, 5), 2)

    def test_first_half_par(self):
        self.assertEqual(solve(6, 2), 1)

    def test_first_half_impar(self):
        self.assertEqual(solve(5, 2), 1)

    def test_second_half_par(self):
        self.assertEqual(solve(6, 4), 1)

    def test_second_half_impar(self):
        self.assertEqual(solve(7, 4), 1)

if __name__ == "__main__":
    unittest.main()
