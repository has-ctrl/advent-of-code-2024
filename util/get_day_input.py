from aocd import get_data


def get_input(day: int, year: int = 2024) -> str:
    """
    Retrieve data from the given {day} in {year}
    """
    with open("../cookie.txt", "r") as f:
        cookie = f.read()
    return get_data(session=cookie, day=day, year=year)
