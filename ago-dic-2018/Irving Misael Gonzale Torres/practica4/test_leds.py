import unittest
import Leds

class test(unittest.TestCase):
    def test_numleds(self):
        r1 = Leds.NumLeds(1)
        self.assertEqual(r1,2)

        r2 = Leds.NumLeds(32)
        self.assertEqual(r2,10)

        r3 = Leds.NumLeds(8888)
        self.assertEqual(r3,28)

        r4 = Leds.NumLeds(115380)
        self.assertEqual(r4,27)

        r5 = Leds.NumLeds(23456)
        self.assertEqual(r5,25)


if __name__ == '__main__':
    unittest.main()
