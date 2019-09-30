import unittest
from chars import DeleteChar

class ReadFiles(unittest.TestCase):

    def test_EmptyFile(self):
        empty = DeleteChar(r'C:\Users\jdac_\Desktop\Empty.txt')
        self.assertEqual(empty, '')

    def test_ChangeFile(self):
        change = DeleteChar(r'C:\Users\jdac_\Desktop\Sicambio.txt')
        self.assertEqual(change,'ahuevoquetenemosqueescribirestojajajoque')

    def test_NoChanges(self):
        nochange = DeleteChar(r'C:\Users\jdac_\Desktop\NoCambio.txt')
        self.assertEqual(nochange, 'enestearchivonohayquecambiarnadajajja')


if __name__ == '__main__':
   unittest.main()
