import unittest
from Parcial1 import *

class taquitosTest(unittest.TestCase):

    def githubEjemploPrueba(self):
        orden = "cachete lengua cachete tripitas machito machito machito cachete lengua"
        resultado = 110
        self.assertEqual(resultado,orden)

    def masDeTreintaTest(self):
        orden = "cachete lengua cachete tripitas machito machito machito cachete lengua cachete lengua cachete tripitas machito machito machito cachete lengua cachete lengua cachete tripitas machito machito machito cachete lengua cachete lengua cachete tripitas machito machito machito cachete lengua"
        resultado = "Error son demaciados taquitos"
        self.assertEqual(resultado,orden)

    def tacoNoEnMenuTest(self):
        orden = "lengua cachete tripitas barbacoa machito"
        resultado = "Hay un taquito que no existe en el menu"
        self.assertEqual(resultado,orden)

    def separadosPorComasTest(self):
        orden = "cachete,lengua,cachete,tripitas,machito,machito,machito,cachete,lengua"
        resultado = 0
        self.assertEqual(resultado,orden)

        
if __name__ == '__main__':
    unittest.main()