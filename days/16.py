from collections import deque
from get_day_input import get_input

data = get_input(day=16).splitlines()

MAX_X, MAX_Y = len(data[0]), len(data)
start, end = None, None
for j, line in enumerate(data):
    for i, char in enumerate(line):
        if char == "S":
            start = i, j
        elif char == "E":
            end = i, j


def one() -> int:
    """
    Analyze your map carefully. What is the lowest score a Reindeer could possibly get?
    """
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    visited = set()
    queue = deque([(start[0], start[1], dirs[0], 0)])
    while queue:
        x, y, d, c = queue.popleft()
        if (x, y, d) in visited:
            continue
        elif (x, y) == end:
            return c

        visited.add((x, y, d))

        for d_x, d_y in dirs:
            new_x, new_y = x + d_x, y + d_y
            if 0 <= new_x < MAX_X and 0 <= new_y < MAX_Y:
                if data[new_y][new_x] != "#":
                    if d == (d_x, d_y):
                        queue.appendleft((new_x, new_y, (d_x, d_y), c + 1))
                    else:
                        queue.append((new_x, new_y, (d_x, d_y), c + 1001))


def two() -> int:
    """
    """
    return 0


print(f"1. {one()}")
print(f"2. {two()}")
