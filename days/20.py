from itertools import combinations
from get_day_input import get_input

DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

data = get_input(day=20).splitlines()


def _get_start() -> tuple[tuple[int, int], tuple[int, int]]:
    s, e = None, None
    for j, line in enumerate(data):
        for i, char in enumerate(line):
            if char == "S":
                s = i, j
            elif char == "E":
                e = i, j
    return s, e


def _calc_max_picoseconds() -> dict[tuple, int]:
    start, end = _get_start()
    visited = {start}
    path = {start: 0}
    x, y = start
    while True:
        if (x, y) == end:
            break
        for d_x, d_y in DIRECTIONS:
            new = new_x, new_y = x + d_x, y + d_y
            if new not in visited and data[new_y][new_x] != "#":
                path[new] = path[(x, y)] + 1
                visited.add(new)
                x, y = new
                break
    return path


def _calc_picoseconds_saved(path: dict,max_time: int = 20, min_saved: int = 100) -> int:
    count = 0
    for ((start_x, start_y), start_dis), ((end_x, end_y), end_dis) in combinations(path.items(), 2):
        distance = abs(start_x - end_x) + abs(start_y - end_y)
        if end_dis - start_dis - distance >= min_saved:
            if distance <= max_time:
                count += 1
    return count


def one(max_time: int = 2) -> int:
    """
    You aren't sure what the conditions of the racetrack will be like, so to give yourself as many options as possible,
    you'll need a list of the best cheats. How many cheats would save you at least 100 picoseconds?
    """
    path = _calc_max_picoseconds()
    return _calc_picoseconds_saved(path, max_time)


def two() -> int:
    """
    Find the best cheats using the updated cheating rules. How many cheats would save you at least 100 picoseconds?
    """
    return one(max_time=20)


print(f"1. {one()}")
print(f"2. {two()}")
