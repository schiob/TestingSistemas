import unittest
from h12to24 import hora12to24
class TestHora(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []

    def tearDown(self):
        self.assertEqual([], self.verificationErrors)

    def test_conv_hora(self):
        tc=[
        {
            "Entrada":"02:23p.m.",
            "Salida":"14:23hrs"
        },
        {
            "Entrada":"11:42p.m.",
            "Salida":"23:43hrs"
        },
        {
            "Entrada":"11:42a.m.",
            "Salida":"11:42hrs"
        },
        {
            "Entrada":"12:00p.m.",
            "Salida":"12:00hrs"
        },
        {
            "Entrada":"12:00a.m.",
            "Salida":"00:00hrs"
        },
        {
            "Entrada":"01:05a.m.",
            "Salida":"01:05hrs"
        },
        {
            "Entrada":"11:59p.m.",
            "Salida":"23:59hrs"
        }
        ]

        for test in tc:
            Hora = hora12to24(test["Entrada"])
            try: self.assertEqual(Hora,test["Salida"])
            except AssertionError: self.verificationErrors.append(f"Error Entrada:{test['Entrada']}, Salida Esperada:{test['Salida']}, Real: {Hora}")
if __name__ == "__main__":
    unittest.main()