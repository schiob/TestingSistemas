#Tomen el código de la práctica 2 y hagan las adecuaciones necesarias para poder correr pruebas unitarias sobre la lógica de su solución.

#Probablemente sea necesario que tengan que modificar un poco el código original de su solución, encapsularlo en alguna función o separar la entrada e impresión de datos.

#Pueden utilizar unittest o pytest para hacer las pruebas unitarias, y traten de seleccionar un buen número de casos de prueba para cubrir la mayor parte del domino del problema.


import unittest
from Practica3 import vendePantalones, pantalon

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