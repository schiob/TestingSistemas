import unittest
from practica3 import juanita, numerosImpares, numerosPares, numerosNegativos, numerosPositivos

class practica3_test(unittest.TestCase):

    def test_primero(self):
        entrada = [51, -12, -3, 0, 2]
        salidaEsperada = [2, 2, 3, 2]
        resultados = []
        resultados.append(numerosPositivos(entrada))
        resultados.append(numerosNegativos(entrada))
        resultados.append(numerosPares(entrada))
        resultados.append(numerosImpares(entrada))
        print('Resultados', resultados)
        self.assertEqual(resultados, salidaEsperada)

    def test_segundo(self):
        entrada = [0, 1, 2, 3, 4]
        salidaEsperada = [4, 0, 3, 2]
        resultados = []
        resultados.append(numerosPositivos(entrada))
        resultados.append(numerosNegativos(entrada))
        resultados.append(numerosPares(entrada))
        resultados.append(numerosImpares(entrada))
        print('\nResultados', resultados)
        self.assertEqual(resultados, salidaEsperada)

    def test_tercero(self):
        entrada = [-1, -2, -3]
        salidaEsperada = [0, 3, 1, 2]
        resultados = []
        resultados.append(numerosPositivos(entrada))
        resultados.append(numerosNegativos(entrada))
        resultados.append(numerosPares(entrada))
        resultados.append(numerosImpares(entrada))
        print('\nResultados', resultados)
        self.assertEqual(resultados, salidaEsperada)

    def test_cuarto(self):
        entrada = [0]
        salidaEsperada = [0, 0, 1, 0]
        resultados = []
        resultados.append(numerosPositivos(entrada))
        resultados.append(numerosNegativos(entrada))
        resultados.append(numerosPares(entrada))
        resultados.append(numerosImpares(entrada))
        print('\nResultados', resultados)
        self.assertEqual(resultados, salidaEsperada)

        


if __name__ == '__main__':
        unittest.main()