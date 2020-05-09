import unittest
from Censura import censura

class TestCensura(unittest.TestCase):
    
    def setUp(self):
        print("Preparando el contexto...")
        self.texto = input("Escriba el texto a censurar: ")
        self.palabras = ["popo","sangre","muerte","maldito"]
        self.magicword = "NOPE"
    
    
    def test_textcensored(self):
        entrada = self.texto
        salida_esperada = "la NOPE tiene mucha NOPE"
        salida_real = censura.censored(self.palabras,self.texto,self.magicword)
        
        self.assertEqual(salida_esperada,salida_real)
    
    def tearDown(self):
        print("Destruyendo el contexto...")
        del(self.texto)
        del(self.magicword)
        del(self.palabras)

if __name__ == "__main__":
    unittest.main()