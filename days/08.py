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


def _is_valid(x: int, y: int) -> bool:
    return 0 <= x < MAX_X and 0 <= y < MAX_Y


def one(boost: bool = False) -> int:
    """
    Calculate the impact of the signal. How many unique locations within the bounds of the map contain an antinode?
    """
    antinodes = set()
    for _, coords in data.items():
        for (x1, y1), (x2, y2) in combinations(coords, 2):
            if boost:
                antinodes.add((x1, y1))
                antinodes.add((x2, y2))
            x_distance, y_distance = x1 - x2, y1 - y2
            while True:
                x1, y1 = x1 + x_distance, y1 + y_distance
                x2, y2 = x2 - x_distance, y2 - y_distance
                if val1 := _is_valid(x1, y1):
                    antinodes.add((x1, y1))
                if val2 := _is_valid(x2, y2):
                    antinodes.add((x2, y2))
                if not boost or (not val1 and not val2):
                    break
    return len(antinodes)


def two() -> int:
    """
    Calculate the impact of the signal using this updated model. How many unique locations within the bounds of the map
    contain an antinode?
    """
    return one(boost=True)


print(f"1. {one()}")
print(f"2. {two()}")
