from get_day_input import get_input

data = get_input(day=2).splitlines()
reports = [list(map(int, r.split())) for r in data]


def one(min_diff: int = 1, max_diff: int = 3) -> int:
    """
    Analyze the unusual data from the engineers. How many reports are safe?
    """
    count = 0
    for report in reports:
        is_safe = True
        increasing = report[0] < report[1]
        for current_level, next_level in zip(report, report[1:]):
            diff = next_level - current_level
            if (increasing and min_diff <= diff <= max_diff) or (not increasing and min_diff <= -diff <= max_diff):
                continue
            else:
                is_safe = False
                break
        if is_safe:
            count += 1
    return count


def two() -> int:
    """
    Once again consider your left and right lists. What is their similarity score?
    """
    return 0


print(f"1. {one()}")
print(f"2. {two()}")
