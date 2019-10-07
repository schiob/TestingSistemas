import unittest 
import horas_12

class test24(unittest.TestCase):

	def test_24(self):


		c1 = horas_12.calcularHora('02:23 p.m')
		self.assertEqual(c1,'14:23 hrs')

		c2 = horas_12.calcularHora('11:42 p.m')
		self.assertEqual(c2,'23:42 hrs')

		c3 = horas_12.calcularHora('12:00 a.m')
		self.assertEqual(c3, '11:42 hrs')

		c4 = horas_12.calcularHora('12:00 a.m')
		self.assertEqual(c4, '00:00 hrs')

		c5 = horas_12.calcularHora('12:00 p.m')
		self.assertEqual(c5, '12:00 hrs')

		c6 = horas_12.calcularHora('01:05 a.m')
		self.assertEqual(c6, '01:05 hrs')

		c7 = horas_12.calcularHora('11:59 p.m')
		self.assertEqual(c7, '23:59 hrs')




if __name__ == '__main__':
	unittest.main()
