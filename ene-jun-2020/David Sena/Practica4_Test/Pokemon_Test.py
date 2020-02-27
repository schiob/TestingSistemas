
import unittest
from Pokemon import getPoke, BiblioPoke, Pokemon

class BiblioMock(BiblioPoke):
    def setPoke(self, name):
        self.pokemon = Pokemon(name, 123)

    def Search(self, id):
        return self.pokemon

class TestRequest(unittest.TestCase):
    def test_pokemon(self):
        tests = (
            {'input': "25", 'expect_out': "pikachu", 'mock_json': {"name": "pikachu"}},
            {'input': "1", 'expect_out': "bulbasaur", 'mock_json': {"name": "bulbasaur"}}
        )

        for tc in tests:
            biblio_mock = BiblioMock()
            biblio_mock.setPoke(tc['expect_out'])

            actual = getPoke(tc['input'], biblio_mock)
            self.assertEqual(tc['expect_out'], actual)

if __name__ == "__main__":
    unittest.main()