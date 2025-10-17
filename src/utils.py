# src/utils.py

from typing import Union

Number = Union[int, float]

def add(*args: Number) -> Number:
    """Return the sum of all provided arguments. Returns 0 if no args."""
    return sum(args) if args else 0

def subtract(*args: Number) -> Number:
    """Subtract subsequent args from the first. Raises error if none given."""
    if not args:
        raise ValueError("subtract() requires at least one argument")
    result = args[0]
    for x in args[1:]:
        result -= x
    return result
