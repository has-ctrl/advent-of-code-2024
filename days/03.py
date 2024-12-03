import re
from get_day_input import get_input

data = get_input(day=3)


def one() -> int:
    """
    Scan the corrupted memory for uncorrupted mul instructions. What do you get if you add up all of the results of the
    multiplications?
    """
    values = re.findall(r"mul\((\d+),(\d+)\)", data)
    multiplications = [int(x) * int(y) for x, y in values]
    return sum(multiplications)


def two() -> int:
    """
    """
    count = 0
    enabled = True
    values = re.findall(r"(do\(\)|don't\(\))|mul\((\d+),(\d+)\)", data)
    for condition, x, y in values:
        match condition:
            case "don't()":
                enabled = False
                continue
            case "do()":
                enabled = True
                continue
        if enabled:
            count += int(x) * int(y)
    return count


print(f"1. {one()}")
print(f"2. {two()}")
