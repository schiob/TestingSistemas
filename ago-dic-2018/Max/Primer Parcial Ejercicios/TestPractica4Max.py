import unittest
import Practica4Max

class LEDs(unittest.TestCase):
    def test_prueba1(self):
        res = Practica4Max.format_LEDs(1)
        self.assertEqual(res, 2)

    def test_prueba2(self):
        res = Practica4Max.format_LEDs(32)
        self.assertEqual(res, 10)

    def test_prueba3(self):
        res = Practica4Max.format_LEDs(8888)
        self.assertEqual(res, 28)

    def test_prueba4(self):
        res = Practica4Max.format_LEDs(115380)
        self.assertEqual(res, 27)

    def test_prueba5(self):
        res = Practica4Max.format_LEDs(2819311)
        self.assertEqual(res, 29)

    def test_prueba6(self):
        res = Practica4Max.format_LEDs(23456)
        self.assertEqual(res, 25)


if __name__ == '__main__':
    unittest.main()
