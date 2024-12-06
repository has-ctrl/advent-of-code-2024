from get_day_input import get_input
from copy import deepcopy

data = [list(row) for row in get_input(day=6).splitlines()]


def _get_start() -> (int, int):
    for j, row in enumerate(data):
        for i, char in enumerate(row):
            if char == "^":
                return i, j


def _get_direction_and_new_pos(data_input: list[list[str]], direction: str, x: int, y: int) -> (str, int, int):
    match direction:
        case "^":
            if data_input[y - 1][x] == "#":
                return ">", x, y
            return direction, x, y - 1
        case ">":
            if data_input[y][x + 1] == "#":
                return "v", x, y
            return direction, x + 1, y
        case "<":
            if data_input[y][x - 1] == "#":
                return "^", x, y
            return direction, x - 1, y
        case "v":
            if data_input[y + 1][x] == "#":
                return "<", x, y
            return direction, x, y + 1


def _been_here_before(visited_list: list[tuple[str, int, int]]) -> bool:
    return len(set(visited_list)) != len(visited_list)


def one(data_input: list[list[str]]) -> set[tuple[int, int]] | None:
    """
    Predict the path of the guard. How many distinct positions will the guard visit before leaving the mapped area?
    """
    x, y = _get_start()
    direction = data_input[y][x]
    visited_set = {(x, y)}
    visited_list = [(direction, x, y)]
    while len(data_input) - 1 > y > 0 and len(data_input[0]) - 1 > x > 0:
        direction, x, y = _get_direction_and_new_pos(data_input, direction, x, y)
        visited_set.add((x, y))
        visited_list.append((direction, x, y))
        if _been_here_before(visited_list):
            return None
    return visited_set


def two(visited: set[tuple[int, int]]) -> int:
    """
    You need to get the guard stuck in a loop by adding a single new obstruction. How many different positions could you
    choose for this obstruction?
    """
    count = 0
    for x, y in visited:
        data_copy = deepcopy(data)
        if data_copy[y][x] != "^":
            data_copy[y][x] = "#"
            if not one(data_copy):
                count += 1
    return count


print(f"1. {len(visited_p1 := one(deepcopy(data)))}")
print(f"2. {two(visited_p1)}")
