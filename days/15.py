from collections import deque
from get_day_input import get_input

warehouse, movements = get_input(day=15).split("\n\n")
movements = movements.replace("\n", "")
movements_dict = {"<": (-1, 0), ">": (+1, 0), "^": (0, -1), "v": (0, +1)}


def _move(x: int, y: int, d_x: int, d_y: int, wh: list[list[str]], try_only: bool = False) -> tuple[int, int]:
    new_x, new_y = x + d_x, y + d_y
    match wh[new_y][new_x], d_y:
        case "#", _:
            return x, y
        case ("O", _) | ("[", 0) | ("]", 0):
            if _move(new_x, new_y, d_x, d_y, wh, try_only) == (new_x, new_y):
                return x, y
        case ("[", 1) | ("[", -1):
            up_down = _move(new_x, new_y, d_x, d_y, wh, try_only=True) == (new_x, new_y)
            right = _move(new_x + 1, new_y, d_x, d_y, wh, try_only=True) == (new_x + 1, new_y)
            if up_down or right:
                return x, y
            _move(new_x, new_y, d_x, d_y, wh, try_only)
            _move(new_x + 1, new_y, d_x, d_y, wh, try_only)
        case ("]", 1) | ("]", -1):
            up_down = _move(new_x, new_y, d_x, d_y, wh, try_only=True) == (new_x, new_y)
            left = _move(new_x - 1, new_y, d_x, d_y, wh, try_only=True) == (new_x - 1, new_y)
            if up_down or left:
                return x, y
            _move(new_x, new_y, d_x, d_y, wh, try_only)
            _move(new_x - 1, new_y, d_x, d_y, wh, try_only)
    if not try_only:
        wh[new_y][new_x], wh[y][x] = wh[y][x], wh[new_y][new_x]
    return new_x, new_y


def _get_start(wh: list[list[str]]) -> tuple[int, int]:
    for j, line in enumerate(wh):
        for i, c in enumerate(line):
            if c == "@":
                return i, j


def _calc_score(wh: list[list[str]]) -> int:
    score = 0
    for j, line in enumerate(wh):
        for i, c in enumerate(line):
            if c in ("O", "["):
                score += i + 100 * j
    return score


def one() -> int:
    """
    Predict the motion of the robot and boxes in the warehouse. After the robot is finished moving, what is the sum of
    all boxes' GPS coordinates?
    """
    wh = [list(s) for s in warehouse.splitlines()][:]
    q = deque(movements)
    x, y = _get_start(wh)
    while q:
        move = q.popleft()
        d_x, d_y = movements_dict[move]
        x, y = _move(x, y, d_x, d_y, wh)
    return _calc_score(wh)


def two() -> int:
    """
    """
    wh = [list(s.replace("#", "##").replace("O", "[]").replace(".", "..").replace("@", "@.")) for s in
          warehouse.splitlines()][:]
    q = deque(movements)
    x, y = _get_start(wh)
    while q:
        move = q.popleft()
        d_x, d_y = movements_dict[move]
        x, y = _move(x, y, d_x, d_y, wh)
    return _calc_score(wh)


print(f"1. {one()}")
print(f"2. {two()}")
