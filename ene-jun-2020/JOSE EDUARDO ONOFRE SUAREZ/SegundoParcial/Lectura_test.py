import unittest
from unittest.mock import MagicMock
from Lectura import getAverage,Promedio,alumno
import datos



class CalculoPromedioMock(Promedio):
    
    def setAverage(self,promedio):
        self.alumno = alumno("Juan_perez","español",89.5,promedio)

    def Search(self, nombre):
        return self.alumno



class AvTest(unittest.TestCase):

    def test_Prom(self):

        testcases = [

            {
                "entrada" : "Jose_Lopez",
                "salida_esperada" : 86.4,
                "mock_test" :
                {

                    "promedio" : 86.4 
                }


            },
            {
                "entrada" : "Maria_Martinez",
                "salida_esperada" : 92.75,
                "mock_test" :
                {

                    "promedio" : 92.75 
                }


            }


        ]

        for tc in testcases:
            data_mock = CalculoPromedioMock()
            data_mock.setAverage(tc['salida_esperada'])

            compara = getAverage(tc['entrada'],data_mock)

            self.assertEqual(tc['salida_esperada'], compara)

    
     def test_Prom(self):

        testcases = [

            {
                "entrada" : "Jose_Lopez",
                "salida_esperada" : 86.4,
                "mock_test" :
                {

                    "promedio" : 86.4 
                }


            },
            {
                "entrada" : "Maria_Martinez",
                "salida_esperada" : 92.75,
                "mock_test" :
                {

                    "promedio" : 92.75 
                }


            },
            {
                "entrada" : "Maria_Martinez",
                "salida_esperada" : 0,
                "mock_test" :
                {

                    "promedio" : 0 
                }


            },
            {
                "entrada" : "Jose_Lopez",
                "salida_esperada" : 92.45,
                "mock_test" :
                {

                    "promedio" : -82.32 
                }


            }


        ]

        for tc in testcases:
            data_mock = CalculoPromedioMock()
            data_mock.setAverage(tc['salida_esperada'])

            compara = getAverage(tc['entrada'],data_mock)

            self.assertEqual(tc['salida_esperada'], compara)

    ## Simule la creacion del archivo con un String
    def setUp(self):
        print("Preparando el contexto...")
        self.archivo = "Jose_Lopez quimica 89.00\nJose_Lopez matematicas 85.34\nMaria_Martinez fisica 95.50\nMaria_Martinez español 90.00"
        self.promedio = [87.17,92.75]
    
    def test_file(self):
        entrada = self.archivo
        salida_esperada = "Jose_Lopez {}\nMaria_Martinez {}".format(self.promediop[0],self.promedio[1])
        salida_real = getAverage(nombre,archivo)
        
        self.assertEqual(salida_esperada,salida_real)
    
    def tearDown(self):
        print("Destruyendo el contexto...")
        del(self.archivo)
    

if __name__ == "__main__":
    unittest.main()