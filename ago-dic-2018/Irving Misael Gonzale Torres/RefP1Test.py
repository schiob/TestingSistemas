import unittest
import RefactorizandoPractica1

class TestPractica1(unittest.TestCase):

	def test_numeros(self):
		result = RefactorizandoPractica1.calculo([5, -5, 4, -4, 2, -2, 0, 0])# ingresando manualmente los numeros
		self.assertEqual(result[0],2)#verificando la salida de numeros "ceros" respecto a los numeros ingresados en result
		self.assertEqual(result[1],3)#verificando la salida de numeros "positivos" respecto a los numeros ingresados en result
		self.assertEqual(result[2],3)#verificando la salida de numeros "negativos" respecto a los numeros ingresados en result
		self.assertEqual(result[3],4)#verificando la salida de numeros "pares" respecto a los numeros ingresados en result
		self.assertEqual(result[4],2)#verificando la salida de numeros "impares" respecto a los numeros ingresados en result

if __name__ == '__main__':
	unittest.main()