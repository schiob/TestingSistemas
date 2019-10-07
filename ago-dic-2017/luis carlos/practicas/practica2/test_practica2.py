import unittest
from practica2 import RegresaString
from practica2 import recibe
class practica2(unittest.TestCase):
    def setUp(self):
        tacos=open("holatacos.txt","w")
        tacos.write('hola tacos')
        tacos.close()

        vacio=open("vacio.txt","w")
        vacio.write('')
        vacio.close()

        saltos=open("saltos.txt","w")
        saltos.write('\nhola\nsalto\ntamal')
        saltos.close()

        nuevo=open("nuevo.txt","w")
        nuevo.write('')
        nuevo.close

    def test_tacos(self):
        self.assertEqual(RegresaString("holatacos.txt"),'hola tacos')

    def test_vacio(self):
        self.assertEqual(RegresaString("vacio.txt"),'')

    def test_saltos(self):
        self.assertEqual(RegresaString("saltos.txt"),'\nhola\nsalto\ntamal')

    def test_charmander(self):
        self.assertEqual(recibe("nuevo.txt","charmander"),'charmander')
    def test_viernes(self):
        self.assertEqual(recibe("nuevo.txt",'ya es viernes'),'ya es viernes')

if __name__ =='__main__':
    unittest.main()
