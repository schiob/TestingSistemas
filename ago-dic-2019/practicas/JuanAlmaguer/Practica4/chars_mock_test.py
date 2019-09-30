import unittest
import chars
import mock
from mock import patch

class TestMock(unittest.TestCase):

    @patch('builtins.open')
    def test_empty(self,mock_open):
        mock_open.return_value.read = True
        chars.DeleteChar = mock.Mock(return_value="")
        repoio = chars.DeleteChar("vacio.txt")
        self.assertEqual(repoio, '')

    @patch('builtins.open')
    def test_changes(self,mock_open):
        mock_open.return_value.read = True
        chars.DeleteChar = mock.Mock(return_value="estetextonocambia")
        repoio = chars.DeleteChar("sicambio.txt")
        self.assertEqual(repoio, 'estetextonocambia')

    @patch('builtins.open')
    def test_nochanges(self, mock_open):
        mock_open.return_value.read = True
        chars.DeleteChar = mock.Mock(return_value="estetextosicambia")
        repoio = chars.DeleteChar("nocambio.txt")
        self.assertEqual(repoio, 'estetextosicambia')


if __name__ == "__main__":
    unittest.main()