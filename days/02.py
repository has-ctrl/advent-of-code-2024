from get_day_input import get_input

data = get_input(day=2).splitlines()
reports = [list(map(int, r.split())) for r in data]

MIN_DIFF, MAX_DIFF = 1, 3


def _is_safe_report(report: list[int], dampener: bool) -> bool:
    increasing = report[0] < report[1]
    for i, (current_level, next_level) in enumerate(zip(report, report[1:])):
        diff = next_level - current_level
        if (increasing and MIN_DIFF <= diff <= MAX_DIFF) or (not increasing and MIN_DIFF <= -diff <= MAX_DIFF):
            continue
        elif not dampener:
            return False
        else:
            for j, _ in enumerate(report):
                temp_report = report[:j] + report[j+1:]
                is_actually_safe = _is_safe_report(temp_report, dampener=False)
                if is_actually_safe:
                    return True
            return False
    return True


def one() -> int:
    """
    Analyze the unusual data from the engineers. How many reports are safe?
    """
    count = 0
    for report in reports:
        is_safe = _is_safe_report(report, dampener=False)
        if is_safe:
            count += 1
    return count


def two() -> int:
    """
    Update your analysis by handling situations where the Problem Dampener can remove a single level from unsafe
    reports. How many reports are now safe?
    """
    count = 0
    for report in reports:
        is_safe = _is_safe_report(report, dampener=True)
        if is_safe:
            count += 1
    return count


print(f"1. {one()}")
print(f"2. {two()}")
