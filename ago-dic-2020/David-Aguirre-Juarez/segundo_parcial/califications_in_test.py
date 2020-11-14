import califications as ca
import califications_test as cat
import os
import unittest

# == INTEGRATION TESTS ==

class CalifInTest(unittest.TestCase):
	def __make_files(self):
		for f in cat.CTests.file_tests:
			if isinstance(f.get("raisemock"), FileNotFoundError):
				continue

			file = open(f["in"], "w")
			file.write(f["outmock"])
			file.close()

	def __remove_files(self):
		for f in cat.CTests.file_tests:
			if os.path.exists(f["in"]):
				os.remove(f["in"])

	def test_read_file(self):
		self.__make_files()
		
		for t in cat.CTests.file_tests:
			out = ca.get_content(t["in"])
			self.assertEqual(out, t.get("out", []))

		self.__remove_files()

	def test_average(self):
		self.__make_files()
		
		for t in cat.CTests.average_tests:
			self.assertEqual(ca.read_and_get_average(t["fpath"]), t.get("out", ""))

		self.__remove_files()


if __name__ == "__main__":
	unittest.main()