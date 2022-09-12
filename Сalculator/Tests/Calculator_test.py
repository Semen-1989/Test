import unittest
from Сalculator.First.Сalculator import calculator_test

class MyTestCase(unittest.TestCase):
    def test_plus(self):
        self.assertEqual(calculator_test('2+2'), 4)  # add assertion here

    def test_minus(self):
        self.assertEqual(calculator_test('71-98'), -27)

    def test_multi(self):
        self.assertEqual(calculator_test('1234*98'), 120932)

    def test_divide(self):
        self.assertEqual(calculator_test('14/3'), 4.666666666666667)

    def test_SyntaxError(self):
        self.assertEqual(calculator_test('09 * 7' or "9***4"),
                         "SyntaxError! Please enter a valid value, leading zeros are not allowed in decimal integer literals," \
                         "\nthe number of signs of the operations '*' and '/' must not exceed two and yes, you cannot divide by zero!")

    def test_ValueError(self):
        self.assertEqual(calculator_test('asdfg'), "ValueError! Please enter a valid value!")


if __name__ == '__main__':
    unittest.main()
