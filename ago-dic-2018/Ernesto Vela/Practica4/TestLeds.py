import unittest
import Leds

class ledsTest(unittest.TestCase):
    def test_Leds(self):
        res = Leds.leds(1)
        self.assertEqual(res, 2)

        res = Leds.leds(32)
        self.assertEqual(res, 10)

        res = Leds.leds(8888)
        self.assertEqual(res, 28)

        res = Leds.leds(115380)
        self.assertEqual(res, 27)

        res = Leds.leds(2819311)
        self.assertEqual(res, 29)

        res = Leds.leds(23456)
        self.assertEqual(res, 25)

if __name__ == '__main__':
    unittest.main()
