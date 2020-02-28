import unittest
from pokemon import getPokymon, Bibliopokymon, Pokymon

class BiblioMock(Bibliopokymon):
    def setPokymon(self, name):
        self.Pokymon = Pokymon(name)
    def Search(self,id):
        return self.Pokymon

class TestPokimon(unittest.TestCase):
    def test_pokymon(self):
        test = (
            {'input':"1",'expect_out':"bulbasaur",'mock_json':{"name":"bulbasaur"}},
            {'input':"6",'expect_out':"charizard",'mock_json':{"name":"charizard"}}
        )

        for tc in test:
            Biblio_mock = BiblioMock()
            Biblio_mock.setPokymon(tc['expect_out'])
            actual = getPokymon(tc['input'],Biblio_mock)
            self.assertEqual(tc['expect_out'],actual)
            print(Biblio_mock)
if __name__ == '__main__':
    unittest.main()
    