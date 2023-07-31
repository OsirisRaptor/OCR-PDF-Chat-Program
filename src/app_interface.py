from flask import Flask, request, jsonify
from src.pdf_reader import read_pdf
from src.equation_parser import parse_equation
from src.equation_explainer import explain_equation
from src.paper_context_analyzer import analyze_context, relate_equation

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected for uploading'}), 400

    pdf_file = read_pdf(file)
    equation = parse_equation(pdf_file)
    equation_explanation = explain_equation(equation)
    paper_context = analyze_context(pdf_file)
    context_relation = relate_equation(equation, paper_context)

    return jsonify({
        'equation': equation,
        'equation_explanation': equation_explanation,
        'context_relation': context_relation
    }), 200

def run_app():
    app.run(debug=True)

if __name__ == "__main__":
    run_app()