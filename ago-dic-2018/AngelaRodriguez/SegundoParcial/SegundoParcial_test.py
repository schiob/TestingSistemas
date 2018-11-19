import unittest
import SegParcial


class SumaImpar (unittest.TestCase):
	def SumaImpar(self):
		res=SegParcial.suma(6,-5)
		res2=SegParcial.suma(12,15)
		res3=SegParcial.suma(12,12)
		res4=SegParcial.suma(123,321)
		res5=SegParcial.suma(4321,1234)
		res6=SegParcial.suma(-19289,7853)
		

		self.assertEqual(res, 5)
		self.assertEqual(res2, 13)
		self.assertEqual(res3, 0)
		self.assertEqual(res4, 21756)
		self.assertEqual(res5, 4284911)
		self.assertEqual(res6, -77593260)

if __name__ =='__main__':
	unittest.main() 