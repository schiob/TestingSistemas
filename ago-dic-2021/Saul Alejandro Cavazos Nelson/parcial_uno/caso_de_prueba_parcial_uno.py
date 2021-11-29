import unittest
from parcial_uno import parcial_uno
class test_parcial_uno(unittest.TestCase):
    def test_1 (self):
        entrada = [[110,"cachete lengua cachete tripitas machito machito machito cachete lengua"],
           [360,"cachete lengua cachete tripitas machito machito machito cachete lengua cachete lengua cachete tripitas machito machito machito cachete lengua cachete lengua cachete tripitas machito machito machito cachete lengua lengua lengua lengua"],
           [0,"ojo queso papas perro"],
           [0,' '],
           [300,"lengua lengua lengua lengua lengua lengua lengua lengua lengua lengua lengua lengua lengua lengua lengua lengua lengua lengua lengua lengua lengua lengua lengua lengua lengua lengua lengua lengua lengua lengua"],
           [10,"lengua papa"],
           [110,"cachete lengua cachete tripitas machito machito machito cachete lengua papa"],
           [0,"1 2 3"],
           [13,'cachete'],
           [10,'lengua'],
           [9,'tripitas'],
           [15,'pastor'],
           [14,'machito'],
           [0,"cachete lengua cachete tripitas machito machito machito cachete lengua cachete lengua cachete tripitas machito machito machito cachete lengua cachete lengua cachete tripitas machito machito machito cachete lengua lengua lengua lengua lengua"],
           [61,"machito pastor tripitas lengua cachete" ],
           [46,"machito tripitas lengua cachete" ],
           [47,"pastor tripitas lengua cachete" ],
           [51,"machito pastor tripitas cachete" ],
           [48,"machito pastor tripitas lengua"],
           [52,"machito pastor lengua cachete" ],
           [0,"1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30"],
           [0,"1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31"],
           [0,"cachete lengua cachete tripitas machito machito machito cachete lengua cachete lengua cachete tripitas machito machito machito cachete lengua cachete lengua cachete tripitas machito machito machito cachete lengua lengua lengua lengua PAPA"]      
           ]
           
        for i in range(0,len(entrada),1):
            resultado=parcial_uno(entrada[i][1])
            self.assertEqual(resultado,entrada[i][0])

if __name__ =='__main__':
 unittest.main()
