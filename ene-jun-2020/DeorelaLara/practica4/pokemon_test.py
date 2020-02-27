import unittest
from pokemon import getPokemon, Pokedex, Pokemon

class BiblioMock(Pokedex):
    def setPokemon(self, name):
        self.pokemon = Pokemon(name)

    def Search(self, id):
        return self.pokemon

class TestRequest(unittest.TestCase):
    def test_pok(self):
        tests = (
            {'input': "12", 'expect_out': "butterfree", 'mock_json': {"name": "butterfree"}},
            {'input': "25", 'expect_out': "pikachu", 'mock_json': {'name': "pikachu"}}

        )

        for tc in tests:
            biblio_mock = BiblioMock()
            biblio_mock.setPokemon(tc['expect_out'])

            actual = getPokemon(tc['input'], biblio_mock)
            self.assertEqual(tc['expect_out'], actual)


if __name__ == "__main__":
    unittest.main()