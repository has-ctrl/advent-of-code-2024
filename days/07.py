from get_day_input import get_input
from itertools import product

data = get_input(day=7).splitlines()


OPERATORS = ["*", "+"]


def one() -> int:
    """
    Determine which equations could possibly be true. What is their total calibration result?
    """
    total = 0
    for equation in data:
        sub_total, values = equation.split(":")
        sub_total = int(sub_total)
        values = [int(v) for v in values.split()]
        operator_config = list(product(OPERATORS, repeat=len(values)-1))
        for operators in operator_config:
            count = 0
            for i, (x, y) in enumerate(zip(values, values[1:])):
                if i == 0:
                    count += x
                if operators[i] == "+":
                    count += y
                elif operators[i] == "*":
                    count *= y
                if count > sub_total:
                    break
            if count == sub_total:
                total += sub_total
                break
    return total


def two() -> int:
    """
    """
    return 0


print(f"1. {one()}")
print(f"2. {two()}")
