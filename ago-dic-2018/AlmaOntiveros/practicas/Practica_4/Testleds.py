import unittest
import Practica4

class Testleds(unittest.TestCase):
    def test_leds(self):
#CasodePrueba1
        resultado= Leds.focosleds(1)
        self.assertEqual(resultado,2)

#CasodePrueba2
        resultado= Leds.focosleds(32)
        self.assertEqual(resultado,10)

#CasodePrueba3
        resultado= Leds.focosleds(8888)
        self.assertEqual(resultado,28)

#CasodePrueba4
        resultado= Leds.focosleds(115380)
        self.assertEqual(resultado,27)

#CasodePrueba5
        resultado= Leds.focosleds(2819311)
        self.assertEqual(resultado,29)

#CasodePrueba6
        resultado= Leds.focosleds(23456)
        self.assertEqual(resultado,25)

if __name__ == '__main__':
    unittest.main()