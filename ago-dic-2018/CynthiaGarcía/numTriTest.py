import unittest
import numerosTriangulares

class  TestTriangulares(unittest.TestCase):
		def test_triang(self):
			re=numerosTriangulares.calcNT(5)
			re2=numerosTriangulares.calcNT(1)
			re3=numerosTriangulares.calcNT(3)
			re4=numerosTriangulares.calcNT(4)
			re5=numerosTriangulares.calcNT(56)
			re6=numerosTriangulares.calcNT(40)

			self.assertEqual(re, 15)
			self.assertEqual(re2, 1)
			self.assertEqual(re3, 6)
			self.assertEqual(re4, 10)
			self.assertEqual(re5, 1596)
			self.assertEqual(re6, 80200)

if __name__ == '__main__' :	
	unittest.main()

	
