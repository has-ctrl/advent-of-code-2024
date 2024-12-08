from get_day_input import get_input
from collections import defaultdict
from itertools import combinations


raw_data = get_input(day=8).splitlines()
MAX_X, MAX_Y = len(raw_data[0]), len(raw_data)

data = defaultdict(list)
for j, row in enumerate(raw_data):
    for i, char in enumerate(row):
        if char != '.':
            data[char] += [(i, j)]


def one() -> int:
    """
    """
    antinodes = set()
    for _, coords in data.items():
        for (x1, y1), (x2, y2) in combinations(coords, 2):
            x_distance, y_distance = x1 - x2, y1 - y2
            antinodes.add((x1 + x_distance, y1 + y_distance))
            antinodes.add((x2 - x_distance, y2 - y_distance))
    return len([(x, y) for x, y in antinodes if 0 <= x < MAX_X and 0 <= y < MAX_Y])


def two() -> int:
    """
    """
    return 0


print(f"1. {one()}")
print(f"2. {two()}")
