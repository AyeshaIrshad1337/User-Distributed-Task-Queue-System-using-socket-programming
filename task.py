import math
import time
def compute_factorial(n):
    """Compute the factorial of n."""
    return math.factorial(n)

def add(*args):
    """Add any number of values."""
    return sum(args)

def subtract(a, b, *args):
    """Subtract two or more numbers, starting with the first two."""
    result = a - b
    for arg in args:
        result -= arg
    return result

def multiply(*args):
    """Multiply any number of values."""
    result = 1
    for arg in args:
        result *= arg
    return result

def divide(a, b):
    """Divide the first number by the second. Raises an error if dividing by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def execute_task(task_type, *args):
    if task_type == 'factorial' and len(args) == 1:
        return compute_factorial(args[0])
    elif task_type == 'add':
        return add(*args)
    elif task_type == 'subtract':
        return subtract(*args)
    elif task_type == 'multiply':
        return multiply(*args)
    elif task_type == 'divide' and len(args) == 2:
        return divide(args[0], args[1])
    else:
        return "Unknown task or incorrect parameters"

if __name__ == "__main__":
    # Example usage
    print(execute_task('factorial', 5))  # Calculate factorial of 5
    print(execute_task('add', 1, 2, 3))  # Add 1, 2, and 3
    print(execute_task('subtract', 10, 5, 1))  # Subtract 1 from 5 from 10
    print(execute_task('multiply', 2, 3, 4))  # Multiply 2, 3, and 4
    print(execute_task('divide', 20, 4))  # Divide 20 by 4
