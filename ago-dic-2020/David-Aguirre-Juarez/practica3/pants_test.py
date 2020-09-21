import unittest
import pants

class PantsTest(unittest.TestCase):
	def test_get_sorted_pants(self):
		tests = [
			{
				"inlist": [
					{ "ptype": "Nike", "price": 5.0 },
					{ "ptype": "Nike", "price": 6.0 },
					{ "ptype": "Nike", "price": 2.0 }
				],
				"outlist": [
					{ "ptype": "Nike", "price": 6.0 },
					{ "ptype": "Nike", "price": 5.0 },
					{ "ptype": "Nike", "price": 2.0 }
				]
			},
			{
				"inlist": [
					{ "ptype": "Nike", "price": 5.0 },
					{ "ptype": "Arris", "price": 8.0 },
					{ "ptype": "Nike", "price": 10.0 }
				],
				"outlist": [
					{ "ptype": "Nike", "price": 10.0 },
					{ "ptype": "Nike", "price": 5.0 },
					{ "ptype": "Arris", "price": 8.0 }
				]
			},
			{
				"inlist": [
					{ "ptype": "Nike", "price": 5.0 },
					{ "ptype": "Arris", "price": 8.0 },
					{ "ptype": "Coleman", "price": 30.0 }
				],
				"outlist": [
					{ "ptype": "Nike", "price": 5.0 },
					{ "ptype": "Coleman", "price": 30.0 },
					{ "ptype": "Arris", "price": 8.0 }
				]
			}
		]

		for t in tests:
			self.assertEqual(pants.sortPants(t["inlist"]), t["outlist"])

	def test_get_candidates(self):
		tests = [
			{
				"inlist": [
					{ "ptype": "Nike", "price": 6.0 },
					{ "ptype": "Nike", "price": 5.0 },
					{ "ptype": "Nike", "price": 2.0 }
				],
				"outlist": [
					{ "ptype": "Nike", "price": 6.0 },
					{ "ptype": "Nike", "price": 5.0 },
				]
			},
			{
				"inlist": [
					{ "ptype": "Nike", "price": 10.0 },
					{ "ptype": "Nike", "price": 5.0 },
					{ "ptype": "Arris", "price": 8.0 }
				],
				"outlist": [
					{ "ptype": "Nike", "price": 10.0 }
				]
			},
			{
				"inlist": [
					{ "ptype": "Nike", "price": 5.0 },
					{ "ptype": "Coleman", "price": 30.0 },
					{ "ptype": "Arris", "price": 8.0 }
				],
				"outlist": []
			},
			{
				"inlist": [
					{ "ptype": "Nike", "price": 10.0 },
					{ "ptype": "Nike", "price": 9.0 },
					{ "ptype": "Nike", "price": 8.0 },
					{ "ptype": "Nike", "price": 7.0 },
					{ "ptype": "Nike", "price": 6.0 },
					{ "ptype": "Nike", "price": 5.0 },
					{ "ptype": "Nike", "price": 4.0 },
					{ "ptype": "Coleman", "price": 30.0 },
					{ "ptype": "Arris", "price": 8.0 }
				],
				"outlist": [
					{ "ptype": "Nike", "price": 10.0 },
					{ "ptype": "Nike", "price": 9.0 },
					{ "ptype": "Nike", "price": 8.0 },
					{ "ptype": "Nike", "price": 7.0 },
					{ "ptype": "Nike", "price": 6.0 }
				]
			}
		]

		for t in tests:
			self.assertEqual(pants.getCandidates(t["inlist"]), t["outlist"])

	def test_get_money(self):
		tests = [
			{
				"candidates": [
					{ "ptype": "Nike", "price": 6.0 },
					{ "ptype": "Nike", "price": 5.0 },
				],
				"count": 2,
				"money": 11.0
			},
			{
				"candidates": [
					{ "ptype": "Nike", "price": 10.0 }
				],
				"count": 5,
				"money": 0.0
			},
			{
				"candidates": [],
				"count": 3,
				"money": 0.0
			},
			{
				"candidates": [
					{ "ptype": "Nike", "price": 10.0 },
					{ "ptype": "Nike", "price": 9.0 },
					{ "ptype": "Nike", "price": 8.0 },
					{ "ptype": "Nike", "price": 7.0 },
					{ "ptype": "Nike", "price": 6.0 }
				],
				"count": 3,
				"money": 27.0
			}
		]

		for t in tests:
			self.assertEqual(pants.tryToSell(t["count"], t["candidates"]), t["money"])

if __name__ == "__main__":
	unittest.main()