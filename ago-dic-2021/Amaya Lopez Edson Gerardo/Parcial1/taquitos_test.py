
import unittest
from taquitos import taquitos_sabrositos

class Test_suma(unittest.TestCase):
    def test_taquitos(self):
        test_cases=[
            {
                "name" : "tacos repetidos",
                "input" :["cachete","lengua","cachete","tripitas","machito","machito","machito","cachete","lengua"],
                "output" :110,
            },
            {
                "name" : "el mismo taco",
                "input" : ["cachete","cachete","cachete","cachete","cachete","cachete","cachete","cachete","cachete"],
                "output" : 117
            },
            {
                "name": "tacos que no estan en el menu y taco vacio",
                "input":["","perro","cachete","puerco","machito","machito","machito","mejilla","lengua"],
                "output": 65
            },
             {
                "name": "no tenemos pedido de taco",
                "input":[""],
                "output": 0
            }
        ]
        for tc in test_cases:
            resultad = taquitos_sabrositos(tc["input"])
            self.assertEqual(resultad, tc["output"],
            msg= f'falla el test.')


if __name__ == '__main__':
    unittest.main()





