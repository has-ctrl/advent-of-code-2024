from collections import defaultdict

from get_day_input import get_input

data = get_input(day=12).splitlines()

MAX_Y, MAX_X = len(data), len(data[0])


def one() -> int:
    """
    What is the total price of fencing all regions on your map?
    """
    total = 0
    area_dict, perimeter_dict, expected_dict, visited_dict = {}, {}, defaultdict(set), defaultdict(set)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for y, line in enumerate(data):
        for x, plant in enumerate(line):
            visited_dict[plant].add((x, y))
            expected_dict[plant].add((x, y))
            area_dict[plant] = area_dict.get(plant, 0) + 1
            for d_x, d_y in directions:
                new_x, new_y = x + d_x, y + d_y
                if 0 <= new_x < MAX_X and 0 <= new_y < MAX_Y:
                    if data[new_y][new_x] == plant:
                        expected_dict[plant].add((new_x, new_y))
                        continue
                perimeter_dict[plant] = perimeter_dict.get(plant, 0) + 1

            if expected_dict[plant] == visited_dict[plant]:
                total += area_dict[plant] * perimeter_dict.get(plant, 0)
                area_dict[plant], perimeter_dict[plant] = 0, 0
    return total


def two() -> int:
    """
    """
    return 0


print(f"1. {one()}")
print(f"2. {two()}")
