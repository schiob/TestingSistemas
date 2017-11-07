import unittest
from bon_appetit import bonAppetit

class TestAppetit(unittest.TestCase):

    # Caso donde el Brayan le debe a la Anita.
    def testDeuda(self):
        self.assertEqual(bonAppetit(4,1,12,[3, 10, 2, 9]), 5)

    # Caso donde el Brayan y Anita son felices.
    def testBA(self):
        self.assertEqual(bonAppetit(4,1,7,[3, 10, 2, 9]), 'Bon Appetit')


if __name__ == '__main__':
    unittest.main()
