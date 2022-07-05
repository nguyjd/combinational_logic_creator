import unittest
import test_boolean_simplify

class TestParsingParenthesis(unittest.TestCase):

    def test_single_parenthesis(self):
        self.assertEqual(test_boolean_simplify.boolean_simplfy('(A + B)'), [[0,4]])

    def test_no_left_parenthesis(self):
        self.assertEqual(test_boolean_simplify.boolean_simplfy('(A + B'), None)

    def test_no_right_parenthesis(self):
        self.assertEqual(test_boolean_simplify.boolean_simplfy('A + B)'), None)

    def test_no_parenthesis(self):
        self.assertEqual(test_boolean_simplify.boolean_simplfy('A + B'), [])

    def test_two_non_overlapping_parenthesis(self):
        self.assertEqual(test_boolean_simplify.boolean_simplfy('(A + B)(A + C)'), [[0,4],[5,9]])

    def test_two_overlapping_parenthesis(self):
        self.assertEqual(test_boolean_simplify.boolean_simplfy('(A + B(A + C))'), [[4,8],[0,9]])

    def test_three_non_overlapping_parenthesis(self):
        self.assertEqual(test_boolean_simplify.boolean_simplfy('(A + B)(A + C)(A + D)'), [[0,4],[5,9],[10,14]])

    def test_three_overlapping_parenthesis(self):
        self.assertEqual(test_boolean_simplify.boolean_simplfy('(A(A + B(A + C)))'), [[6,10],[2,11],[0,12]])

if __name__ == '__main__':
    unittest.main()