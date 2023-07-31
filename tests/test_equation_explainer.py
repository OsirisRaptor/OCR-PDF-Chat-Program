import unittest
from src.equation_explainer import explain_equation

class TestEquationExplainer(unittest.TestCase):
    def setUp(self):
        self.equation = "x = y + 2"

    def test_explain_equation(self):
        explanation = explain_equation(self.equation)
        self.assertIsNotNone(explanation, "Explanation should not be None")
        self.assertIsInstance(explanation, str, "Explanation should be a string")

if __name__ == "__main__":
    unittest.main()