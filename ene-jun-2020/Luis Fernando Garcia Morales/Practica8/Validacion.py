from censura import censura
import unittest
def validate(lista,text,palabra,limite):
    nuevoTexto = censura(lista,text,palabra)
    if len(nuevoTexto)-len(text) <= limite:
        return True
    else:
        return False

class TestValidate(unittest.TestCase):
    def testValidacion (self):
        testcases = [{
            "lista":["popo", "sangre", "muerte", "maldito"],
            "texto":"El animal maldito se acercó con una mirada de muerte. Manchas de sangre cubrían el suelo",
            "palabra":"kawai",
            "limite": 5,
            "salida_esperada": True
        },
        {
            "lista":["popo", "sangre", "muerte", "maldito"],
            "texto":"El animal maldito se acercó con una mirada de muerte. Manchas de sangre cubrían el suelo",
            "palabra":"kawaiiiiii",
            "limite": 5,
            "salida_esperada": False
        },
        {
            "lista":["popo", "sangre", "muerte", "maldito"],
            "texto":"El animal maldito se acercó con una mirada de muerte. Manchas de sangre cubrían el suelo",
            "palabra":"fine_fine_fine_veri_veri_veriguuuuuuuuu",
            "limite": 115,
            "salida_esperada": True
        },
        {
            "lista":["popo", "sangre", "muerte", "maldito"],
            "texto":"La popo es saludable",
            "palabra":"popis",
            "limite": 1,
            "salida_esperada": True
        },
        {
            "lista":["popo", "sangre", "muerte", "maldito"],
            "texto":"La popo es saludable",
            "palabra":"popis",
            "limite": 0,
            "salida_esperada": False
        },
        {
            "lista":["popo", "sangre", "muerte", "maldito"],
            "texto":"Una aventura es mas divertida si huele a popo",
            "palabra":"peligro",
            "limite": 3,
            "salida_esperada": True
        }]

        for tc in testcases:
            self.assertEqual(validate(tc["lista"],tc["texto"],tc["palabra"],tc["limite"]),tc["salida_esperada"])

if __name__ == '__main__':
    unittest.main()