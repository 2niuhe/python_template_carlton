import unittest
from multiply.add_three import add_by_three



class TestMultiplyByThree(unittest.TestCase):

	def test_multiply_by_three(self):
		self.assertEqual(add_by_three(3), 6)



unittest.main()
