import datetime
import unittest
def convert_time(str24hrs):
    strtime = str24hrs
    strtime_ok = ''
    for i in strtime:
        if i != 'h' and i != 'r' and i !='s':
            strtime_ok += i
    format24hs  = "%H:%M"
    format12hs = "%I:%M%P"
    datetime_object24 = datetime.datetime.strptime(strtime_ok, format24hs)
    datetime_object12 = datetime.datetime.strftime(datetime_object24, format12hs)
    print(datetime_object12)
    return str(datetime_object12)

convert_time('12:23hrs')

class Test_Convert_time(unittest.TestCase):
    def test_uno(self):
        convertir = convert_time('14:23hrs')
        self.assertEqual(convertir, '02:23pm')
    def test_dos(self):
        convertir = convert_time('23:43hrs')
        self.assertEqual(convertir, '11:43pm')
    def test_tres(self):
        convertir = convert_time('11:42hrs')
        self.assertEqual(convertir, '11:42am')
    def test_cuatro(self):
        convertir = convert_time('00:00hrs')
        self.assertEqual(convertir, '12:00am')
    def test_cinco(self):
        convertir = convert_time('12:00hrs')
        self.assertEqual(convertir, '12:00pm')
    def test_seis(self):
        convertir = convert_time('01:05hrs')
        self.assertEqual(convertir, '01:05am')
    def test_siete(self):
        convertir = convert_time('23:59hrs')
        self.assertEqual(convertir, '11:59pm')
if __name__== '__main__':
    unittest.main()