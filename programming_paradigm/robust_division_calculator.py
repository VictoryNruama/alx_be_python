# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """Safely divide two numbers with error handling."""
    try:
        # Convert inputs to floats
        numerator = float(numerator)
        denominator = float(denominator)

        # Attempt division
        result = numerator / denominator
        return f"The result of the division is {result}"

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
