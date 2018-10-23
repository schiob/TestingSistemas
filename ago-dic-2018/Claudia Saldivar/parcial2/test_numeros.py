import unittest
import numeros

class Test_Impar(unittest.TestCase):
    def Testimpar(self):

        res=numeros.numeros_impar(6,-5)
        self.assertEqual(res,5)

        res=numeros.numeros_impar(12,15)
        self.assertEqual(res,13)

        res=numeros.numeros_impar(12,12)
        self.assertEqual(res,0)

        res=numeros.numeros_impar(123,321)
        self.assertEqual(res,21756)

        res=numeros.numeros_impar(4321,1234)
        self.assertEqual(res, 4284911)

        res=numeros.numeros_impar(-19289, 7853)
        self.assertEqual(res, -77593260)



if __name__ =='__main__':
    unittest.main()
