import unittest
from promedios import avg


usuario,correo,puntos
Tom,tomas@hotmail.com,85
Juan,juan@hotmail.com,75
Maria,maria84@gmail.com,90
Paco,paquito123@outlook.com,74
Ana,anaa22@gmail.com,88
Marcos,marcosss@hotmail.com,92

class TestPromedios(unittest.TestCase):
    def test_promedios_csv(self, mocksito):
        cases = [ ("Tom,tomas@hotmail.com", 85, 75),
                    ("Juan,juan@hotmail.com",85, 75),
                        ("Maria,maria84@gmail.com",85, 75 ),
                            ("Paco,paquito123@outlook.com",85, 75),
                                ("Marcos,marcosss@hotmail.com",85, 75)]

        for i, mocktxt, esp in cases:
            integers = avg(i)
            mocksito.text = mocktxt
            self.assertEqual(integers, esp)



if __name__=="__main__":
    unittest.main()