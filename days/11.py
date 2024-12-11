import functools
from get_day_input import get_input

data = get_input(day=11)


@functools.lru_cache(maxsize=None)
def _calc_stones(stone: str, blinks: int) -> int:
    if blinks == 0:
        return 1

    new_stones = []
    if stone == "0":
        new_stones.append("1")
    elif len(stone) % 2 == 0:
        new_stones += stone[:len(stone)//2], str(int(stone[len(stone)//2:]))
    else:
        new_stones.append(str(2024 * int(stone)))

    stones = 0
    for new_stone in new_stones:
        stones += _calc_stones(new_stone, blinks-1)
    return stones


def one(blinks: int = 25) -> int:
    """
    Consider the arrangement of stones in front of you. How many stones will you have after blinking 25 times?
    """
    total = 0
    for stone in data.split():
        total += _calc_stones(stone, blinks)
    return total


def two() -> int:
    """
    How many stones would you have after blinking a total of 75 times?
    """
    return one(blinks=75)


print(f"1. {one()}")
print(f"2. {two()}")
