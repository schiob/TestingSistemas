import unittest
import leds
class Leds(unittest.TestCase):

    def test1(self):
        resultado = Leds.format_Leds(0000)
        self.assertEqual(res, 24)
    def test2(self):
        resultado = Leds.format_Leds(10)
        self.assertEqual(res, 8)
    def test3(self):
        resultado = Leds.format_Leds(675)
        self.assertEqual(res, 14)
    def test4(self):
        resultado = Leds.format_Leds(2018)
        self.assertEqual(res, 20)
    def test5(self):
        resultado = Leds.format_Leds(666)
        self.assertEqual(res, 18)
    def test6(self):
        resultado = Leds.format_Leds(18361)
        self.assertEqual(res, 22)
    def test7(self):
        resultado=Leds.format_Leds(9625)
        self.assertEqual(res,25)
if __name__ == '__main__':
    unittest.main()
