import unittest
from src import utils

class TestUtils(unittest.TestCase):

    def test_read_pdf(self):
        pdf_file = "test.pdf"
        result = utils.read_pdf(pdf_file)
        self.assertIsNotNone(result, "Failed to read PDF file.")

    def test_parse_equation(self):
        pdf_file = "test.pdf"
        result = utils.parse_equation(pdf_file)
        self.assertIsNotNone(result, "Failed to parse equation from PDF file.")

    def test_explain_equation(self):
        equation = "x = y + 2"
        result = utils.explain_equation(equation)
        self.assertIsNotNone(result, "Failed to explain equation.")

    def test_analyze_context(self):
        pdf_file = "test.pdf"
        result = utils.analyze_context(pdf_file)
        self.assertIsNotNone(result, "Failed to analyze paper context.")

    def test_relate_equation(self):
        equation = "x = y + 2"
        paper_context = "In this paper, we discuss the relationship between x and y."
        result = utils.relate_equation(equation, paper_context)
        self.assertIsNotNone(result, "Failed to relate equation to paper context.")

    def test_run_app(self):
        result = utils.run_app()
        self.assertTrue(result, "Failed to run app.")

if __name__ == '__main__':
    unittest.main()