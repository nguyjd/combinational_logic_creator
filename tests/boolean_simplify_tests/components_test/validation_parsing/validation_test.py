import unittest
import test_boolean_simplify

class TestValidation(unittest.TestCase):

    def test_nothing(self):
        self.assertEqual(test_boolean_simplify.boolean_simplfy(''), True)

    def test_no_logic(self):
        self.assertEqual(test_boolean_simplify.boolean_simplfy('A'), True)

    def test_one_or(self):
        self.assertEqual(test_boolean_simplify.boolean_simplfy('(A + B)'), True)

    def test_one_and_no_symbol(self):
        self.assertEqual(test_boolean_simplify.boolean_simplfy('(AB)'), True)

    def test_one_and_symbol(self):
        self.assertEqual(test_boolean_simplify.boolean_simplfy('(A * B)'), True)

    def test_one_not(self):
        self.assertEqual(test_boolean_simplify.boolean_simplfy('!A'), True)

    def test_two_not(self):
        self.assertEqual(test_boolean_simplify.boolean_simplfy('!!A'), True)

    def test_not_parenthesis(self):
        self.assertEqual(test_boolean_simplify.boolean_simplfy('!(A + B)'), True)

    def test_and_two_express(self):
        self.assertEqual(test_boolean_simplify.boolean_simplfy('(A + B)*(A + C)'), True)

    def test_or_two_express(self):
        self.assertEqual(test_boolean_simplify.boolean_simplfy('(A + B)+(A + C)'), True)

    def test_or_not_express(self):
        self.assertEqual(test_boolean_simplify.boolean_simplfy('(A + B) + !(A + C)'), True)

    def test_not_two_express(self):
        self.assertEqual(test_boolean_simplify.boolean_simplfy('(A + B)!(A + C)'), True)

    def test_and_not_express(self):
        self.assertEqual(test_boolean_simplify.boolean_simplfy('(A + B) * !(A + C)'), True)

    def test_just_not(self):
        self.assertEqual(test_boolean_simplify.boolean_simplfy('!'), False)

    def test_not_and(self):
        self.assertEqual(test_boolean_simplify.boolean_simplfy('(!A !* !B)'), True)

    def test_or_end(self):
        self.assertEqual(test_boolean_simplify.boolean_simplfy('(A * B)+'), False)

    def test_and_end(self):
        self.assertEqual(test_boolean_simplify.boolean_simplfy('(A * B)*'), False)

    def test_not_end(self):
        self.assertEqual(test_boolean_simplify.boolean_simplfy('(A * B)!'), False)

    def test_and_and(self):
        self.assertEqual(test_boolean_simplify.boolean_simplfy('(A ** B)'), False)

    def test_or_start(self):
        self.assertEqual(test_boolean_simplify.boolean_simplfy('+(A * B)'), False)

    def test_and_start(self):
        self.assertEqual(test_boolean_simplify.boolean_simplfy('*(A * B)'), False)

    def test_and_and(self):
        self.assertEqual(test_boolean_simplify.boolean_simplfy('(A ** B)'), False)

    def test_or_or(self):
        self.assertEqual(test_boolean_simplify.boolean_simplfy('(A ++ B)'), False)

    def test_and_not_and(self):
        self.assertEqual(test_boolean_simplify.boolean_simplfy('(A *!* B)'), False)

if __name__ == '__main__':
    unittest.main()