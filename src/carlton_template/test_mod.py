from .mod import add_three
import unittest


class TestAddThree(unittest.TestCase):
    def test_add_three(self):
        self.assertEqual(add_three(3), 6)
