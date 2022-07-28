from test_boolean_generation import *
import unittest

class TestSimplify(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(boolean_generation([''], ''), None)

    def test_empty_list(self):
        self.assertEqual(boolean_generation([], ''), None)

    def test_different_length(self):
        self.assertEqual(boolean_generation(['11', '00'], '101'), None)

    def test_too_large(self):
        self.assertEqual(boolean_generation(['111111111111111111111111111111111111111111111111111111111111111111111111111111111111'], '1'), None)

    def test_make_xor(self):
        self.assertEqual(boolean_generation(['00', '01', '10', '11'], '0110'), '~a&b+a&~b')

    def test_make_or(self):
        self.assertEqual(boolean_generation(['00', '01', '10', '11'], '0111'), '~a&b+a&~b+a&b')

    def test_make_and(self):
        self.assertEqual(boolean_generation(['00', '01', '10', '11'], '0001'), 'a&b')

if __name__ == '__main__':
    unittest.main()
