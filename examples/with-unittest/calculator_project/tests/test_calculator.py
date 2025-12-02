import unittest
from main import Calculator


print("Running calculator tests...", Calculator)
class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

if __name__ == '__main__':
    unittest.main()