from datetime import datetime, date, time
import unittest
import Parcial1

def cambiarhora(horaActual):
    horario = "%H:%Mhrs"
    nuevoHorario = "%I:%M%p"
    hora=horaActual
    nuevaHora=datetime.strptime(hora,horario)
    #cambiohora=datetime.strptime(hora,nuevoHorario)
    strhora=datetime.strftime(nuevahora,horario)
    return strhora

class TestCambioHora(unittest.TestCase):
    def test1(self):
        horaActual="14:23hrs"
        self.assertEqual(Parcial1.cambiarhora(horaActual),"2:23p.m.")

    def test2(self):
        horaActual="23:43hrs"
        self.assertEqual(Parcial1.cambiarhora(horaActual),"11:43p.m.")

    def test3(self):
        horaActual="11:42hrs"
        self.assertEqual(Parcial1.cambiarhora(horaActual),"11:42a.m.")

    def test4(self):
        horaActual="00:00hrs"
        self.assertEqual(Parcial1.cambiarhora(horaActual),"12:00a.m.")

    def test5(self):
        horaActual="12:00hrs"
        self.assertEqual(Parcial1.cambiarhora(horaActual),"12:00p.m.")

    def test6(self):
        horaActual="01:05hrs"
        self.assertEqual(Parcial1.cambiarhora(horaActual),"01:05a.m.")

    def test7(self):
        horaActual="23:59hrs"
        self.assertEqual(Parcial1.cambiarhora(horaActual),"11:59p.m.")

if __name__ == "__main__":
    unittest.main()
