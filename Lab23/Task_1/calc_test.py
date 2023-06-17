import unittest
import calc

class CalcTest(unittest.TestCase):
	def test_add(self):
		self.assertEqual(calc.add(6,2),8)

	def test_sub(self):
		self.assertEqual(calc.sub(13,7),6)

	def test_mul(self):
		self.assertEqual(calc.mul(7,8),56)
		
	def test_div(self):
		self.assertEqual(calc.div(6,2),3)