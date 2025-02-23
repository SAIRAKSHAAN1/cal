"""
Utility functions for input validation and handling.
"""

def validate_number(value: str) -> float:
    """
    Validate and convert string input to float.
    
    Args:
        value: String input to validate
        
    Returns:
        Float value if valid
        
    Raises:
        ValueError: If input cannot be converted to float
    """
    try:
        return float(value)
    except ValueError:
        raise ValueError(f"Invalid number: {value}")

def validate_operator(operator: str) -> str:
    """
    Validate the operator input.
    
    Args:
        operator: String operator to validate
        
    Returns:
        Validated operator
        
    Raises:
        ValueError: If operator is not valid
    """
    valid_operators = {'+', '-', '*', '/'}
    if operator not in valid_operators:
        raise ValueError(f"Invalid operator. Please use one of: {', '.join(valid_operators)}")
    return operator 