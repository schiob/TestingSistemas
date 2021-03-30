import unittest

from practica_cinco import censurar, validar

class Test_practica_cinco(unittest.TestCase):
    def test_censura(self):
        self.assertEqual(censurar(['popo', 'sangre', 'muerte', 'maldito'],'El animal maldito se acercó con una mirada de muerte. Manchas de sangre cubrían el suelo','kawai'),'El animal kawai se acercó con una mirada de kawai. Manchas de kawai cubrían el suelo')
        self.assertCountEqual(censurar(['maldito','bomba'],'El maldito dejo una bomba','---'),'El --- dejo una ---')
        
        
    def test_validar(self):
        censuras=(
                ['tonto','fuck','alv'],
                ['coño','maldito','shit'],
                ['muerte','popo','sangre']
            )
        texto='tonto fuck alv coño muerte popo maldito'
        for i in censuras:
            lista=[i[0],i[1],i[2]]
            r = validar(lista,texto,'kawai',10)
            self.assertEqual(r,"Es valido")
        
        for t in censuras:
            listas=[t[0],t[1]]
            re = validar(listas,texto,'########',1)
            self.assertEqual(re,'No es valido')
        
        
if __name__ == '__main__' :
    unittest.main()