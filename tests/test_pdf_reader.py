import unittest
from src.pdf_reader import read_pdf

class TestPdfReader(unittest.TestCase):
    def setUp(self):
        self.pdf_file = 'test.pdf'

    def test_read_pdf(self):
        content = read_pdf(self.pdf_file)
        self.assertIsNotNone(content)

if __name__ == '__main__':
    unittest.main()