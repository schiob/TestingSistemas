import unittest
import califications as ca
from unittest.mock import patch, MagicMock

class CTests:
	file_tests = [
		{
			"in": "perro.txt",
			"outmock": "alumno mate 2.15\nalumno esp 2.00\ndavid esp 6.002",
			"out": [
				{
					"name": "alumno",
					"assign": "mate",
					"calif": 2.15
				},
				{
					"name": "alumno",
					"assign": "esp",
					"calif": 2.0
				},
				{
					"name": "david",
					"assign": "esp",
					"calif": 6.0
				}
			]
		},
		{
			"in": "no_exist.txt",
			"raisemock": FileNotFoundError(),
			"out": []
		},
		{
			"in": "err_format.txt",
			"outmock": "oh no! format error",
			"out": []
		},
		{
			"in": "err_format_2.txt",
			"outmock": "materia 5",
			"out": []
		}
	]

	average_tests = [
		{
			"fpath": file_tests[0]["in"],
			"in": file_tests[0]["out"],
			"out": "alumno 2.08\ndavid 6.00"
		},
		{
			"fpath": file_tests[1]["in"],
			"in": file_tests[1]["out"],
			"out": ""
		},
		{
			"fpath": file_tests[2]["in"],
			"in": file_tests[2]["out"],
			"out": ""
		},
		{
			"fpath": file_tests[3]["in"],
			"in": file_tests[3]["out"],
			"out": ""
		}
	]

class CalifTest(unittest.TestCase):
	@patch("builtins.open")
	def test_read_file(self, reader_mock):
		def raise_err(raises):
			raise raises

		for t in CTests.file_tests:
			reader_mock.return_value = MagicMock()
			reader_mock.return_value.read = lambda: t.get("outmock", "") if not t.get("raisemock", False) else raise_err(t.get("raisemock", Exception()))
			reader_mock.return_value.close = lambda: None

			out = ca.get_content(t["in"])

			reader_mock.assert_called_with(t["in"])
			self.assertEqual(out, t.get("out", []))

	def test_average(self):
		for t in CTests.average_tests:
			self.assertEqual(ca.get_average(t["in"]), t.get("out", ""))

if __name__ == "__main__":
	unittest.main()