import unittest
from practica_5 import funcion_1

class Pruebas (unittest.TestCase):

    def Pruebas_practica_5(self):

        # Los primeros 3 parametros son dados, el 4to parametro en la tupla es el resultado de los Tests
        tc = (
            [(["popo", "sangre", "muerte", "maldito"], "El animal maldito se acercó con una mirada de muerte. Manchas de sangre cubrían el suelo", "kawai"), "El animal kawai se acercó con una mirada de kawai. Manchas de kawai cubrían el suelo"]
        )
        tc_2 = (
            [(["popo", "sangre", "muerte", "maldito"], "El animal maldito se acercó con una mirada de muerte. Manchas de sangre cubrían el suelo", "kawai", 5), "El animal kawai se acercó con una mirada de kawai. Manchas de kawai cubrían el suelo"]
        )
        for caso in tc:
            self.assertEquals(funcion_1(caso[0]),caso[1])

        for caso in tc_2:
            self.assertEquals(funcion_1(caso[0],caso[1]))
if __name__ == '__main__':
    unittest.main()