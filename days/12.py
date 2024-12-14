from collections import deque

from get_day_input import get_input

data = get_input(day=12).splitlines()


MAX_Y, MAX_X = len(data), len(data[0])


def one() -> int:
    """
    What is the total price of fencing all regions on your map?
    """
    total = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque()
    visited = set()
    for j, line in enumerate(data):
        for i, plant in enumerate(line):
            if (i, j) in visited:
                continue
            visited.add((i, j))
            queue.appendleft((i, j))
            area = perimeter = 0
            while queue:
                x, y = queue.popleft()
                area += 1
                for d_x, d_y in directions:
                    adj_coords = new_x, new_y = x + d_x, y + d_y
                    if 0 <= new_x < MAX_X and 0 <= new_y < MAX_Y:
                        if data[new_y][new_x] == plant:
                            if adj_coords not in visited:
                                visited.add(adj_coords)
                                queue.append(adj_coords)
                            continue
                    perimeter += 1
            total += area * perimeter
    return total


def two() -> int:
    """
    """
    return 0


print(f"1. {one()}")
print(f"2. {two()}")
