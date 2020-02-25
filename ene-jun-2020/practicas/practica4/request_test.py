import unittest
from request import getAnime, BiblioAnime, Anime

class BiblioMock(BiblioAnime):
    def setAnime(self, title):
        self.anime = Anime(title, 123, "temp")

    def Search(self, id):
        return self.anime

class TestRequest(unittest.TestCase):
    def test_anime(self):
        tests = (
            {'input': "1", 'expect_out': "Cowboy Bebop", 'mock_json': {"title": "Cowboy Bebop"}},
            {'input': "40852", 'expect_out': "Dr. Stone: Stone Wars", 'mock_json': {"title": "Dr. Stone: Stone Wars"}}
        )

        for tc in tests:
            biblio_mock = BiblioMock()
            biblio_mock.setAnime(tc['expect_out'])

            actual = getAnime(tc['input'], biblio_mock)
            self.assertEqual(tc['expect_out'], actual)

if __name__ == "__main__":
    unittest.main()