import unittest
from Volumen import volumen


class TestVolumen(unittest.TestCase):
    def test_calVol(self):
        testcases = [

            {
                "nombre" : "calcular volumen",
                "entradas": [
                        
                    {"largo": 2},
                    {"ancho": 3},
                    {"alto": 4},

                ],
                "salida_esperada": 24
            },
            {
                "nombre" : "calcular volumen 2",
                "entradas": [
                        
                    {"largo": 5},
                    {"ancho": 2},
                    {"alto": 3},

                ],
                "salida_esperada": 30
            },
            {
                "nombre" : "calcular volumen con numero negativo",
                "entradas": [
                        
                    {"largo": -5},
                    {"ancho": 2},
                    {"alto": 3},

                ],
                "salida_esperada": 25
            }


        ]

        for tc in testcases:
            vol = volumen.calVol(tc["entradas"][0]["largo"],tc["entradas"][1]["ancho"],tc["entradas"][2]["alto"])

            self.assertEqual(vol,tc["salida_esperada"], msg = "Error dato invalido")


if __name__ == "__main__":
    unittest.main()