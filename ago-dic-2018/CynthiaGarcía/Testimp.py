import unittest
import imp

class TestLeds(unittest.TestCase):
	def test_impares(self):
		re=imp.NumImpares(6,-5)
		re1=imp.NumImpares(12,15)
		re2=imp.NumImpares(12,12)
		re3=imp.NumImpares(123,321)
		re4=imp.NumImpares(4321,1234)
		re5=imp.NumImpares(-19289,7853)

		self.assertEquals(re, 5)
		self.assertEquals(re1,13)
		self.assertEquals(re2,0)
		self.assertEquals(re3,21756)
		self.assertEquals(re4,4284911)
		self.assertEquals(re5,-77593260)
		
if __name__ == '__main__' :	
	unittest.main()