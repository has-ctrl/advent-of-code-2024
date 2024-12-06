from get_day_input import get_input


data = get_input(day=6).splitlines()


def _get_start() -> (int, int):
    for j, row in enumerate(data):
        for i, char in enumerate(row):
            if char == "^":
                return i, j


def one() -> int:
    """
    Predict the path of the guard. How many distinct positions will the guard visit before leaving the mapped area?
    """
    x, y = _get_start()
    direction = "^"
    visited = {(x, y)}
    while len(data) - 1 > y > 0 and len(data[0]) - 1 > x > 0:
        match direction:
            case "^":
                if data[y-1][x] == "#":
                    direction = ">"
                else:
                    x, y = x, y - 1
            case ">":
                if data[y][x+1] == "#":
                    direction = "v"
                else:
                    x, y = x + 1, y
            case "<":
                if data[y][x-1] == "#":
                    direction = "^"
                else:
                    x, y = x - 1, y
            case "v":
                if data[y+1][x] == "#":
                    direction = "<"
                else:
                    x, y = x, y + 1
        visited.add((x, y))
    return len(visited)


def two() -> int:
    """
    """
    return 0


print(f"1. {one()}")
print(f"2. {two()}")
