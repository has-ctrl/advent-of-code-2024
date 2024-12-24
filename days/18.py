from collections import deque
from get_day_input import get_input

data = get_input(day=18).splitlines()
MAX_X = MAX_Y = 71


def _create_grid(steps: int) -> tuple[list[list[str]], int, int]:
    grid = [["." for _ in range(MAX_X)] for _ in range(MAX_Y)]
    for i, coords in enumerate(data):
        x, y = coords.split(",")
        grid[int(y)][int(x)] = "#"
        if i == steps - 1:
            return grid, int(x), int(y)


def one(simulate_steps: int = 1024) -> (int | tuple[int, int]):
    """
    Simulate the first kilobyte (1024 bytes) falling onto your memory space. Afterward, what is the minimum number of
    steps needed to reach the exit?
    """
    grid, byte_x, byte_y = _create_grid(simulate_steps)
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    visited = set()

    start_x, start_y, end_x, end_y = 0, 0, MAX_X - 1, MAX_Y - 1
    queue = deque([(start_x, start_y, 0)])
    visited.add((start_x, start_y))
    while queue:
        x, y, c = queue.popleft()

        if (x, y) == (end_x, end_y):
            return c

        for d_x, d_y in dirs:
            new = new_x, new_y = x + d_x, y + d_y
            if 0 <= new_x < MAX_X and 0 <= new_y < MAX_Y:
                if grid[new_y][new_x] != "#" and new not in visited:
                    visited.add(new)
                    queue.append((new_x, new_y, c + 1))
    return byte_x, byte_y


def two() -> tuple[int, int]:
    """
    Simulate more of the bytes that are about to corrupt your memory space. What are the coordinates of the first byte
    that will prevent the exit from being reachable from your starting position? (Provide the answer as two integers
    separated by a comma with no other characters.)
    """
    for steps in range(1024, 100_000):
        res = one(steps)
        if not isinstance(res, int):
            return res


print(f"1. {one()}")
print(f"2. {two()}")
