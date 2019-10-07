import Leds
import unittest

class Testeo(unittest.TestCase):
    def test_cuentaleds(self):
        res = Leds.cuentaleds(1)
        self.assertEqual(res, 2)
        res = Leds.cuentaleds(32)
        self.assertEqual(res, 10)
        res = Leds.cuentaleds(8888)
        self.assertEqual(res, 28)
        res = Leds.cuentaleds(115380)
        self.assertEqual(res, 27)
        res = Leds.cuentaleds(2819311)
        self.assertEqual(res, 29)
        res = Leds.cuentaleds(23456)
        self.assertEqual(res, 25)

if __name__ == '__main__':
    unittest.main()
