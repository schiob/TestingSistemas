import unittest
from drawingB import solve

class TestDrawingB(unittest.TestCase):
    def testPaginasPar(self):
        self.assertEqual(solve(3, 1), 0)
        self.assertEqual(solve(6, 6), 0)
        self.assertEqual(solve(4, 3), 1)
        self.assertEqual(solve(2, 2), 0)
        self.assertEqual(solve(4, 4), 0)

    def testPaginasImpar(self):
        self.assertEqual(solve(1, 1), 0)
        self.assertEqual(solve(5, 5), 0)
        self.assertEqual(solve(5, 3), 1)
        self.assertEqual(solve(3, 1), 0)
        self.assertEqual(solve(5, 4), 0)

if __name__ == '__main__':
    unittest.main()
