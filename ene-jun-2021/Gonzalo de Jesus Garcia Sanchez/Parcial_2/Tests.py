import unittest
import Parcial_2
from unittest.mock import patch

class testFunctions(unittest.TestCase):
    # @patch('requests.post')
    # def test_palabras_arriba(self, mock_post):
    #     test_cases = [("hola", 200, "HOLA"),
    #                   ("adios", 200, "ADIOS"),
    #                   ("error", 404, "error"),
    #                   ("espero sacar cien", 200, "ESPERO SACAR CIEN")
    #                   ]
    #
    #     for entrada, code, esperado in test_cases:
    #         mock_post.return_value.text = entrada
    #         salida_real = segundop.palabras_arriba(entrada)
    #         self.assertEqual(salida_real, esperado)

    # def test_regretContent(self):
    #     test_cases = [("prueba_sp.txt", "Soy un archivo que tiene info"),
    #                   ("prueba_spp.txt", """El archivito no estaba pero mientras ve este bonito perrito:
    #                ▄              ▄
    #               ▌▒█           ▄▀▒▌
    #               ▌▒▒█        ▄▀▒▒▒▐
    #              ▐▄▀▒▒▀▀▀▀▄▄▄▀▒▒▒▒▒▐
    #            ▄▄▀▒░▒▒▒▒▒▒▒▒▒█▒▒▄█▒▐
    #          ▄▀▒▒▒░░░▒▒▒░░░▒▒▒▀██▀▒▌
    #         ▐▒▒▒▄▄▒▒▒▒░░░▒▒▒▒▒▒▒▀▄▒▒▌
    #         ▌░░▌█▀▒▒▒▒▒▄▀█▄▒▒▒▒▒▒▒█▒▐
    #        ▐░░░▒▒▒▒▒▒▒▒▌██▀▒▒░░░▒▒▒▀▄▌
    #        ▌░▒▄██▄▒▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒▌
    #       ▌▒▀▐▄█▄█▌▄░▀▒▒░░░░░░░░░░▒▒▒▐
    #       ▐▒▒▐▀▐▀▒░▄▄▒▄▒▒▒▒▒▒░▒░▒░▒▒▒▒▌
    #       ▐▒▒▒▀▀▄▄▒▒▒▄▒▒▒▒▒▒▒▒░▒░▒░▒▒▐
    #        ▌▒▒▒▒▒▒▀▀▀▒▒▒▒▒▒░▒░▒░▒░▒▒▒▌
    #        ▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▒▄▒▒▐
    #         ▀▄▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▄▒▒▒▒▌
    #           ▀▄▒▒▒▒▒▒▒▒▒▒▄▄▄▀▒▒▒▒▄▀
    #             ▀▄▄▄▄▄▄▀▀▀▒▒▒▒▒▄▄▀
    #                ▒▒▒▒▒▒▒▒▒▒▀▀""")]
    #
    #     for entrada, esperado in test_cases:
    #         actual = segundop.regretContent(entrada)
    #         self.assertEqual(esperado, actual)


    def test_regretContentUP(self):
        test_cases = [("prueba_sp.txt", "SOY UN ARCHIVO QUE TIENE INFO"),
                      ("prueba_spp.txt", """EL ARCHIVITO NO ESTABA PERO MIENTRAS VE ESTE BONITO PERRITO:
                   ▄              ▄
                  ▌▒█           ▄▀▒▌
                  ▌▒▒█        ▄▀▒▒▒▐
                 ▐▄▀▒▒▀▀▀▀▄▄▄▀▒▒▒▒▒▐
               ▄▄▀▒░▒▒▒▒▒▒▒▒▒█▒▒▄█▒▐
             ▄▀▒▒▒░░░▒▒▒░░░▒▒▒▀██▀▒▌
            ▐▒▒▒▄▄▒▒▒▒░░░▒▒▒▒▒▒▒▀▄▒▒▌
            ▌░░▌█▀▒▒▒▒▒▄▀█▄▒▒▒▒▒▒▒█▒▐
           ▐░░░▒▒▒▒▒▒▒▒▌██▀▒▒░░░▒▒▒▀▄▌
           ▌░▒▄██▄▒▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒▌
          ▌▒▀▐▄█▄█▌▄░▀▒▒░░░░░░░░░░▒▒▒▐
          ▐▒▒▐▀▐▀▒░▄▄▒▄▒▒▒▒▒▒░▒░▒░▒▒▒▒▌
          ▐▒▒▒▀▀▄▄▒▒▒▄▒▒▒▒▒▒▒▒░▒░▒░▒▒▐
           ▌▒▒▒▒▒▒▀▀▀▒▒▒▒▒▒░▒░▒░▒░▒▒▒▌
           ▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▒▄▒▒▐
            ▀▄▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▄▒▒▒▒▌
              ▀▄▒▒▒▒▒▒▒▒▒▒▄▄▄▀▒▒▒▒▄▀
                ▀▄▄▄▄▄▄▀▀▀▒▒▒▒▒▄▄▀
                   ▒▒▒▒▒▒▒▒▒▒▀▀""")]

        for entrada, esperado in test_cases:
            actual = segundop.regretContentUP(entrada)
            self.assertEqual(esperado, actual)


if __name__ == '__main__':
    unittest.main()
