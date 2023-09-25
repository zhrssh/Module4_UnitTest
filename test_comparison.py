import unittest

def isGreaterThanOrEqual100(number):
    return number >= 100

class TestComparison(unittest.TestCase):
    def test(self):
        self.assertTrue(isGreaterThanOrEqual100(999), "Number is not greater than or equal 100")

if __name__ == "__main__":
    unittest.main()