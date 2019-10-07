import unittest
from os
from masaCorporal import masaCORP
class test_MC(unittest.TestCase):
	def setUp(self):
		my_file=Path("imc.txt")
		if my_file.exists():
			return true 

	def mc_test(self):
		masaCORP(82.5 1.80)
		file = open("imd.txt","r")
		self.assertEqual(file,"25.46")

    def ceromc_test(self):
	    masaCORP(0 -11)
		file = open("imd.txt","r")
		self.assertEqual(file,"error")

def tearDown(self):
	self.widget.dispose()