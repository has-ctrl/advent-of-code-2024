from get_day_input import get_input

patterns, designs = get_input(day=19).split("\n\n")
patterns = tuple(patterns.split(", "))
designs = designs.splitlines()
seen_dict = {}


def _match_design(d: str, ps: list[str]) -> int:
    if d in seen_dict:
        return seen_dict[d]

    count = 0
    for p in ps:
        if d.startswith(p):
            count += _match_design(d.removeprefix(p), ps)
        elif not d:
            count = 1
    seen_dict[d] = count
    return count


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
    They'll let you into the onsen as soon as you have the list. What do you get if you add up the number of different
    ways you could make each design?
    """
    count = 0
    for i, design in enumerate(designs):
        count += _match_design(design, patterns)
    return count


print(f"1. {one()}")
print(f"2. {two()}")
