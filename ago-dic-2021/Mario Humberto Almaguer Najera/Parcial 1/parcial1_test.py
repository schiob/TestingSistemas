import unittest
from parcial1 import total_pagar


class parcial1_test(unittest.TestCase):

    def test(self):
        test_cases = [
            {
                'nombre': 'Cero tacos de orden',
                'entrada': [''],
                'salida_esperada': 'El/Un taco no existe',
                'error_esperado': False,
            },

            {
                'nombre': 'El matahambre: 1 taco de orden',
                'entrada': ['Cachete'],
                'salida_esperada': 13, #13
                'error_esperado': False,
            },

            {
                'nombre': 'Orden normal: 5 tacos de orden',
                'entrada': ['Cachete', 'Lengua', 'Machito', 'Tripitas', 'Pastor'],
                'salida_esperada': 61, #61
                'error_esperado': False,
            },

            {
                #Este caso se espera que de error porque solo se aceptan 30 tacos como maximo segun GitHub.
                'nombre': 'El hambriento: 31 tacos de orden',
                'entrada': ['Cachete'] * 31,
                'salida_esperada': 'Solo se aceptan 30 tacos como maximo.',
                'error_esperado': False,
            },

            {
                #Este caso se espera que de error porque el taco de "Serpiente" no existe en el menu.
                'nombre': 'El raro: 4 tacos del menu y 1 raro',
                'entrada': ['Cachete', 'Lengua', 'Tripitas', 'Pastor', 'Serpiente'],
                'salida_esperada': 'El/Un taco no existe',
                'error_esperado': False
            }
        ]

        for tc in test_cases:
            if tc['error_esperado']:
                self.assertRaises(Exception, total_pagar, tc['entrada'][0])
            else:
                resultado = total_pagar(tc['entrada'])
                self.assertEqual(
                    resultado, tc['salida_esperada'], msg='Falla en el test {}, entrada {}, salida esperada {}, salida real {}'.format(tc['nombre'], tc['entrada'], tc['salida_esperada'], resultado))


if __name__ == '__main__':
    unittest.main()
