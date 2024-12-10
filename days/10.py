from get_day_input import get_input

data = get_input(day=10).splitlines()
data = [[int(x) for x in line] for line in data]
MAX_X, MAX_Y = len(data[0]), len(data)

trailheads = []
for j, row in enumerate(data):
    for i, val in enumerate(row):
        if val == 0:
            trailheads.append((i, j))


def one() -> int:
    """
    The reindeer gleefully carries over a protractor and adds it to the pile. What is the sum of the scores of all
    trailheads on your topographic map?
    """
    count = 0
    for start in trailheads:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = set()
        queue = [start]
        visited.add(start)

        while queue:
            x, y = queue.pop(0)

            if data[y][x] == 9:
                count += 1
                continue

            for d_x, d_y in directions:
                new = new_x, new_y = x + d_x, y + d_y
                if 0 <= new_x < MAX_X and 0 <= new_y < MAX_Y and new not in visited:
                    if data[new_y][new_x] == data[y][x] + 1:
                        queue.append(new)
                        visited.add(new)
    return count


def two() -> int:
    """
    """
    return 0


print(f"1. {one()}")
print(f"2. {two()}")
