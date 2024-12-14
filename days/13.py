import re

from get_day_input import get_input

data = get_input(day=13).split("\n\n")


def one() -> int:
    """
    Figure out how to win as many prizes as possible. What is the fewest tokens you would have to spend to win all
    possible prizes?
    """
    total = 0
    for machine in data:
        machine_tokens = 0
        a_x, a_y, b_x, b_y, p_x, p_y = [int(v) for v in re.findall("\d+", machine)]
        for a in range(100):
            remaining_x = p_x - a * a_x
            if remaining_x % b_x != 0:
                continue
            b = remaining_x // b_x
            if a * a_y + b * b_y == p_y:
                tokens = 3 * a + 1 * b
                machine_tokens = tokens if machine_tokens == 0 or tokens < machine_tokens else machine_tokens
        total += machine_tokens
    return total


def two() -> int:
    """
    """
    return 0


print(f"1. {one()}")
print(f"2. {two()}")
