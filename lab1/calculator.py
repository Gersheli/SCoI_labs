import math_operations


def calculate(a, b, operation):
    if operation == math_operations.DIVISION:
        return a / b
    elif operation == math_operations.MULTIPLICATION:
        return a * b
    elif operation == math_operations.SUBTRACTION:
        return a - b
    elif operation == math_operations.ADDITION:
        return a + b
    else:
        raise Exception('There is no such operation.')
