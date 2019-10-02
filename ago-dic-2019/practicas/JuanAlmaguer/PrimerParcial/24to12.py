import unittest

def convert24to12(hora):
    horaint = int(hora)
    if horaint > 12:
        converthora = str(horaint - 12)
        converthora += 'pm'
        return converthora
        return
    else:
        return hora + "am"


class test_24to12(unittest.TestCase):

    def test_1423(self):
        prueba = convert24to12("14:23")
        self.assertEqual(prueba,'2:23pm')