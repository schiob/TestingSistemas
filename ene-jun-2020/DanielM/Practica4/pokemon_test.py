import unittest
from pokemon import get_pokemon, Pokemon, Pokedex


class BibliotMock(Pokedex):
    def set_pokemon(self, name):
        self.pokemon = Pokemon(name)

    def search(self, id):
        return self.pokemon


class TestRequest(unittest.TestCase):
    def test_pok(self):
        tests = (
            {'input': "144", 'expect_out': "articuno", 'mock_json': {'name': "articuno"}},
            {'input': "150", 'expect_out': "mewtwo", 'mock_json': {"name": "mewtwo"}},
            {'input': "151", 'expect_out': "mew", 'mock_json': {'name': "mew"}}
        )

        for tc in tests:
            biblio_mock = BibliotMock()
            biblio_mock.set_pokemon(tc['expect_out'])

            actual = get_pokemon(tc['input'], biblio_mock)
            self.assertEqual(tc['expect_out'], actual)


if __name__ == "__main__":
    unittest.main()
