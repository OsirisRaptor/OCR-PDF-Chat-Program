import unittest
from src.equation_parser import parse_equation

class TestEquationParser(unittest.TestCase):
    def setUp(self):
        self.pdf_file = 'test.pdf'
        self.equation = None

    def test_parse_equation(self):
        self.equation = parse_equation(self.pdf_file)
        self.assertIsNotNone(self.equation, "Failed to parse equation from PDF.")

    def tearDown(self):
        self.pdf_file = None
        self.equation = None

if __name__ == '__main__':
    unittest.main()