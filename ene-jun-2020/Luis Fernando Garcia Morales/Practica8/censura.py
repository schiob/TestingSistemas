import unittest
def censura(lista, texto, palabra):
    lista = [i.lower() for i in lista]
    texto = texto.lower()
    for i in lista:
        if i in texto:
            texto = texto.replace(i, palabra)
    texto = ". ".join(i.capitalize() for i in texto.split(". "))
    return texto

class TestCensura(unittest.TestCase):
    def testText(self):

        testCases = [{
            "lista":["popo", "sangre", "muerte", "maldito"],
            "texto":"El animal maldito se acercó con una mirada de muerte. Manchas de sangre cubrían el suelo",
            "palabra":"kawai",
            "salida_esperada":"El animal kawai se acercó con una mirada de kawai. Manchas de kawai cubrían el suelo"
        },
        {
            "lista":["popo", "sangre", "muerte", "maldito"],
            "texto":"El animal MaLdItO se acercó con una mirada de MuERtE. Manchas de SanGrE cubrían el suelo",
            "palabra":"kawai",
            "salida_esperada":"El animal kawai se acercó con una mirada de kawai. Manchas de kawai cubrían el suelo"
        },
        {
            "lista":["POPO", "SANGRE", "MUERTE", "MALDITO"],
            "texto":"El animal MaLdItO se acercó con una mirada de MuERtE. Manchas de SanGrE cubrían el suelo",
            "palabra":"kawai",
            "salida_esperada":"El animal kawai se acercó con una mirada de kawai. Manchas de kawai cubrían el suelo"
        },
        {
            "lista":["popo", "sangre", "muerte", "maldito"],
            "texto":"EL ANIMAL MALDITO SE ACERCÓ CON UNA MIRADA DE MUERTE. MANCHAS DE SANGRE CUBRÍAN EL SUELO",
            "palabra":"kawai",
            "salida_esperada":"El animal kawai se acercó con una mirada de kawai. Manchas de kawai cubrían el suelo"
        }]

        for tc in testCases:
            self.assertEqual(censura(tc["lista"],tc["texto"],tc["palabra"]),tc["salida_esperada"])

if __name__ == '__main__':
    unittest.main()
    
