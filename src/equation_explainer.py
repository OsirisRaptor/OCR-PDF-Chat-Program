```python
from sympy import sympify, explain

def explain_equation(equation):
    """
    Function to explain how the equation works.
    """
    try:
        # Parse the equation
        parsed_equation = sympify(equation)

        # Explain the equation
        equation_explanation = explain(parsed_equation)

        return equation_explanation

    except Exception as e:
        print(f"Error in explaining the equation: {str(e)}")
        return None
```