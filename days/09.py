from get_day_input import get_input
from itertools import pairwise

data = get_input(day=9)


def one() -> int:
    """
    Compact the amphipod's hard drive using the process he requested. What is the resulting filesystem checksum?
    """
    s = list()
    for i, char in enumerate(data):
        if i % 2:
            s += ['.' for _ in range(int(char))]
        else:
            s += [str(i // 2) for _ in range(int(char))]

    space_idxs, fill_chars = [], []
    for i, char in enumerate(s):
        if char == ".":
            space_idxs.append(i)
        else:
            fill_chars.append(char)

    for i in space_idxs:
        s[i] = fill_chars.pop()
    return sum([i * int(v) for i, v in enumerate(s[:len(fill_chars) + len(space_idxs)])])


def two() -> int:
    """
    """
    return 0


print(f"1. {one()}")
print(f"2. {two()}")
