import unittest
from practica3 import practica3
class test_p3(unittest.TestCase):
    def test_ni_idea(self):
        lista=[[(51, -12, -3, 0, 2),
        '''2 número(s) positivo(s)\n2 número(s) negativo(s)\n3 número(s) par(es)\n2 número(s) impar(es)'''],
        [(0, 1, 2, 3, 4),
        '''4 número(s) positivo(s)\n0 número(s) negativo(s)\n3 número(s) par(es)\n2 número(s) impar(es)'''],
        [(-1, -2, -3),
         '''0 número(s) positivo(s)\n3 número(s) negativo(s)\n1 número(s) par(es)\n2 número(s) impar(es)'''],
        [(0),
         '''0 número(s) positivo(s)\n0 número(s) negativo(s)\1 número(s) par(es)\0 número(s) impar(es)'''] 
        ]

        for i in range(0,len(lista)-1,1):
            resultado=(practica3(len(lista[i][0]) , lista[i][0]))
            self.assertEqual(resultado,lista[i][1])

if __name__ =='__main__':
 unittest.main()