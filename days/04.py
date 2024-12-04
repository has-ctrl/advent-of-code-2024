from get_day_input import get_input


data = get_input(day=4).splitlines()
XMAS = ("XMAS", "SAMX")
MAX_SIZE = len(data[0]) - 1


def _l(x: int, y: int) -> bool:
    if x >= 3:
        return data[y][x-3:x+1] in XMAS
    return False


def _r(x: int, y: int) -> bool:
    if MAX_SIZE - x >= 3:
        return data[y][x:x+4] in XMAS
    return False


def _u(x: int, y: int) -> bool:
    if y >= 3:
        return "".join(li[x] for li in data[y-3:y+1]) in XMAS
    return False


def _d(x: int, y: int) -> bool:
    if MAX_SIZE - y >= 3:
        return "".join(li[x] for li in data[y:y+4]) in XMAS
    return False


def _lu(x: int, y: int) -> bool:
    if x >= 3 and y >= 3:
        return "".join(li[x-i] for i, li in enumerate(reversed(data[y-3:y+1]))) in XMAS
    return False


def _ru(x: int, y: int) -> bool:
    if MAX_SIZE - x >= 3 and y >= 3:
        return "".join(li[x+i] for i, li in enumerate(reversed(data[y-3:y+1]))) in XMAS
    return False


def _ld(x: int, y: int) -> bool:
    if x >= 3 and MAX_SIZE - y >= 3:
        return "".join(li[x-i] for i, li in enumerate(data[y:y+4])) in XMAS
    return False


def _rd(x: int, y: int) -> bool:
    if MAX_SIZE - x >= 3 and MAX_SIZE - y >= 3:
        return "".join(li[x+i] for i, li in enumerate(data[y:y+4])) in XMAS
    return False


def one() -> int:
    """
    Take a look at the little Elf's word search. How many times does XMAS appear?
    """
    count = 0
    for j, line in enumerate(data):
        for i, char in enumerate(line):
            if char == "X":
                count += _l(i, j) + _r(i, j) + _u(i, j) + _d(i, j) + _lu(i, j) + _ru(i, j) + _ld(i, j) + _rd(i, j)
    return count


def two() -> int:
    """
    """
    return 0


print(f"1. {one()}")
print(f"2. {two()}")