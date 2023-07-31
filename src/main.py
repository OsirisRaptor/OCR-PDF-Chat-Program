import os
import sys
from flask import Flask, request, jsonify

from pdf_reader import read_pdf
from equation_parser import parse_equation
from equation_explainer import explain_equation
from paper_context_analyzer import analyze_context, relate_equation

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected for uploading'}), 400

    if file:
        pdf_file = read_pdf(file)
        equation = parse_equation(pdf_file)
        paper_context = analyze_context(pdf_file)
        equation_explanation = explain_equation(equation)
        context_relation = relate_equation(equation, paper_context)

        return jsonify({
            'equation': equation,
            'equation_explanation': equation_explanation,
            'context_relation': context_relation
        }), 200

    return jsonify({'error': 'Something went wrong'}), 500

if __name__ == '__main__':
    app.run(debug=True)