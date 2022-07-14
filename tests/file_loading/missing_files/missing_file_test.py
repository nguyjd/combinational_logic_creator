from test_file_loading import load_opcodes_and_names
import unittest

class TestInvalidOpcodes(unittest.TestCase):

    def test(self):
        self.assertEqual(load_opcodes_and_names(), ('nofile', 'nofile'))


if __name__ == '__main__':
    unittest.main()