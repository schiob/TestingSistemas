import unittest
from request import getPokimon, Pokedex, PoketMonsta # Importamos el metodo getPokimon(Regresa el nombre del pokemon), Clase Pokedex que es la interface con el metodo Search, La clase PoketMonsta que tiene los atributos del pokemon

class PokedexMock(Pokedex): # La clase Mock implementa la clase abstracta Pokedex
    def setPokemon(self, nombre):
        self.pokemon = PoketMonsta(nombre, "grass", 49)

    def Search(self, id):
        return self.pokemon

class TestRequest(unittest.TestCase):
    def test_poke(self):
        poke_test = (
            {'input': "1", 'expect_out': "Bulbasaur", 'mock_json': {"name": "Bulbasaur"}},
            {'input': "2", 'expect_out': "Ivysaur", 'mock_json': {"name": "Ivysaur"}},
            {'input': "3", 'expect_out': "Venasaur", 'mock_json': {"name": "Venasaur"}}
            
        )

        for tc in poke_test:
            poke_mock = PokedexMock()
            poke_mock.setPokemon(tc['expect_out'])

            actual = getPokimon(tc['input'], poke_mock)
            self.assertEqual(tc['expect_out'], actual)
           

if __name__ == "__main__":
    unittest.main()