from functools import cache

from get_day_input import get_input

patterns, designs = get_input(day=19).split("\n\n")
patterns = tuple(patterns.split(", "))
designs = designs.splitlines()


@cache
def _match_design(d: str, ps: list[str]) -> bool:
    for p in ps:
        if d.startswith(p):
            if _match_design(d.removeprefix(p), ps):
                return True
        elif not d:
            return True
    return False


def one() -> int:
    """
    To get into the onsen as soon as possible, consult your list of towel patterns and desired designs carefully. How
    many designs are possible?
    """
    count = 0
    for i, design in enumerate(designs):
        if _match_design(design, patterns):
            count += 1
    return count


def two() -> int:
    """
    """
    return 0


print(f"1. {one()}")
print(f"2. {two()}")
