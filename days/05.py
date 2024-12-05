from get_day_input import get_input


rules, updates = get_input(day=5).split("\n\n")
updates = [[int(x) for x in line.split(",")] for line in updates.splitlines()]
rule_dict = {}
for rule in rules.splitlines():
    x, y = rule.split("|")
    x, y = int(x), int(y)
    if y in rule_dict:
        rule_dict[y] += [x]
    else:
        rule_dict[y] = [x]


def one() -> int:
    """
    Determine which updates are already in the correct order. What do you get if you add up the middle page number from
    those correctly-ordered updates?
    """
    count = 0
    for update in updates:
        ordered = True
        for i, page in enumerate(update):
            if page in rule_dict:
                for j in update[i+1:]:
                    if j in rule_dict[page]:
                        ordered = False
            if not ordered:
                break
        if ordered:
            count += update[len(update) // 2]
    return count


def two() -> int:
    """
    """
    return 0


print(f"1. {one()}")
print(f"2. {two()}")
