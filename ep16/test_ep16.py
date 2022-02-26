import unittest
import ep16


class TestPower(unittest.TestCase):

    def test_power_sum_example(self):
        result = ep16.power_sum(2, 15)
        self.assertEqual(result, 26)  # add assertion here


if __name__ == '__main__':
    unittest.main()
