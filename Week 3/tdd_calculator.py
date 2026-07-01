import unittest

# Calculator Class
class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b


# Test Cases
class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    # RED: Write failing test
    def test_add(self):
        self.assertEqual(self.calc.add(10, 5), 15)

    # GREEN: Make test pass
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)

    # REFACTOR: Improve without changing behavior
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(10, 5), 50)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 5), 2)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)


if __name__ == "__main__":
    unittest.main()
