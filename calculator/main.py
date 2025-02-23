"""
Command-line interface for the calculator application.
"""

from operations import add, subtract, multiply, divide
from utils import validate_number, validate_operator

def calculate(a: float, operator: str, b: float) -> float:
    """Perform calculation based on operator."""
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
    }
    return operations[operator](a, b)

def main():
    """Main CLI interface for the calculator."""
    print("Welcome to Python Calculator!")
    print("Enter 'q' to quit")
    
    while True:
        try:
            # Get first number
            first = input("\nEnter first number: ")
            if first.lower() == 'q':
                break
            num1 = validate_number(first)
            
            # Get operator
            operator = input("Enter operator (+, -, *, /): ")
            if operator.lower() == 'q':
                break
            op = validate_operator(operator)
            
            # Get second number
            second = input("Enter second number: ")
            if second.lower() == 'q':
                break
            num2 = validate_number(second)
            
            # Calculate and display result
            result = calculate(num1, op, num2)
            print(f"\nResult: {num1} {op} {num2} = {result}")
            
        except ValueError as e:
            print(f"\nError: {e}")
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")

if __name__ == "__main__":
    main() 