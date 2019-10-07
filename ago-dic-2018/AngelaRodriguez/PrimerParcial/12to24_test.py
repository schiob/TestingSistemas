import unittest
import examen

class TestHora (unittest.TestCase):
	def test_horas(self):
		res=examen.conv_horas("02:23 P.M.")
		res2=examen.conv_horas("11:42 P.M.")
		res3=examen.conv_horas("11:42 A.M.")
		res4=examen.conv_horas("12:00 A.M.")
		res5=examen.conv_horas("12:00 P.M.")
		res6=examen.conv_horas("01:05 A.M.")
		res7=examen.conv_horas("11:59 P.M.")
		

		self.assertEqual(res, '14:23hrs')
		self.assertEqual(res2, '23:43hrs')
		self.assertEqual(res3, '11:42hrs')
		self.assertEqual(res4, '00:00hrs')
		self.assertEqual(res5,'12:00hrs')
		self.assertEqual(res6, '01:05hrs')
		self.assertEqual(res7, '23:59hrs')

if __name__ =='__main__':
	unittest.main() 