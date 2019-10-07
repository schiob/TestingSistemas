import unittest
from grading_students import solve

class TestGrading(unittest.TestCase):

    # Caso con calificaciones mixtas.
    def testMix(self):
        self.assertEqual(solve([73, 67, 38, 33]), [75, 67, 40, 33])

    # Caso donde ninguna calificacion se redondea.
    def testNoRound(self):
        self.assertEqual(solve([97, 62, 57, 33]), [97, 62, 57, 33])

    # Caso ningun alumno pasa.
    def testTuNoPasaras(self):
        self.assertEqual(solve([27, 20, 12, 33]), [27, 20, 12, 33])

    # Caso donde todos pasan a base de sobornos.
    def testTodosPasan(self):
        self.assertEqual(solve([57, 98, 40, 83]), [57, 100, 40, 85])


if __name__ == '__main__':
    unittest.main()
