import unittest
from doceTo24 import doce_to24


class Test(unittest.TestCase):
    def test(self):
        cp = [
                {'input': '02:23 PM', 'expected': '14:23 HRS'},
                {'input': '11:42 PM', 'expected': '23:42 HRS'},
                {'input': '11:42 AM', 'expected': '11:42 HRS'},
                {'input': '12:00 PM', 'expected': '12:00 HRS'},
                {'input': '12:00 AM', 'expected': '00:00 HRS'},
                {'input': '01:05 AM', 'expected': '01:05 HRS'},
                {'input': '11:59 PM', 'expected': '23:59 HRS'}
        ]
        for horas in cp:
            self.assertEqual(doce_to24(horas['input']), horas['expected'])


if __name__ == '__main__':
    unittest.main()
