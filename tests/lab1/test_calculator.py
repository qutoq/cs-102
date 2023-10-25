import unittest

from src.lab1.calculator import Calculator


class CalculatorTestCase(unittest.TestCase):
    def test_Calculator(self):
        self.assertEquals(Calculator().solve("1"), 1)
        self.assertEquals(Calculator().solve("1+1"), 2)
        self.assertEquals(Calculator().solve("2**3"), 8)
        self.assertEquals(Calculator().solve("5*5"), 25)
        self.assertEquals(Calculator().solve("5.5 + 4.5"), 10.0)
        self.assertEquals(Calculator().solve("3&8"), "В вашей формуле есть неккоректные символы")


if __name__ == "__main__":
    unittest.main()
