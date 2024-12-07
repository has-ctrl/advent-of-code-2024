from get_day_input import get_input
from itertools import product

data = get_input(day=7).splitlines()


def _parse_input(equation: str) -> tuple[int, list[str]]:
    sub_total, values = equation.split(":")
    return int(sub_total), values.split()


def one(operators_input: tuple[str] = ("*", "+")) -> int:
    """
    Determine which equations could possibly be true. What is their total calibration result?
    """
    total = 0
    for equation in data:
        sub_total, values = _parse_input(equation)
        operator_config = list(product(operators_input, repeat=len(values)-1))
        for operators in operator_config:
            count = 0
            for i, (x, y) in enumerate(zip(values, values[1:])):
                operator = operators[i]
                count += int(x) if i == 0 else 0
                if operator == "||":
                    count = int(str(count) + y)
                elif operator == "+":
                    count += int(y)
                elif operator == "*":
                    count *= int(y)
                if count > sub_total:
                    break
            if count == sub_total:
                total += sub_total
                break
    return total


def two(operators_input: tuple[str] = ("||", "*", "+")) -> int:
    """
    Using your new knowledge of elephant hiding spots, determine which equations could possibly be true. What is their
    total calibration result?
    """
    return one(operators_input)


print(f"1. {one()}")
print(f"2. {two()}")
