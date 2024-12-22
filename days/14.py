import re
from get_day_input import get_input

data = get_input(day=14).splitlines()
MAX_X, MAX_Y = 101, 103


def one(seconds_elapsed: int = 100) -> int:
    """
    Predict the motion of the robots in your list within a space which is 101 tiles wide and 103 tiles tall. What will
    the safety factor be after exactly 100 seconds have elapsed?
    """
    ne = nw = se = sw = 0
    for robot in data:
        x, y, v_x, v_y = [int(v) for v in re.findall(r"-?[0-9]+", robot)]
        x = (x + v_x * seconds_elapsed) % MAX_X
        y = (y + v_y * seconds_elapsed) % MAX_Y
        if x < MAX_X // 2 and y < MAX_Y // 2:
            nw += 1
        elif x > MAX_X // 2 and y < MAX_Y // 2:
            ne += 1
        elif x < MAX_X // 2 and y > MAX_Y // 2:
            sw += 1
        elif x > MAX_X // 2 and y > MAX_Y // 2:
            se += 1
    return ne * nw * se * sw


def two() -> int:
    """
    What is the fewest number of seconds that must elapse for the robots to display the Easter egg?
    """
    for seconds_elapsed in range(1_000_000):
        grid = [["." for _ in range(MAX_X)] for _ in range(MAX_Y)]
        for robot in data:
            x, y, v_x, v_y = [int(v) for v in re.findall(r"-?[0-9]+", robot)]
            new_x = (x + v_x * seconds_elapsed) % MAX_X
            new_y = (y + v_y * seconds_elapsed) % MAX_Y
            grid[new_y][new_x] = "#"
        for line in grid:
            s = "".join(line)
            if "#########" in s:
                return seconds_elapsed


print(f"1. {one()}")
print(f"2. {two()}")
