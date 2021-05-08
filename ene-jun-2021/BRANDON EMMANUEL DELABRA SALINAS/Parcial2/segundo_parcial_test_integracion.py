from unittest import TestCase
import segundo_parcial

class segundo_parcial_integracion(TestCase):
    def testUno(self):
        esperado="texto leido"
        real=segundo_parcial.checkArchivoExiste("testintegracion.txt")

        assert esperado==real

    def testDos(self):
        esperado="{ \"INPUT\": \"convertir este texto\" , \"OUTPUT\": \"CONVERTIR ESTE TEXTO\"}"
        real=segundo_parcial.convertirAMayusculas("convertir este texto")

        assert esperado==real

    def testDos(self):
        esperado="{ \"INPUT\": \"texto leido\" , \"OUTPUT\": \"TEXTO LEIDO\"}"
        real=segundo_parcial.funcionFinal("testintegracion.txt")

        assert esperado==real