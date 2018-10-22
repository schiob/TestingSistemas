import unittest
import impares

class Test_Impar(unittest.TestCase):
    def Testimpar(self):
#caso de prueba 1
        res=impares.impar(6,-5)
        self.assertEqual(res,5)

#caso de prueba 2
        res=impares.impar(12,15)
        self.assertEqual(res,13)
#caso de prueba 2
        res=impares.impar(12,12)
        self.assertEqual(res,0)
#caso de prueba 3
        res=impares.impar(123,321)
        self.assertEqual(res,21756)

#caso de prueba 4
        res=impares.impar(4321,1234)
        self.assertEqual(res,4284911)

#caso de prueba 5
        res=impares.impar(-19289,7853)
        self.assertEqual(res,-77593260)

if __name__ =='__main__':
    unittest.main()
