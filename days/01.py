from get_day_input import get_input


data = get_input(day=1).splitlines()

l1, l2 = [], []
for line in data:
    x, y = line.split()
    l1.append(int(x))
    l2.append(int(y))


def one() -> int:
    """
    What is the total distance between your lists?
    """
    total = 0
    sorted_l1 = sorted(l1)
    sorted_l2 = sorted(l2)
    for i, j in zip(sorted_l1, sorted_l2):
        total += abs(i - j)
    return total


def two() -> int:
    """
    """
    pass


print(f"1. {one()}")
print(f"2. {two()}")
