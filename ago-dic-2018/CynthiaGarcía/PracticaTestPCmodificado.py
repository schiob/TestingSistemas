import unittest
import practicaenPC  #importa el archivo que quiere comprobar

class TestJuanita(unittest.TestCase):
		def test_numeros(self):
			res=practicaenPC.calc([-7, -5, -40, 8, -3])
			res2=practicaenPC.calc([1, 10, -3, 14,2])

			self.assertEqual(res[0],2)
			self.assertEqual(res[1],3)
			self.assertEqual(res[2],1)
			self.assertEqual(res[3],4)

			self.assertEqual(res2[0],3)
			self.assertEqual(res2[1],2)
			self.assertEqual(res2[2],4)
			self.assertEqual(res2[3],1)
			 #revisa el programa

if __name__ == '__main__':
	unittest.main()			