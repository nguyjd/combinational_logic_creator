from test_file_loading import load_opcodes_and_names
import unittest

class TestEmptyNamesFile(unittest.TestCase):

    def test(self):
        self.assertEqual(load_opcodes_and_names(), (['100111011'], 'empty'))


if __name__ == '__main__':
    unittest.main()