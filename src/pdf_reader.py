```python
import os
import PyPDF2

def read_pdf(pdf_file):
    """
    Function to read the PDF file.
    """
    if not os.path.exists(pdf_file):
        raise FileNotFoundError(f"{pdf_file} does not exist.")

    with open(pdf_file, 'rb') as file:
        pdf_reader = PyPDF2.PdfFileReader(file)
        total_pages = pdf_reader.numPages
        paper_context = ''

        for page_num in range(total_pages):
            page = pdf_reader.getPage(page_num)
            paper_context += page.extractText()

    return paper_context
```