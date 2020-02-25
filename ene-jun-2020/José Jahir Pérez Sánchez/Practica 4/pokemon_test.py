import unittest
from unittest.mock import patch,MagicMock
from pokemon import pokedex

class TestPokemon(unittest.TestCase):
    @patch('requests.get')
    def test_pokemon(self,get_mock):
        test = [
            {   "input": "1",
                "expect_out": "bulbasaur",
                "mock_json": {"name": "bulbasaur"}

             },
              {   "input": "151",
                "expect_out": "mew",
                "mock_json": {"name": "mew"}

             },          
        ]
        for tc in test:
            def json():
                return tc["mock_json"]
            m = MagicMock()
            m.json = json
            get_mock.return_value = m
            actual = pokedex(tc['input'])
            self.assertEqual(tc['expect_out'],actual)

if __name__ == "__main__":
    unittest.main()