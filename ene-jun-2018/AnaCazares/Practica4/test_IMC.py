import unittest
from primer_parcial import IMC_desde_archivo

class TestUnitario(unittest.TestCase):
	#Función "constructor":
	def setUp(self):
		IMC_1 = open("IMC_1.txt", "w")
		#IMC_1.write("1.65 70")
		IMC_1.write("42.4242")
		IMC_1.close()

		IMC_2 = open("IMC_2.txt", "w")
		#IMC_2.write("1.5 45")
		IMC_2.write("30")
		IMC_2.close()

	#Funciones test:
	def test_IMC(self):
		self.assertEqual(IMC_desde_archivo("IMC_1.txt"), "IMC.")
		self.assertEqual(IMC_desde_archivo("IMC_2.txt"), "IMC.")
                
	#def  tearDown ( self ): 
        #self.IMC.disponer()
        #self.IMC=None
if __name__ == '__main__':
	unittest.main()
