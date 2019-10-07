import unittest

from NumeroTriangulares import Ntriangular

class TestNTriangular(unittest.TestCase):

    def setUp(self):
        pass

    def testTriagular1(self):
        result = Ntriangular(1)
        self.assertEqual(result,1)

    def testTriagular3(self):
        result = Ntriangular(3)
        self.assertEqual(result,6)

    def testTriagular4(self):
        result = Ntriangular(4)
        self.assertEqual(result,10)

    def testTriagular56(self):
        result = Ntriangular(56)
        self.assertEqual(result,1596)

    def testTriagular400(self):
        result = Ntriangular(400)
        self.assertEqual(result,80200)

if __name__ == '__main__':
    unittest.main()
