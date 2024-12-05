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


def _is_ordered(li: list[int]) -> (bool, int | None):
    ordered = True
    unordered_idx = None
    for i, page_r in enumerate(li):
        if page_r in rule_dict:
            for page_l in li[i+1:]:
                if page_l in rule_dict[page_r]:
                    ordered = False
                    unordered_idx = i
                    break
        if not ordered:
            break
    return ordered, unordered_idx


def one() -> (int, list[int]):
    """
    Determine which updates are already in the correct order. What do you get if you add up the middle page number from
    those correctly-ordered updates?
    """
    count = 0
    unordered_updates = []
    for update in updates:
        ordered, _ = _is_ordered(update)
        if ordered:
            count += update[len(update) // 2]
        else:
            unordered_updates.append(update)
    return count, unordered_updates


def two(unordered_updates: list[list[int]]) -> int:
    """
    Find the updates which are not in the correct order. What do you get if you add up the middle page numbers after
    correctly ordering just those updates?
    """
    count = 0
    for update in unordered_updates:
        update_copy = update[:]
        for _ in range(len(update_copy)):
            for i in range(len(update_copy) - 1):
                page_l, page_r = update_copy[i], update_copy[i+1]
                if page_l in rule_dict and page_r in rule_dict[page_l]:
                    update_copy[i], update_copy[i + 1] = update_copy[i + 1], update_copy[i]
        count += update_copy[len(update_copy) // 2]
    return count


answer, new_input = one()
print(f"1. {answer}")
print(f"2. {two(unordered_updates=new_input)}")
