import unittest
import practica4

class TestLeds (unittest.TestCase):
	def test_leds(self):
		res=practica4.contar_leds(1)
		res2=practica4.contar_leds(32)
		res3=practica4.contar_leds(8888)
		res4=practica4.contar_leds(115380)
		res5=practica4.contar_leds(2819311)
		res6=practica4.contar_leds(23456)
		

		self.assertEqual(res, 2)
		self.assertEqual(res2, 10)
		self.assertEqual(res3, 28)
		self.assertEqual(res4, 27)
		self.assertEqual(res5, 29)
		self.assertEqual(res6, 25)

if __name__ =='__main__':
	unittest.main() 