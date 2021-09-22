import unittest
from taquitos import orden


class testTaquitos(unittest.TestCase):
    def testUnTacoDeCada(self):
        prueba = orden('cachete lengua tripitas pastor machito')
        self.assertEqual(prueba, 'Van a ser: $61 mas propina joven')

    def testCincoDePastor(self):
        prueba = orden('pastor pastor pastor pastor pastor')
        self.assertEqual(prueba, 'Van a ser: $75 mas propina joven')

    def testDosDeMaciza(self):
        prueba = orden('maciza maciza')
        self.assertEqual(prueba, 'Van a ser: $0 mas propina joven')
        # DADO QUE NO HAY DE MACIZA PUES NO SE LE COBRA NADA:(

    def testTresMachitoUnoLengua(self):
        prueba = orden('machito machito machito lengua')
        self.assertEqual(prueba, 'Van a ser: $52 mas propina joven')

    def testUnTacoNoEnMenu(self):
        prueba = orden('machito cachete pastor tripitas barbacoa')
        self.assertEqual(prueba, 'Van a ser: $51 mas propina joven')
        # DADO QUE NO HAY DE BARBACOA NO SE LE COBRA

    def testMas30Tacos(self):
        prueba = orden('machito cachete pastor tripitas machito cachete pastor tripitas machito cachete pastor tripitas machito cachete pastor tripitas machito cachete pastor tripitas machito cachete pastor tripitas machito cachete pastor tripitas machito cachete pastor tripitas')
        self.assertEqual(prueba, 'Hasta un maximo de 30 tacos por orden')

    def testCeroTacos(self):
        prueba = orden('')
        self.assertEqual(prueba, 'Minimo un taco por orden')

    def testOrdenGithub(self):
        prueba = orden(
            'cachete lengua cachete tripitas machito machito machito cachete lengua')
        self.assertEqual(prueba, 'Van a ser: $110 mas propina joven')


if __name__ == '__main__':
    unittest.main()
