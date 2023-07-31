```python
import os
import sys

def validate_file(pdf_file):
    """
    Function to validate if the provided file is a PDF and exists.
    """
    if not pdf_file.endswith('.pdf'):
        print("Invalid file type. Please provide a PDF file.")
        sys.exit(1)

    if not os.path.exists(pdf_file):
        print("File does not exist. Please provide a valid file path.")
        sys.exit(1)

def validate_equation(equation):
    """
    Function to validate if the provided equation is a string.
    """
    if not isinstance(equation, str):
        print("Invalid equation. Please provide an equation as a string.")
        sys.exit(1)

def validate_context(paper_context):
    """
    Function to validate if the provided paper context is a string.
    """
    if not isinstance(paper_context, str):
        print("Invalid context. Please provide the paper context as a string.")
        sys.exit(1)
```