import unittest
import Leds

class TestLeds(unittest.TestCase):
    def test_Leds(self):
        # Caso de prueba 1
        res=Leds.conteoLeds(1)
        self.assertEqual(res, 2)
        # Caso de prueba 2
        res=Leds.conteoLeds(32)
        self.assertEqual(res, 10)
        # Caso de prueba 3
        res=Leds.conteoLeds(8888)
        self.assertEqual(res, 28)
        # Caso de prueba 4
        res=Leds.conteoLeds(115380)
        self.assertEqual(res, 27)
        # Caso de prueba 5
        res=Leds.conteoLeds(2819311)
        self.assertEqual(res, 29)
        # Caso de prueba 6
        res=Leds.conteoLeds(23456)
        self.assertEqual(res, 25)

if __name__ == '__main__':
    unittest.main()
