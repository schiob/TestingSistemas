import unittest
from unittest.mock import patch, MagicMock
from primer_parcial import triangle_from_file as triangle

class FileReaderMock:
	def __init__(self, read_value, error = False):
		self.read_value = read_value
		self.display_error = error

	def close(self):
		pass

	def read(self):
		if self.display_error:
			raise OSError()

		return self.read_value


class TriangleTest(unittest.TestCase):
	@patch("builtins.open")
	def __do_tests(self, tests, reader_mock):
		for t in tests:
			reader_mock.return_value = FileReaderMock(
				t.get("file_content", ""),
				t.get("file_error", False)
			)

			out = triangle(t["path"])

			reader_mock.assert_called_with(t["path"])
			self.assertEqual(out, t["out"])


	def test_no_triangulo(self):
		self.__do_tests([
			{
				"path": "notri1.txt",
				"file_content": "0 0 0",
				"out": "No triangulo"
			},
			{
				"path": "notri2.txt",
				"file_content": "0 5 7",
				"out": "No triangulo"
			},
			{
				"path": "notri3.txt",
				"file_content": "1 2 3",
				"out": "No triangulo"
			},
			{
				"path": "notri",
				"file_error": True,
				"out": "No triangulo"
			},
			{
				"path": "notri.txt",
				"file_content": "2 1",
				"out": "No triangulo"
			}
		])

	def test_equilatero(self):
		self.__do_tests([
			{
				"path": "equi1.txt",
				"file_content": "3 3 3",
				"out": "Equilatero"
			},
			{
				"path": "equi2.txt",
				"file_content": "5 5 5",
				"out": "Equilatero"
			}
		])

	def test_isoceles(self):
		self.__do_tests([
			{
				"path": "iso1.txt",
				"file_content": "10 7 7",
				"out": "Isoceles"
			},
			{
				"path": "iso2.txt",
				"file_content": "4 5 4",
				"out": "Isoceles"
			}
		])

	def test_escaleno(self):
		self.__do_tests([
			{
				"path": "esca1.txt",
				"file_content": "8 6 5",
				"out": "Escaleno"
			}
		])

if __name__ == "__main__":
	unittest.main()