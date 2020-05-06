import unittest
from Cajas import volumen, lista, calcularcajas

class TestCajas(unittest.TestCase):
    def test_caja(self):
        test= [
             {   "input": 1,
                 "input2": 1,
                 "input3": 2,
                "expect_out": 2
             },
             {   "input": 1,
                 "input2": 1,
                 "input3": 2,
                "expect_out": 2
             },
             {   "input": 1,
                 "input2": 1,
                 "input3": .4,
                "expect_out": None
             },
        ]
        for tc in test :
            actual = volumen(tc["input"],tc["input2"],tc["input3"])
            self.assertEquals(tc["expect_out"],actual)
    
    def test_lista(self):
        test= [
            {
                 "input": ((5,4),(2,3),(6,2)),
                 "expect_out": 38
            },
            {
                 "input": ((5,3),(2,3),(6,2)),
                 "expect_out": 33
            }
        ]
        for tc in test :
             actual = lista(tc["input"])
             self.assertEquals(tc["expect_out"],actual)

    def test_calcular(self):
        test= [
             {   "input": 4,
                 "input2": 3,
                 "input3": 2,
                 "input4": 100,
                 "expect_out": 107
             }
        ]
        for tc in test :
            actual = calcularcajas(tc["input"],tc["input2"],tc["input3"],tc["input4"])
            self.assertEquals(tc["expect_out"],actual)
    
if __name__ == "__main__":
    unittest.main()