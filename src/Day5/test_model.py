import unittest
from src.Day5.model import Calculator


class TestCalculator(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(2, Calculator.sum(1, 1))
        self.assertEqual(10, Calculator.sum(0, 10))
        self.assertEqual(-3, Calculator.sum(-5, 2))
        self.assertNotEqual(1, Calculator.sum(3, 5))
        self.assertNotEqual(2, Calculator.sum(-1, -1))
        with self.assertRaises(TypeError):
            Calculator.sum(None, 3)

    def test_difference(self):
        raise NotImplemented

    def test_multiplication(self):
        raise NotImplemented

    def test_division(self):
        raise NotImplemented


if __name__ == '__main__':
    unittest.main()