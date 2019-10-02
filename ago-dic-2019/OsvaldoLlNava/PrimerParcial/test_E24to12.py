import unittest
import E24to12

class test(unittest.TestCase):
    #entrada=['14:23hrs', '23:43hrs', '11:42hrs','00:00hrs','12:00','01:05hrs','23:59hrs']
    #salida = ['02:23p.m.', '11:43p.m.','11:42a.m.', '12:00a.m.', '12:00p.m.','01:05a.m.', '11:59p.m.']
    
    def test_uno(self):
        self.assertEqual(E24to12.Conversor('14:23hrs'),'02:23p.m.')
    
    def test_dos(self):
        self.assertEqual(E24to12.Conversor('23:43hrs'),'11:43p.m.')

    def test_tres(self):
        self.assertEqual(E24to12.Conversor('11:42hrs'),'11:42a.m.')

    def test_cuatro(self):
        self.assertEqual(E24to12.Conversor('00:00hrs'),'12:00a.m.')

    def test_cinco(self):
        self.assertEqual(E24to12.Conversor('12:00hrs'),'12:00p.m.')

    def test_seis(self):
        self.assertEqual(E24to12.Conversor('01:05hrs'),'01:05a.m.')

    def test_siete(self):
        self.assertEqual(E24to12.Conversor('23:59hrs'),'11:59p.m.')     


if __name__ == '__main__':
    unittest.main()