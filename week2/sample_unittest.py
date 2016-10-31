import unittest
import my_module


class TestWordFrequency(unittest.TestCase):

    def test_assert_true(self):
        self.assertTrue(my_module.is_true())

    def test_assert_false(self):
        self.assertFalse(my_module.is_false())

    def test_assert_equal(self):
        self.assertEqual(my_module.get_one(), 1)

    def test_assert_not_equal(self):
        self.assertNotEqual(my_module.get_one(), 0)


if __name__ == '__main__':
    unittest.main()

