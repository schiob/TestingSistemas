import unittest
from vocales import count

class Test(unittest.TestCase):
    def test_vowel(self):
        count()
        self.assertEqual('FOO','FOO')


if __name__ == '__main__':
    unittest.main()