import unittest
import Practica4

class Test (unittest.TestCase):
    def test_1(self):
        res=Practica4.Led(1)
        self.assertEqual(res, 2)
    def test_2(self):
        res=Practica4.Led(32)
        self.assertEqual(res, 10)
    def test_3(self):
        res=Practica4.Led(8888)
        self.assertEqual(res, 28)
    def test_4(self):
        res=Practica4.Led(115380)
        self.assertEqual(res, 27)
    def test_5(self):
        res=Practica4.Led(2819311)
        self.assertEqual(res, 29)
    def test_6(self):
        res=Practica4.Led(23456)
        self.assertEqual(res, 25)

if __name__ == '__main__':
    unittest.main()
