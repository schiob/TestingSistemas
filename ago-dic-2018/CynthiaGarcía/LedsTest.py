import unittest
import Leds

class TestLeds(unittest.TestCase):
	def test_leds(self):
		re=Leds.ContadorLeds(1)
		re2=Leds.ContadorLeds(32)
		re3=Leds.ContadorLeds(8888)
		re4=Leds.ContadorLeds(115380)
		re5=Leds.ContadorLeds(2819311)
		re6=Leds.ContadorLeds(23456)
		self.assertEqual(re, 2)
		self.assertEqual(re2, 10)
		self.assertEqual(re3, 28)
		self.assertEqual(re4, 27)
		self.assertEqual(re5, 29)
		self.assertEqual(re6, 25 )

if __name__ == '__main__' :	
	unittest.main()

