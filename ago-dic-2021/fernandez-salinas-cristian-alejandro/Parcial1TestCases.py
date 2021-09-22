import unittest
from Parcial1 import taquitos

class taquitosTest(unittest.TestCase):

    def test_githubEjemploPrueba(self):
        orden = "cachete lengua cachete tripitas machito machito machito cachete lengua"
        resultado = 110
        self.assertEqual(resultado,taquitos(orden))

    def test_masDeTreintaTest(self):
        orden = "cachete lengua cachete tripitas machito machito machito cachete lengua cachete lengua cachete tripitas machito machito machito cachete lengua cachete lengua cachete tripitas machito machito machito cachete lengua cachete lengua cachete tripitas machito machito machito cachete lengua"
        resultado = "Error son demaciados taquitos"
        self.assertEqual(resultado,taquitos(orden))

    def test_tacoNoEnMenuTest(self):
        orden = "lengua cachete tripitas barbacoa machito"
        resultado = 46
        self.assertEqual(resultado,taquitos(orden))

    def test_separadosPorComasTest(self):
        orden = "cachete,lengua,cachete,tripitas,machito,machito,machito,cachete,lengua"
        resultado = 0
        self.assertEqual(resultado,taquitos(orden))

        
if __name__ == '__main__':
    unittest.main()