import unittest
from src.paper_context_analyzer import analyze_context

class TestPaperContextAnalyzer(unittest.TestCase):
    def setUp(self):
        self.pdf_file = 'sample.pdf'
        self.paper_context = None

    def test_analyze_context(self):
        self.paper_context = analyze_context(self.pdf_file)
        self.assertIsNotNone(self.paper_context, "Failed to analyze paper context.")

    def tearDown(self):
        self.pdf_file = None
        self.paper_context = None

if __name__ == '__main__':
    unittest.main()