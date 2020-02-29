import unittest
from pokemon import getPokemon, Natpokedex, pokemon

class pokedexMock(Natpokedex):
    def setPokemon(self,name):
        self.pokemon = pokemon(name)
    def Search(self, num):
        return self.pokemon

class TestPokemon(unittest.TestCase):
    def test_pokedex(self):
        tests= (
            {'input': "1", 'expect_out': "bulbasaur", 'mock_json': {"name": "bulbasaur"}},
            {'input': "2" ,'expect_out': "ivysaur", 'mock_json': {"name": "ivysaur"}}
            )
        for tc in tests:
            pokedex_Mock = pokedexMock()
            pokedex_Mock.setPokemon(tc['expect_out'])

            actual = getPokemon(tc['input'],pokedex_Mock)
            self.assertEqual(tc['expect_out'],actual)

if __name__ == "__main__":
    unittest.main()