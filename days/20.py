from collections import defaultdict
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


def _calc_max_picoseconds() -> tuple[dict[tuple, int], int]:
    picoseconds = 0
    start, end = _get_start()
    visited = {start}
    path = {start: picoseconds}
    x, y = start
    while True:
        if (x, y) == end:
            break
        picoseconds += 1
        for d_x, d_y in DIRECTIONS:
            new = new_x, new_y = x + d_x, y + d_y
            if new not in visited and data[new_y][new_x] != "#":
                path[new] = picoseconds
                visited.add(new)
                x, y = new
                break
    return path, picoseconds


def _calc_picoseconds_saved(path: dict, track_length: int, min_saved: int = 100) -> int:
    count = 0
    for x, y in path:
        for d_x, d_y in DIRECTIONS:
            c_x, c_y = x + d_x, y + d_y
            cheat_end = x + d_x * 2, y + d_y * 2
            if cheat_end in path and data[c_y][c_x] == "#":
                if path[(x, y)] + track_length - path[cheat_end] + 2 <= track_length - min_saved:
                    count += 1
    return count


def one() -> int:
    """
    You aren't sure what the conditions of the racetrack will be like, so to give yourself as many options as possible,
    you'll need a list of the best cheats. How many cheats would save you at least 100 picoseconds?
    """
    path, picoseconds = _calc_max_picoseconds()
    return _calc_picoseconds_saved(path, picoseconds)


def two() -> int:
    """
    Find the best cheats using the updated cheating rules. How many cheats would save you at least 100 picoseconds?
    """
    return 0


print(f"1. {one()}")
print(f"2. {two()}")
