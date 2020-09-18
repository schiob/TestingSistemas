import unittest
from practica3_test import vendePantalones, pantalon

class practica2PantalonesTest(unittest.TestCase):

    def testinput_Chio(self):
        inputChio = [pantalon("Patito",4),
                    pantalon("Patito",5),
                    pantalon("Levice",15),
                    pantalon("Patito",5),
                    pantalon("Levice",3),
                    pantalon("Nike",20),
                    pantalon("Nike",18),
                    pantalon("Levice",4)]

        self.assertEqual(vendePantalones(8,5,inputChio),"3 40")

    def test_descartaPantalonesQuedateConUno(self):
        marcaInput = [pantalon("Nike",100),
                pantalon("Nike",100),
                pantalon("Kike",10),
                pantalon("Kike",10),
                pantalon("Kike",10)
                ]

        self.assertEqual(vendePantalones(5,3,marcaInput),"2 110")

    def test_pantalonesAVenderMayorQueActual(self):
        marcaInput = [pantalon("Nike",100),
                pantalon("Bike",110)
                ]

        self.assertEqual(vendePantalones(2,5,marcaInput),0)

    def test_venderTodosPantalones(self):
      marcaInput = [pantalon("Nike",100),
              pantalon("Bike",110)
              ]

      self.assertEqual(vendePantalones(2,0,marcaInput),0)

    def test_venderNingunPantalon(self):
      marcaInput = [pantalon("Nike",100),
              pantalon("Bike",110)
              ]

      self.assertEqual(vendePantalones(2,2,marcaInput),"0 0")

if __name__ == "__main__":
    unittest.main()
    
