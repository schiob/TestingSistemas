from datetime import datetime
import unittest
import Examen12to24

class Test_12to24(unittest.TestCase):

    formato = "%H:%M:%S"
    h1 = datetime.strptime("02:23:00", formato)
    h2 = datetime.strptime("11:42:00", formato)
    h3 = datetime.strptime("11:42:00", formato)
    h4 = datetime.strptime("12:00:00", formato)
    h5 = datetime.strptime("12:00:00", formato)
    h6 = datetime.strptime("01:05:00", formato)
    h7 = datetime.strptime("11:59:00", formato)



    def Test_12to24(self):
        hr2 = datetime.strptime("14:23:00", formato)
        hr2 = datetime.strptime("23:43:00", formato)
        hr3 = datetime.strptime("11:43:00", formato)
        hr4 = datetime.strptime("00:00:00", formato)
        hr5 = datetime.strptime("12:00:00", formato)
        hr6 = datetime.strptime("01:05:00", formato)
        hr7 = datetime.strptime("23:59:00", formato)
        resultado2=Examen12to24.convertirHora(['pm','pm','am','am','pm','am','pm'])
        resultado=Examen12to24.convertirHora([h1,h2,h3,h4,h5,h6.h7])

        self.assertEqual(resultado [1],hr1
        self.assertEqual(resultado [1],hr2)
        self.assertEqual(resultado [2],hr3)
        self.assertEqual(resultado [3],hr4)
        self.assertEqual(resultado [4],hr5)
        self.assertEqual(resultado [5],hr6)
        self.assertEqual(resultado [6],hr7)
        self.assertEqual(resultado [7],hr8)

if __name__ == "__main__":
    unittest.main()
