import unittest
from Practica_5 import censurador, Limite

class Pruebas (unittest.TestCase):

    def TestPractica_5(self):

        Test1 = (
            [(["popo", "sangre", "muerte", "maldito"], "El animal maldito se acercó con una mirada de muerte. Manchas de sangre cubrían el suelo", "kawai"), "El animal kawai se acercó con una mirada de kawai. Manchas de kawai cubrían el suelo"]
        )
        Test2 = (
            [(["popo", "sangre", "muerte", "maldito"], "El animal maldito se acercó con una mirada de muerte. Manchas de sangre cubrían el suelo", "kawai", 5), "Valido"],
            [(["popo", "sangre", "muerte", "maldito"], "El animal maldito se acercó con una mirada de muerte. Manchas de sangre cubrían el suelo", "YAMETEKUDASAYYYYYYYY", 20), "No Valido"],
            [(["popo", "sangre", "muerte", "maldito"], "El animal maldito se acercó con una mirada de muerte. Manchas de sangre cubrían el suelo", "404 404 404", 12), "NO Valido"],
            [(["popo", "sangre", "muerte", "maldito"], "El animal maldito se acercó con una mirada de muerte. Manchas de sangre cubrían el suelo", "*****",5), "Valido"],
            [(["popo", "sangre", "muerte", "maldito"], "El animal maldito se acercó con una mirada de muerte. Manchas de sangre cubrían el suelo", "numnumnum",9 ), "No Valido"]
        )
        for caso1 in Test1:
            self.assertEquals(censurador(caso1[0]),caso1[1])

        for caso2 in Test2:
            self.assertEquals(Limite(caso2[0]),caso2[1],caso2[2])

if __name__ == '__main__':
    unittest.main() 