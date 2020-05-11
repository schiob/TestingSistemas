import unittest
from Volumen import volumen
from Contenedor import contenedor
from Full import allinone



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
                "salida_esperada": 30
            }


        ]

        for tc in testcases:
            vol = volumen.calVol(tc["entradas"][0]["largo"],tc["entradas"][1]["ancho"],tc["entradas"][2]["alto"])

            self.assertEqual(vol,tc["salida_esperada"], msg = "Error dato invalido")



    def test_volumencontenedor(self):
        testcases = [

            {
                "nombre" : "calcular volumen correcto",
                "entradas": [
                        
                    {"contenedores": [5,2,6]},
                    {"volumenes": [4,3,2]},
                    

                ],
                "salida_esperada": 38
            },
            {
                "nombre" : "calcular volumen incorrecto",
                "entradas": [
                        
                    {"contenedores": [5,2,6]},
                    {"volumenes": [4,3,2]},
                    

                ],
                "salida_esperada": 36
            },
            {
                "nombre" : "calcular volumen con un 0",
                "entradas": [
                        
                    {"contenedores": [0,0,0]},
                    {"volumenes": [4,3,2]},
                    

                ],
                "salida_esperada": 0
            },
            {
                "nombre" : "calcular volumen con 0 dando valor positivo",
                "entradas": [
                        
                    {"contenedores": [5,2,6]},
                    {"volumenes": [0,0,0]},
                    

                ],
                "salida_esperada": 38
            }


        ]

        for tc in testcases:
            volu = contenedor.volumencontenedor(tc["entradas"][0]["contenedores"],tc["entradas"][1]["volumenes"])

            self.assertEqual(volu,tc["salida_esperada"], msg = "Error dato invalido")




    def test_calnecesario(self):
        testcases = [

            {
                "nombre" : "calcular num de cajas necesarias",
                "entradas": [
                        
                    {"lados": [4,3,2]},
                    {"volumen": 100},
                    

                ],
                "salida_esperada": ['(1,4)', '(1,3)', '(2,2)']
            },
            {
                "nombre" : "Error en la salida",
                "entradas": [
                        
                    {"lados": [4,3,2]},
                    {"volumen": 100},
                    

                ],
                "salida_esperada": ['(4,1)', '(3,1)', '(2,2)']
            }
            

        ]

        for tc in testcases:
            resul = allinone.calnecesario(tc["entradas"][0]["lados"][0],tc["entradas"][0]["lados"][1],tc["entradas"][0]["lados"][2],tc["entradas"][1]["volumen"])

            self.assertEqual(resul,tc["salida_esperada"])




if __name__ == "__main__":
    unittest.main()