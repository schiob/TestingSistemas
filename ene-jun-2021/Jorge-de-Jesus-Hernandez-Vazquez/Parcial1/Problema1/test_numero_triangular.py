import unittest
from numeros import numero_triangular


### Casos de pruebas
###  <1, 1>    <3, 6>   <4, 10>    <56, 1596>     <400, 80200>


class TestNumeros(unittest.TestCase):
    def test_numero_triangular(self):
        cases = [(1, 1), (3, 6),   
            (4, 10), (56, 1596), 
                (400, 80200)]
        for i, esp in cases:
            trian = numero_triangular(i)
            self.assertEqual(esp, trian) 

if __name__=="__main__":
    unittest.main()
