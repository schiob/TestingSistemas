import unittest
from triangulo3 import tipo_de_triangulo

class TestTrian(unittest.TestCase):
    def Test_Triangulo(self):

        prueba = (
              [3,3,3, "Equilatero"],   
              [3,2,3, "Isoseles"],
              [0,0,0, "No triangulo"],
              [7,1,8, "No trinagulo"],
              [5,7,9, "Escaleno"],
              [3,-2,0, "No triangulo"],
              ["quiero morir",3,3, "No triangulo"],
              [16,None,18, "No triangulo"]
          )

        for tc in prueba:
            self.assertEqual(tipo_de_triangulo(tc[0], tc[1], tc[2]), tc[3])     

if __name__ == "__main__":    
    unittest.main()