import unittest
from taquitos import taqueria

class test_total(unittest.TestCase):
    def test_taqueria(self):
        test_cases=[
            {
                "name" : "orden de tacos del mismo",
                "input" :['cachete', 'cachete', 'cachete'],
                "output" :33,
            },
            {
                "name" : "orden de tacos mixto",
                "input" : ["pastor","cachete","lengua"],
                "output" : 38
            },
            {
                "name": "orden vacia",
                "input":[""],
                "output": 'Se tienen que ordenar por lo menos 1 taco y maximo 30'
            },
            {
                "name": "mas de 30 tacos",
                "input":['cachete', 'cachete', 'cachete','cachete', 'cachete', 'cachete','cachete', 'cachete', 'cachete','cachete', 'cachete', 'cachete','cachete', 'cachete', 'cachete','cachete', 'cachete', 'cachete','cachete', 'cachete', 'cachete','cachete', 'cachete', 'cachete','cachete', 'cachete', 'cachete','cachete', 'cachete', 'cachete','cachete', 'cachete', 'cachete','cachete', 'cachete', 'cachete','cachete', 'cachete', 'cachete','cachete', 'cachete', 'cachete','cachete', 'cachete', 'cachete','cachete', 'cachete', 'cachete','cachete', 'cachete', 'cachete','cachete', 'cachete', 'cachete','cachete', 'cachete', 'cachete','cachete', 'cachete', 'cachete','cachete', 'cachete', 'cachete'],
                "output": 'Se tienen que ordenar por lo menos 1 taco y maximo 30'
            }




        ]
        for tc in test_cases:
            resultado = taqueria(tc["input"])
            self.assertEqual(resultado, tc["output"],
            msg= f'fallo el test.')

if __name__ == '__main__':
    unittest.main()