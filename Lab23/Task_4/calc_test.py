import unittest
import calc

class CalcTest(unittest.TestCase):
	"""Тест для калькулятора"""

	@classmethod
	def setUpClass(cls):
		print("setUpClass")
		print("==========")

	@classmethod
	def tearDownClass(cls):
		print("==========")
		print("tearDownClass")

	def setUp(self):
		print("Set up for ["+self.shortDescription()+"]")

	def tearDown(self):
		print("Tear down for ["+self.shortDescription()+"]")
		print("")

	def test_add(self):
		"""Тест для операции сложения"""
		print("id: "+self.id())
		self.assertEqual(calc.add(6,2),8)

	def test_sub(self):
		"""Тест для операции вычитания"""
		print("id: "+self.id())
		self.assertEqual(calc.sub(8,6),2)

	def test_mul(self):
		"""Тест для операции умножения"""
		print("id: "+self.id())
		self.assertEqual(calc.mul(7,5),35)
		
	def test_div(self):
		"""Тест для операции деления"""
		print("id: "+self.id())
		self.assertEqual(calc.div(16,4),4)

class CalcExTests(unittest.TestCase):
	"""Расиширение теста для калькулятора"""

	def test_pow(self):
		"""Тест для операции возведения в степень"""
		print("id: "+self.id())
		self.assertEqual(calc.pow(4,2),16)

	def test_sqrt(self):
		"""Тест для операции выведения из корня"""
		print("id: "+self.id())
		self.assertEqual(calc.sqrt(4),2)

if __name__=='__main__':
	unittest.main()
