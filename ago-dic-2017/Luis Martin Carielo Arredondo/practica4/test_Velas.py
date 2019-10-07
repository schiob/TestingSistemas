import unittest
from Velas import birthdaycake_candles

class TestUnitario(unittest.TestCase):
	#Función "constructor":
	def setUp(self):
		self.n=5; self.lista=[10,10,9,8,9]
		self.n2=3; self.lista2=[1,1,1]
		self.n3=1; self.lista3=[5]
		self.n4=2; self.lista4=[4,1]
		self.n5=0; self.lista5=[]

	#Funciones test:
	def test_time_convertion(self):
		self.assertEqual(birthdaycake_candles(self.n, self.lista), 2)
		self.assertEqual(birthdaycake_candles(self.n2, self.lista2), 3)
		self.assertEqual(birthdaycake_candles(self.n3, self.lista3), 1)
		self.assertEqual(birthdaycake_candles(self.n4, self.lista4), 1)
		self.assertEqual(birthdaycake_candles(self.n5, self.lista5), 0)
		
if __name__ == '__main__':
	unittest.main()