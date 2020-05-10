import unittest
from censura import *
##BOTTOM UP
class censura_test(unittest.TestCase):
    def test_censor(self):
        black_list = ['popo','sangre','muerte','maldito']
        test_case = [
            {
                'input':['La popo','kawai'],
                'expected':'La kawai'
            },
            {
                'input':['La muerte','Bad word'],
                'expected':'La Bad word'
            },
            {
                'input':['La muerte de la popo','*'],
                'expected':'La ****** de la ****'
            },
            {
                'input':['La amiga de la popo','NOPE'],
                'expected':'La amiga de la NOPE'
            },
            {
                'input':['La muerte, amarga','falta de vida'],
                'expected':'La falta de vida, amarga'
            },
            {
                'input':['La sangre del maldito, es peor que la muerte','*'],
                'expected':'La ****** del *******, es peor que la ******'
            },
        ]
        for i in test_case:
            actual = censura(black_list,i['input'][0],i['input'][1])
            self.assertEqual(actual,i['expected'])

    def test_validUnit(self):
        test_cases=[
            {
                'in1':"hola dude",
                'in2':"**** dude",
                'ml': 3,
                'expected': True
            },
            {
                'in1':"hola dude",
                'in2':"****** dude",
                'ml': 1,
                'expected': False
            },
            {
                'in1':"hola dude",
                'in2':"***** dude",
                'ml': 1,
                'expected': True
            },
            {
                'in1':"hola dude",
                'in2':"**** dudeasdasdasd",
                'ml': 4,
                'expected': False
            },
            {
                'in1':"hola dude",
                'in2':"****  dude",
                'ml': 0,
                'expected': False
            }
        ]
        for i in test_cases:
            actual=validar(i['in1'],i['in2'],i['ml'])
            self.assertEqual(actual,i['expected'])

    def test_validInteg(self):
        black_list = ['popo','sangre','muerte','maldito','ex']
        test_cases=[
            {
                'in': 'La popo',
                'n_word': '*', #Refiriendose a new word, no a la otra palabra con n
                'ml':5,
                'ex':True
            },
            {
                'in': 'La popo de mi ex olia a rosas',
                'n_word': 'sadness',
                'ml':5,
                'ex':False
            },
            {
                'in': 'La muerte es popo',
                'n_word': '*',
                'ml':1,
                'ex':True
            },
            {
                'in': 'La popo es cool',
                'n_word': 'coca-cola',
                'ml':100,
                'ex':True
            },
            {
                'in': 'La katsup',
                'n_word': '*',
                'ml':0,
                'ex':True
            }
        ]
        for i in test_cases:
            actual=validar(i['in'],censura(black_list,i['in'],i['n_word']),i['ml'])
            self.assertEqual(actual,i['ex'])
if __name__=='__main__':
    unittest.main()