from get_day_input import get_input

data = get_input(day=10).splitlines()
data = [[int(x) for x in line] for line in data]
MAX_X, MAX_Y = len(data[0]), len(data)

trailheads = []
for j, row in enumerate(data):
    for i, val in enumerate(row):
        if val == 0:
            trailheads.append((i, j))


def one(track_distinct_paths: bool = False) -> int:
    """
    The reindeer gleefully carries over a protractor and adds it to the pile. What is the sum of the scores of all
    trailheads on your topographic map?
    """
    count = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for start in trailheads:
        visited = set()
        queue = [start]
        distinct_paths = {start: 1}
        visited.add(start)

        while queue:
            x, y = queue.pop(0)

            if data[y][x] == 9:
                count += 1 if not track_distinct_paths else distinct_paths[(x, y)]
                continue

            for d_x, d_y in directions:
                new = new_x, new_y = x + d_x, y + d_y
                if 0 <= new_x < MAX_X and 0 <= new_y < MAX_Y:
                    if data[new_y][new_x] == data[y][x] + 1:
                        if new not in visited:
                            queue.append(new)
                            visited.add(new)
                        distinct_paths[(new_x, new_y)] = distinct_paths.get((new_x, new_y), 0) + distinct_paths.get((x, y), 0)
    return count


def two() -> int:
    """
    You're not sure how, but the reindeer seems to have crafted some tiny flags out of toothpicks and bits of paper and
    is using them to mark trailheads on your topographic map. What is the sum of the ratings of all trailheads?
    """
    return one(track_distinct_paths=True)


print(f"1. {one()}")
print(f"2. {two()}")
