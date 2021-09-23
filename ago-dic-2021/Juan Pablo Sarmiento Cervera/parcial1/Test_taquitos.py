import unittest
from taquitos import orden

class testTaquitos(unittest.TestCase):
    def testOrdenEjemplu(self):
        prueba = orden('cachete lengua cachete tripitas machito machito machito cachete lengua')
        self.assertEqual(prueba, 'En total serian: $110 ')
    def testMasDe30Ordenes(self):
        prueba = orden('machito cachete pastor tripitas machito cachete pastor tripitas machito cachete pastor pastor pastor pastor cachete pastor tripitas machito pastor pastor tripitas machito cachete pastor tripitas pastor cachete pastor tripitas machito cachete pastor tripitas bistek pastor lengua')
        self.assertEqual(prueba, 'Hasta un maximo de 30 ordenes por favor')
    def testNoOrden(self):
        prueba = orden('')
        self.assertEqual(prueba, 'Minimo una orden')
    def testCincoDePastor(self):
        prueba = orden('pastor pastor pastor pastor pastor')
        self.assertEqual(prueba, 'En total serian: $75 ')
    def testOrdenDeCada(self):
        prueba = orden('cachete lengua tripitas pastor machito')
        self.assertEqual(prueba, 'En total serian: $61 ')    
    def testDosMachitoUnPastorUnLengua(self):
        prueba = orden('machito pastor machito lengua')
        self.assertEqual(prueba, 'En total serian: $53 ')
    def testUnTacoNoExistente(self):
        prueba = orden('machito cachete pastor tripitas bistek')
        self.assertEqual(prueba, 'En total serian: $51 ')
    

if __name__ == '__main__':
    unittest.main()

#Ahora si toca llorar :'(:'C:'(:'C:'(:'C:'(:'C:'(:'C
#Si me va vien entonces el analisar las tareas y repasar 6 veces las clases si sirve (ademas de provocar migrañas y ganas de llorar)