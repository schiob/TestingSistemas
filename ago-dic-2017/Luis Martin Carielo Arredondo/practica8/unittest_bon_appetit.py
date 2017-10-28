import unittest
from bon_appetit import bonAppetit

class TestUnitario(unittest.TestCase):
	#Función "constructor":
	def setUp(self):
		self.n=5; self.k=3; self.ar=[10,12,14,8,16]; self.b=30;
		self.n1=5; self.k1=3; self.ar1=[10,12,14,8,16]; self.b1=26;
		self.n2=2; self.k2=0; self.ar2=[18, 12]; self.b2=0;
		self.n3=2; self.k3=1; self.ar3=[18, 12]; self.b3=15;
		self.n4=2; self.k4=1; self.ar4=[18, 12]; self.b4=9;

	#Funciones test:
	def test_bonAppetit(self):
		self.assertEquals(bonAppetit(self.n1, self.k1, self.b1, self.ar1), "Bon Appetit")
		self.assertEquals(bonAppetit(self.n4, self.k4, self.b4, self.ar4), "Bon Appetit")
		

	def test_noBonAppetit(self):
		self.assertEquals(bonAppetit(self.n, self.k, self.b, self.ar), 4)
		self.assertEquals(bonAppetit(self.n2, self.k2, self.b2, self.ar2), -6)
		self.assertEquals(bonAppetit(self.n3, self.k3, self.b3, self.ar3), 6)

if __name__ == '__main__':
	unittest.main()