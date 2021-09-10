import unittest
from Pratica_2 import suma_Numeros
class test_suma(unittest.TestCase):
    def test_suma(self):
        
        test_cases =[
            (5, 5, 10),
            (-5, 6, 1),
            (-5, -4, -9),
            (1.5, 1.5, 3.0),
            (-0.5, 1, .5),
            ("n1", 1, "error"),
            (1,"n2", "error"),
            (1/2, 1/2, 1),
            (1,-1/2,0.5),
            (1e10,1e10,2e10),
            (-2e5,1e5,-1e5),
            (-2e5,-2e5,-4e5),
            (1e5,1e-6,100000.000001)
         
            ]
        for tc in test_cases:
            resultado = suma_Numeros(tc[0], tc[1])
            self.assertEqual(resultado, tc[2])
        

if __name__=="__main__":
    unittest.main()