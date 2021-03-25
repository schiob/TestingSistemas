import unittest
from Censura import censura, censuraValida
from unittest.mock import patch

class TestCasos(unittest.TestCase):
    def test_todospasan(self):
        PalabrasCensurables=(
            ["popo", "sangre", "muerte", "maldito"],
            ["animal", "mirada", "muerte", "cubrían"],
            ["Manchas", "acercó", "suelo", "maldito"]
        )

        texto = "El animal maldito se acercó con una mirada de muerte. Manchas de sangre cubrían el suelo"
        longtexto=len(texto)
        ltextvalido=longtexto + 10
        remplazo = "cristal"
        for tc in PalabrasCensurables:
            censurables=[tc[0],tc[1],tc[2],tc[3]]
            resultado = censuraValida(censurables,texto,remplazo,ltextvalido)
            self.assertEqual(resultado,"Es válido")

    def test_nadiepasan(self):
        PalabrasCensurables=(
            ["popo", "sangre", "muerte", "maldito"],
            ["animal", "mirada", "muerte", "cubrían"],
            ["Manchas", "acercó", "suelo", "maldito"]
        )

        texto = "El animal maldito se acercó con una mirada de muerte. Manchas de sangre cubrían el suelo"
        longtexto=len(texto)
        ltextvalido=longtexto + 10
        remplazo = "cristalososo"
        for tc in PalabrasCensurables:
            censurables=[tc[0],tc[1],tc[2],tc[3]]
            resultado = censuraValida(censurables,texto,remplazo,ltextvalido)
            self.assertEqual(resultado,"No es válida")

if __name__ == '__main__':
    unittest.main()