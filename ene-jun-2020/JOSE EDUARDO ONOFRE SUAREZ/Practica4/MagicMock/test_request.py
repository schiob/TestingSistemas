import unittest
from request import pokedx
from unittest.mock import patch,MagicMock

class TestPokemon(unittest.TestCase):
    @patch('requests.get')
    def test_pokemon(self,get_mock): #Recibe como argumento get_mock que simula una funcion que retorna un valor del Json
        test = [

            {'input': "1", 'expect_out': "Bulbasaur", 'mock_json': {"name": "Bulbasaur"}},
            {'input': "2", 'expect_out': "Ivysaur", 'mock_json': {"name": "Ivysaur"}},
            {'input': "3", 'expect_out': "Venasaur", 'mock_json': {"name": "Venasaur"}}
            
        ]
    
        for tc in test:

            def json(): #Creamos una funcion Json que es la que retornara el valor de mock_json, es decir, el nombre del pokimon
                return tc['mock_json']
            m = MagicMock()
            m.json = json
            get_mock.return_value = m
            actual = pokedx(tc['input'])
            self.assertEqual(tc['expect_out'], actual)

if __name__ == "__main__":

    unittest.main()
    