import unittest

from practica2editada import getData
from practica2editada import sortPants
from practica2editada import getCandidates
from practica2editada import tryToSell

class TestGetData(unittest.TestCase):
    def setUp(self):
        #Caso satisfactorio
        self.entrada_N = 8
        self.entrada_X = 5
        self.entrada_cSolds = self.entrada_N - self.entrada_X
        self.pants = [{'ptype': 'Patito', 'price': 4},
        {'ptype': 'Patito', 'price': 5},
        {'ptype': 'Levice', 'price': 15},
        {'ptype': 'Patito', 'price': 5},
        {'ptype': 'Levice', 'price': 3},
        {'ptype': 'Nike', 'price': 20},
        {'ptype': 'Nike', 'price': 18},
        {'ptype': 'Levice', 'price': 4}]

        #Caso satisfactorio
        self.entrada_N2 = 6
        self.entrada_X2 = 3
        self.entrada_cSolds2 = self.entrada_N2 - self.entrada_X2
        self.pants2 = [{'ptype': 'Patito', 'price': 4},
        {'ptype': 'Patito', 'price': 5},
        {'ptype': 'Levice', 'price': 15},
        {'ptype': 'Patito', 'price': 5},
        {'ptype': 'Levice', 'price': 3},
        {'ptype': 'Nike', 'price': 20}]

        #Caso satisfactorio
        self.entrada_N3 = 4
        self.entrada_X3 = 2
        self.entrada_cSolds3 = self.entrada_N3 - self.entrada_X3
        self.pants3 = [{'ptype': 'Patito', 'price': 4},
        {'ptype': 'Patito', 'price': 5},
        {'ptype': 'Levice', 'price': 15},
        {'ptype': 'Patito', 'price': 5}]

        #Caso fallido, quiere vender 1, pero solo tiene 1 pantalon de cada marca y una de las reglas
        #  es que se debe quedar con por lo menos 1 pantalon de cada marca
        self.entrada_N4 = 4
        self.entrada_X4 = 3
        self.entrada_cSolds4 = self.entrada_N4 - self.entrada_X4
        self.pants4 = [{'ptype': 'CCP', 'price': 4},
        {'ptype': 'Patito', 'price': 5},
        {'ptype': 'Levice', 'price': 15},
        {'ptype': 'Nike', 'price': 5}]

        #Caso fallido, quiere vender 6 pantalones, y aun que tiene los suficientes todos son de la
        #misma marca y una de las reglas es que no puede vender más de 5 pantalones de cada marca
        self.entrada_N5 = 7
        self.entrada_X5 = 1
        self.entrada_cSolds5 = self.entrada_N5 - self.entrada_X5
        self.pants5 = [{'ptype': 'Patito', 'price': 4},
        {'ptype': 'Patito', 'price': 5},
        {'ptype': 'Patito', 'price': 2},
        {'ptype': 'Patito', 'price': 8},
        {'ptype': 'Patito', 'price': 10},
        {'ptype': 'Patito', 'price': 9},
        {'ptype': 'Patito', 'price': 5}]
        

    def test_data(self):
        salida_esperada = getData(self.entrada_N,self.entrada_X,self.pants)
        salida_real = {
            "N": self.entrada_N,
            "X": self.entrada_X,
            "pants": self.pants
        }

        self.assertEqual(salida_real, salida_esperada)

        salida_esperada2 = getData(self.entrada_N2,self.entrada_X2,self.pants2)
        salida_real2 = {
            "N": self.entrada_N2,
            "X": self.entrada_X2,
            "pants": self.pants2
        }

        self.assertEqual(salida_real2, salida_esperada2)

        salida_esperada3 = getData(self.entrada_N3,self.entrada_X3,self.pants3)
        salida_real3 = {
            "N": self.entrada_N3,
            "X": self.entrada_X3,
            "pants": self.pants3
        }

        self.assertEqual(salida_real3, salida_esperada3)

        salida_esperada4 = getData(self.entrada_N4,self.entrada_X4,self.pants4)
        salida_real4 = {
            "N": self.entrada_N4,
            "X": self.entrada_X4,
            "pants": self.pants4
        }

        self.assertEqual(salida_real4, salida_esperada4)

        salida_esperada5 = getData(self.entrada_N5,self.entrada_X5,self.pants5)
        salida_real5 = {
            "N": self.entrada_N5,
            "X": self.entrada_X5,
            "pants": self.pants5
        }

        self.assertEqual(salida_real5, salida_esperada5)

    def test_sort(self):

        salida_esperadasort1 = sortPants(self.pants)
        salida_realsort1 = [{'ptype': 'Patito', 'price': 5},
        {'ptype': 'Patito', 'price': 5},
        {'ptype': 'Patito', 'price': 4},
        {'ptype': 'Nike', 'price': 20},
        {'ptype': 'Nike', 'price': 18},
        {'ptype': 'Levice', 'price': 15},
        {'ptype': 'Levice', 'price': 4},
        {'ptype': 'Levice', 'price': 3}]
    
        self.assertEqual(salida_realsort1, salida_esperadasort1)

        salida_esperadasort2 = sortPants(self.pants2)
        salida_realsort2 = [{'ptype': 'Patito', 'price': 5},
        {'ptype': 'Patito', 'price': 5},
        {'ptype': 'Patito', 'price': 4},
        {'ptype': 'Nike', 'price': 20},
        {'ptype': 'Levice', 'price': 15},
        {'ptype': 'Levice', 'price': 3}]

        self.assertEqual(salida_realsort2, salida_esperadasort2)

        salida_esperadasort3 = sortPants(self.pants3)
        salida_realsort3 = [{'ptype': 'Patito', 'price': 5},
        {'ptype': 'Patito', 'price': 5},
        {'ptype': 'Patito', 'price': 4},
        {'ptype': 'Levice', 'price': 15}]

        self.assertEqual(salida_realsort3, salida_esperadasort3)

        salida_esperadasort4 = sortPants(self.pants4)
        salida_realsort4 = [{'ptype': 'Patito', 'price': 5},
        {'ptype': 'Nike', 'price': 5},
        {'ptype': 'Levice', 'price': 15},
        {'ptype': 'CCP', 'price': 4}]

        self.assertEqual(salida_realsort4, salida_esperadasort4)

        salida_esperadasort5 = sortPants(self.pants5)
        salida_realsort5 = [{'ptype': 'Patito', 'price': 10},
        {'ptype': 'Patito', 'price': 9},
        {'ptype': 'Patito', 'price': 8},
        {'ptype': 'Patito', 'price': 5},
        {'ptype': 'Patito', 'price': 5},
        {'ptype': 'Patito', 'price': 4},
        {'ptype': 'Patito', 'price': 2}]
    
        self.assertEqual(salida_realsort5, salida_esperadasort5)

    def test_getCandidates(self):
        salida_esperadagC = getCandidates(sortPants(self.pants))
        salida_realgC = [{'ptype': 'Patito', 'price': 5},
        {'ptype': 'Patito', 'price': 5},
        {'ptype': 'Nike', 'price': 20},
        {'ptype': 'Levice', 'price': 15},
        {'ptype': 'Levice', 'price': 4}]
        
        self.assertEqual(salida_esperadagC, salida_realgC)

        salida_esperadagC2 = getCandidates(sortPants(self.pants2))
        salida_realgC2 = [{'ptype': 'Patito', 'price': 5},
        {'ptype': 'Patito', 'price': 5},
        {'ptype': 'Levice', 'price': 15}]

        self.assertEqual(salida_esperadagC2, salida_realgC2)

        salida_esperadagC3 = getCandidates(sortPants(self.pants3))
        salida_realgC3 = [{'ptype': 'Patito', 'price': 5},
        {'ptype': 'Patito', 'price': 5}]

        self.assertEqual(salida_esperadagC3, salida_realgC3)

        salida_esperadagC4 = getCandidates(sortPants(self.pants4))
        salida_realgC4 = []

        self.assertEqual(salida_esperadagC4, salida_realgC4)

        salida_esperadagC5 = getCandidates(sortPants(self.pants5))
        salida_realgC5 = [{'ptype': 'Patito', 'price': 10},
        {'ptype': 'Patito', 'price': 9},
        {'ptype': 'Patito', 'price': 8},
        {'ptype': 'Patito', 'price': 5},
        {'ptype': 'Patito', 'price': 5}]

        self.assertEqual(salida_esperadagC5, salida_realgC5)

    def test_trytosell(self):
        salida_esperadatts = tryToSell(self.entrada_cSolds, getCandidates(sortPants(self.pants)))
        salida_realtts = 40

        self.assertEqual(salida_esperadatts, salida_realtts)

        salida_esperadatts2 = tryToSell(self.entrada_cSolds2, getCandidates(sortPants(self.pants2)))
        salida_realtts2 = 25

        self.assertEqual(salida_esperadatts2, salida_realtts2)

        salida_esperadatts3 = tryToSell(self.entrada_cSolds3, getCandidates(sortPants(self.pants3)))
        salida_realtts3 = 10

        self.assertEqual(salida_esperadatts3, salida_realtts3)

        salida_esperadatts4 = tryToSell(self.entrada_cSolds4, getCandidates(sortPants(self.pants4)))
        salida_realtts4 = 0

        self.assertEqual(salida_esperadatts4, salida_realtts4)

        salida_esperadatts5 = tryToSell(self.entrada_cSolds5, getCandidates(sortPants(self.pants5)))
        salida_realtts5 = 0

        self.assertEqual(salida_esperadatts5, salida_realtts5)

    def tearDown(self):
        del(self.entrada_N)
        del(self.entrada_N2)
        del(self.entrada_N3)
        del(self.entrada_N4)
        del(self.entrada_N5)
        del(self.entrada_X)
        del(self.entrada_X2)
        del(self.entrada_X3)
        del(self.entrada_X4)
        del(self.entrada_X5)
        del(self.entrada_cSolds)
        del(self.entrada_cSolds2)
        del(self.entrada_cSolds3)
        del(self.entrada_cSolds4)
        del(self.entrada_cSolds5)
        del(self.pants)
        del(self.pants2)
        del(self.pants3)
        del(self.pants4)
        del(self.pants5)


if __name__ == '__main__':
    unittest.main()