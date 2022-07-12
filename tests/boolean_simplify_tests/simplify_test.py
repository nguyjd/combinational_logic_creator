from test_boolean_simplify import *
import unittest

class TestSimplify(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(boolean_simplfy(''), None)

    def test_Idempotent_one(self):
        self.assertEqual(boolean_simplfy('A+A'), 'A')

    def test_Idempotent_two(self):
        self.assertEqual(boolean_simplfy('A&A'), 'A')

    def test_double_negation(self):
        self.assertEqual(boolean_simplfy('~~A'), 'A')

    def test_triple_negation(self):
        self.assertEqual(boolean_simplfy('~~~A'), '~A')

    def test_example_one(self):
        self.assertEqual(boolean_simplfy('C + !(B&C)'), '1')

    def test_example_two(self):
        self.assertEqual(boolean_simplfy('!(A&B)&(!A + B)&(!B + B)'), '~A')

    def test_example_three(self):
        self.assertEqual(boolean_simplfy('(A + C)&(A&D + A&~D) + A&C + C'), 'A|C')

    def test_example_four(self):
        self.assertEqual(boolean_simplfy('~A&(A+B)+(B+A&A)&(A+~B)'), 'A|B')

if __name__ == '__main__':
    unittest.main()
