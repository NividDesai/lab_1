# add to src/utils.py (Partner B)

def multiply(*args: Number) -> Number:
    """
    Multiply all arguments together. If no args, return 1 (neutral element).
    """
    if not args:
        return 1
    product = 1
    for x in args:
        product *= x
    return product

def divide(*args: Number) -> float:
    """
    Perform left-associative division: divide(a, b, c) => a / b / c.
    Requires at least one argument. If only one arg, return it as float.
    Raises ZeroDivisionError if any divisor is zero.
    """
    if not args:
        raise ValueError("divide() requires at least one argument")
    result = float(args[0])
    for x in args[1:]:
        if x == 0:
            raise ZeroDivisionError("division by zero")
        result /= x
    return result
