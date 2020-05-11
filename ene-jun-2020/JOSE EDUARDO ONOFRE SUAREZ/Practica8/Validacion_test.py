import unittest
from Censura import censura
from Validacion import validacion
from unittest.mock import MagicMock

class testVC(unittest.TestCase):

    def test_censura(self):

        testcases = [

            {
                "nombre" : "Prueba de censura correcta",
                "entradas" : 
                    {
                    "palabras" : ["popo","sangre","muerte","maldito"],
                    "texto" : "la muerte del maldito",
                    "magword" : "NOOB"
                    },
        
                "salida_esperada" : "la NOOB del NOOB"

            },
            {
                "nombre" : "Prueba de censura incorrecta",
                "entradas" : 
                    {
                    "palabras" : ["popo","sangre","muerte","maldito"],
                    "texto" : "la muerte del maldito",
                    "magword" : "NOOB"
                    },
                
                "salida_esperada" : "la NOOB del maldito"

            }


        ]

        for i,tc in enumerate(testcases):

            res = censura.censored(tc["entradas"]["palabras"],tc["entradas"]["texto"],tc["entradas"]["magword"])
           
            self.assertEqual(res,tc["salida_esperada"])

        

        def test_validar(self):

            testcases = [

            {
                "nombre" : "Prueba de validacion correcta",
                "mock_censura" : "la NOOB es NOOB",
                "entradas" : 
                    {
                    "palabras" : ["popo","sangre","muerte","maldito"],
                    "num" : 5,
                    "magword" : "NOOB"
                    },
        
                "salida_esperada" : "El texto sigue siendo valido"

            },
            {
                "nombre" : "Prueba de validacion incorrecta",
                "mock_censura" : "la NOOB es NOOB?",
                "entradas" : 
                    {
                    "palabras" : ["popo","sangre","muerte","maldito"],
                    "num" : 1,
                    "magword" : "NOOB"
                    },
                
                "salida_esperada" : "El texto ya no es valido"

            }


        ]



        for i,tc in enumerate(testcases):
            censura_mock = MagicMock()
            censura_mock.censored.return_value = tc["mock_censura"]
            res = validacion.validar(tc["entradas"]["palabras"],censura_mock,tc["entradas"]["magword"],tc["entrads"]["num"])
            self.assertEqual(res,tc["salida_esperada"])



if __name__ == "__main__":
    unittest.main()
