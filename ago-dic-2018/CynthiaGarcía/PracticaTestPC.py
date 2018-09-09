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

			#casos de prueba del archivo 
			res3=practicaenPC.calc([-1, 4, 2, 3, 10])
			self.assertEqual(res3[0],3)

			res4=practicaenPC.calc([-4,0,11,7,9])
			self.assertEqual(res4[1],3)

			res5=practicaenPC.calc([-7,-5,40,8,-3])
			self.assertEqual(res5[1],2) #Debe ser fallo
			self.assertEqual(res5[3],4)

			res6=practicaenPC.calc([-7,-5,1,8,-3])
			self.assertEqual(res6[2],2)

			

if __name__ == '__main__':
	unittest.main()			