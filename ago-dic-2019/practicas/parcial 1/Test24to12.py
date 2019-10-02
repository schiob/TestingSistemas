import unittest
module = __import__('24to12')
#from 24to12 import transform

class Test24to12(unittest.TestCase):
    cases = [
        ("14:23hrs", "02:23p.m."),
        ("23:43hrs", "11:43p.m."),
        ("11:42hrs", "11:42a.m."),
        ("00:00hrs", "12:00a.m."),
        ("12:00hrs", "12:00p.m."),
        ("01:05hrs", "01:05a.m."),
        ("23:59hrs", "11:59p.m."),
    ]

    def test_transform(self):
        for pairs in self.cases:
            with self.subTest(pairs=pairs):
                self.assertEqual(module.transform(pairs[0]), pairs[1])

if __name__ == '__main__':
    unittest.main()
