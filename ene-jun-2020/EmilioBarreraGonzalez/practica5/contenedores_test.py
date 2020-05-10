import unittest
from contenedores import *
def vol_calcmock(input1,input2,input3):
    return input1*input2*input3

class test_contenedores(unittest.TestCase):
    def test_volCalc(self):
        test_cases = [
            {
                'name': 'PRUEBA DE CONTENEDORES  3 x 3 x 3',
                'input': ([3.0,3.0,3.0]),
                'expected_out': 27.0
            },
            {
                'name': 'PRUEBA DE CONTENEDORES  4 x 4 x 4',
                'input': ([4.0,4.0,4.0]),
                'expected_out': 64.0
            },
            {
                'name': 'PRUEBA DE CONTENEDORES  5 x 5 x 5',
                'input': ([5.0,5.0,5.0]),
                'expected_out': 125.0
            },
            {
                'name': 'PRUEBA DE CONTENEDORES  2 x 2 x 2',
                'input': ([2.0,2.0,2.0]),
                'expected_out': 8.0
            },
            {
                'name': 'PRUEBA DE CONTENEDORES  1 x 1 x 1',
                'input': [1.0,1.0,1.0],
                'expected_out': 1.0
            }
        ]
        for i in test_cases:
            actual=vol_calc(i['input'][0],i['input'][1],i['input'][2])
            self.assertEqual(actual,i['expected_out'])
    def test_totalVol(self):
        test_cases = [
            {
                'name': 'PRUEBA 3 contenedores de Volumen 1, 2 de 4 y 5 de 3',
                'input': ['3,1','2,4','5,3'],
                'expected_out':26.0
            },
            {
                'name': 'PRUEBA 4 contenedores de Volumen 2, 5 de 1 y 5 de 6',
                'input': ['4,2','5,1','5,6'],
                'expected_out':43.0
            },
            {
                'name': 'PRUEBA 2 contenedores de Volumen 2, 4 de 4 y 5 de 5',
                'input': ['2,2','4,4','5,5'],
                'expected_out':45.0
            }
        ]
        for i in test_cases:
            actual = total_vol(i['input'])
            self.assertEqual(actual,i['expected_out'])

    def test_savingstratUnit(self): #USANDO UN MOCK
        test_cases = [
            {
                'name': 'cajas de 1, 2 y 3 para un volumen de 100',
                'input': [[1,2,3],100],
                'expected':['(3,3)','(2,2)','(1,3)']
            },
            {
                'name': 'cajas de 2, 4 y 6 para un volumen de 500',
                'input': [[2,4,6],500],
                'expected':['(6,2)','(4,1)','(2,1)']
            },
            {
                'name': 'cajas de 1, 2 y 3 para un volumen de 200',
                'input': [[1,2,3],200],
                'expected':['(3,7)','(2,1)','(1,3)']
            }
        ]
        for i in test_cases:
            actual = saving_strat(i['input'][0],i['input'][1],vol_calcmock)
            self.assertEqual(actual,i['expected'])
    
    def test_savingstrat(self): ##INTEGRANDO FUNCIONES A USAR
        test_cases = [
            {
                'name': 'cajas de 1, 2 y 3 para un volumen de 100',
                'input': [[1,2,3],100],
                'expected':['(3,3)','(2,2)','(1,3)']
            },
            {
                'name': 'cajas de 2, 4 y 6 para un volumen de 500',
                'input': [[2,4,6],500],
                'expected':['(6,2)','(4,1)','(2,1)']
            },
            {
                'name': 'cajas de 1, 2 y 3 para un volumen de 200',
                'input': [[1,2,3],200],
                'expected':['(3,7)','(2,1)','(1,3)']
            }
        ]
        for i in test_cases:
            actual = saving_strat(i['input'][0],i['input'][1],vol_calc)
            self.assertEqual(actual,i['expected'])


if __name__ == '__main__':
    unittest.main()
