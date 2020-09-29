import unittest
from unittest.mock import patch, MagicMock
import domain_average as da

class FileReaderMock:
	def __init__(self, read_value, display_error):
		self.read_value = read_value
		self.display_error = display_error

	def close(self):
		pass

	def read(self):
		if self.display_error:
			raise OSError()

		return self.read_value

class AverageTest(unittest.TestCase):
	def __init__(self, *args, **kwargs):
		super(AverageTest, self).__init__(*args, **kwargs)

		self.correct_file_output = f"usuario,correo,puntos\nTom,tomas@hotmail.com,85\nJuan,juan@hotmail.com,75\nMaria,maria84@gmail.com,90\nPaco,paquito123@outlook.com,74\nAna,anaa22@gmail.com,88\nMarcos,marcosss@hotmail.com,92"
		self.correct_convert_output = [
			{ "usuario": "Tom", "correo": "tomas@hotmail.com", "puntos": "85" },
			{ "usuario": "Juan", "correo": "juan@hotmail.com", "puntos": "75" },
			{ "usuario": "Maria", "correo": "maria84@gmail.com", "puntos": "90" },
			{ "usuario": "Paco", "correo": "paquito123@outlook.com", "puntos": "74" },
			{ "usuario": "Ana", "correo": "anaa22@gmail.com", "puntos": "88" },
			{ "usuario": "Marcos", "correo": "marcosss@hotmail.com", "puntos": "92" }
		]
		self.correct_parse_output = [
			{ "usuario": "Tom", "correo": "tomas@hotmail.com", "puntos": 85.0 },
			{ "usuario": "Juan", "correo": "juan@hotmail.com", "puntos": 75.0 },
			{ "usuario": "Maria", "correo": "maria84@gmail.com", "puntos": 90.0 },
			{ "usuario": "Paco", "correo": "paquito123@outlook.com", "puntos": 74.0 },
			{ "usuario": "Ana", "correo": "anaa22@gmail.com", "puntos": 88.0 },
			{ "usuario": "Marcos", "correo": "marcosss@hotmail.com", "puntos": 92.0 }
		]
		self.correct_average_output = [
			{ "domain": "hotmail.com", "average": 84.0 },
			{ "domain": "gmail.com", "average": 89.0 },
			{ "domain": "outlook.com", "average": 74.0 }
		]

	def test_read_file(self):
		tests = [
			{
				"in": "",
				"out": ""
			},
			{
				"in": "users",
				"out": ""
			},
			{
				"in": "../users.csv",
				"out": ""
			},
			{
				"in": "users.csv",
				"out": self.correct_file_output
			},
			{
				"in": "UseRs.csv",
				"out": self.correct_file_output
			},
			{
				"in": "../practica4/users.csv",
				"out": self.correct_file_output
			}
		]

		for t in tests:
			self.assertEqual(da.get_content_file(t["in"]), t["out"])

	@patch("builtins.open")
	def test_read_file_mocks(self, reader_mock):
		tests = [
			{
				"in": "",
				"out": "",
				"throw_error": True
			},
			{
				"in": "users",
				"out": "",
				"throw_error": True
			},
			{
				"in": "../users.csv",
				"out": "",
				"throw_error": True
			},
			{
				"in": "users.csv",
				"out": self.correct_file_output
			},
			{
				"in": "UseRs.csv",
				"out": self.correct_file_output
			},
			{
				"in": "../practica4/users.csv",
				"out": self.correct_file_output
			}
		]

		for t in tests:
			reader_mock.return_value = FileReaderMock(t["out"], t.get("throw_error", False))
			real_output = da.get_content_file(t["in"])

			reader_mock.assert_called_with(t["in"])
			self.assertEqual(real_output, t["out"])

	def test_convert_content(self):
		tests = [
			{
				"in": "",
				"out": []
			},
			{
				"in": "perro,gato",
				"out": []
			},
			{
				"in": "usuario,correo\nusuario1",
				"out": [],
			},
			{
				"in": "usuario ,correo   ,puntos\n david,  david@ gmail.com , 2",
				"out": [
					{ "usuario": "david", "correo": "david@ gmail.com", "puntos": "2" }
				],
			},
			{
				"in": "perro ,gato\n david, alfedro",
				"out": [
					{ "perro": "david", "gato": "alfedro" }
				],
			},
			{
				"in": self.correct_file_output,
				"out": self.correct_convert_output,
			}
		]

		for t in tests:
			self.assertEqual(da.convert_content(t["in"]), t["out"])

	def test_parse_converted_content(self):
		tests = [
			{
				"in": [],
				"out": []
			},
			{
				"in": [
					{ "perro": "holas" }
				],
				"out": [],
			},
			{
				"in": [
					{ "usuario": "Ana", "correo": "anaa22@gmail.com", "puntos": 88.0 },
					{ "usuario": "Marcos", "correo": "marcossshotmail.com", "puntos": 92.0 }
				],
				"out": []
			},
			{
				"in": self.correct_convert_output,
				"out": self.correct_parse_output,
			}
		]

		for t in tests:
			self.assertEqual(da.parse_converted_content(t["in"]), t["out"])

	def test_get_average(self):
		tests = [
			{
				"in": [
					{ "usuario": "Paco", "correo": "paquito123@outlook.com", "puntos": 74.0 }
				],
				"out": [
					{ "domain": "outlook.com", "average": 74.0 }
				]
			},
			{
				"in": [],
				"out": []
			},
			{
				"in": self.correct_parse_output,
				"out": self.correct_average_output,
			}
		]

		for t in tests:
			self.assertEqual(da.get_average(t["in"]), t["out"])

if __name__ == "__main__":
	unittest.main()