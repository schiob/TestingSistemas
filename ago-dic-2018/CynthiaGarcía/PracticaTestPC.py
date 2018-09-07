import unittest
import practicaenPC  #importa el archivo que quiere comprobar

class TestJuanita(unittest.TestCase):
		def test_numeros(self):
			res=practicaenPC.calc([0, 4, 3, 5, 8])
			self.assertEqual(res[1], 2) #revisa el programa

if __name__ == '__main__':
	unittest.main()			