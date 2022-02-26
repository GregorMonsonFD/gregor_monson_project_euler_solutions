import unittest, ep20


class TestFactorialSum(unittest.TestCase):
    def test_factorial_sum_10_factorial(self):
        result = ep20.factorial_sum(10)
        self.assertEqual(result, 27)

    def test_factorial_sum_1_factorial(self):
        result = ep20.factorial_sum(1)
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()
