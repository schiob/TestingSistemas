import unittest
import Leds

class TestLeds(unittest.TestCase):
    def test_led1(self):
        res=Leds.CalcularLeds(1)
        self.assertEqual(res,2)
    def test_led2(self):
        res=Leds.CalcularLeds(32)
        self.assertEqual(res,10)
    def test_led3(self):
        res=Leds.CalcularLeds(8888)
        self.assertEqual(res,28)
    def test_led4(self):
        res=Leds.CalcularLeds(115380)
        self.assertEqual(res,27)
    def test_led5(self):
        res=Leds.CalcularLeds(2819311)
        self.assertEqual(res,29)
    def test_led6(self):
        res=Leds.CalcularLeds(23456)
        self.assertEqual(res,25)
if __name__ == '__main__':
    unittest.main()
