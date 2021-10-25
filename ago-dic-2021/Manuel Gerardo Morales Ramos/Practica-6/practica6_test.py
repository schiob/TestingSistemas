from test_cases import *
from mocks import MockInput
import practica6
import unittest

def make_list(data: str) -> list[str]:
    final_list = []
    for line in data.split('\n'):
        aux = line.split(' ')
        final_list.append(
            '{} {}'.format(aux[0], aux[1])
        )

    return final_list

class TestPractica6(unittest.TestCase):
    def test_siguiente_usuario(self):
        for test in sig_usuario_test_cases:
            if test['expected_raise']:
                self.assertRaises(Exception, practica6.siguiente_usuario, test["input"])
            else:
                users_mock = MockInput(test['input'])
                users = make_list(users_mock.Read())
                
                got = practica6.siguiente_usuario(users)
                self.assertEqual(got, test['expected_output'])

    def test_viajes_disponibles(self):
        for test in viajes_disponibles_test_cases:
            if test['expected_raise']:
                self.assertRaises(Exception, practica6.viajes_disponibles, MockInput(test['input']))
            else:
                travels_mock = MockInput(test['input'])
                got = practica6.viajes_disponibles(travels_mock)
                
                self.assertEqual(got, test['expected_output'])

    def test_extraer_conductores(self):
        for test in extraer_conductores_test_cases:
            if test['expected_raise']:
                self.assertRaises(Exception, practica6.extraer_conductores, MockInput(test['input']))
            else:
                travels_mock = MockInput(test['input'])
                got = practica6.extraer_conductores(travels_mock)

                self.assertEqual(got, test['expected_output'])

    def test_calcular_tarifa(self):
        for test in calcular_tarifa_test_cases:
            if test['expected_raise']:
                self.assertRaises(Exception, practica6.calcuar_tarifa, MockInput(test['input']))
            else:
                got = practica6.calcuar_tarifa(test['input'])

                self.assertEqual(got, test['expected_output'])

    def test_funcion_prinicpal(self):
        for test in funcion_principal_test_cases:
            if test['expected_raise']:
                self.assertRaises(Exception, practica6.funcion_principal, MockInput(test['input']), MockInput(test['input2']))
            else:
                users_mock = MockInput(test['input'])
                travels_mock = MockInput(test['input2'])

                got = practica6.funcion_principal(users_mock, travels_mock)

                self.assertEqual(got, test['expected_output'])
                
if __name__ == '__main__':
    unittest.main()
