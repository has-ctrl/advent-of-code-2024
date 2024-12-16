from collections import deque
from get_day_input import get_input

warehouse, movements = get_input(day=15).split("\n\n")
warehouse = [list(s) for s in warehouse.splitlines()]
movements = movements.replace("\n", "")
MAX_Y, MAX_X = len(warehouse), len(warehouse[0])
movements_dict = {"<": (-1, 0), ">": (+1, 0), "^": (0, -1), "v": (0, +1)}


def _move(x: int, y: int, d_x: int, d_y: int) -> tuple[int, int]:
    new_x, new_y = x + d_x, y + d_y
    match warehouse[new_y][new_x]:
        case "#":
            return x, y
        case "O":
            if _move(new_x, new_y, d_x, d_y) == (new_x, new_y):
                return x, y
    warehouse[new_y][new_x], warehouse[y][x] = warehouse[y][x], warehouse[new_y][new_x]
    return new_x, new_y


def _get_start() -> tuple[int, int]:
    for j, line in enumerate(warehouse):
        for i, c in enumerate(line):
            if c == "@":
                return i, j


def _calc_score() -> int:
    score = 0
    for j, line in enumerate(warehouse):
        for i, c in enumerate(line):
            if c == "O":
                score += i + 100 * j
    return score


def one() -> int:
    """
    Predict the motion of the robot and boxes in the warehouse. After the robot is finished moving, what is the sum of
    all boxes' GPS coordinates?
    """
    q = deque(movements)
    x, y = _get_start()
    while q:
        move = q.popleft()
        d_x, d_y = movements_dict[move]
        x, y = _move(x, y, d_x, d_y)
    return _calc_score()


def two() -> int:
    """
    """
    return 0


print(f"1. {one()}")
print(f"2. {two()}")
