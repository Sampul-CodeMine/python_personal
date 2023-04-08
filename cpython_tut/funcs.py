def add(a: int, b: int) -> int:
    return a + b


def sub(a: int, b: int) -> int:
    return a - b


def mult(a: int, b: int) -> int:
    return a * b


def divi(a: int, b: int) -> float:
    try:
        return a / b
    except (ValueError, ZeroDivisionError):
        return

