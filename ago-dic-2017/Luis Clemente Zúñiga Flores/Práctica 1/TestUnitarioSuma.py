import unittest
from suma import suma_nums

#Prueba unitaria para la función suma_nums
class TestUnitarioSuma(unittest.TestCase):
   
   def testSuma(self):
	   arr = [10,11,12,13,14]
	   self.assertEqual(suma_nums(arr),'46 50')	   
	   
if __name__ == '__main__':
    unittest.main()
