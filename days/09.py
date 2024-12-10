from get_day_input import get_input

data = get_input(day=9)


def one() -> int:
    """
    Compact the amphipod's hard drive using the process he requested. What is the resulting filesystem checksum?
    """
    s = list()
    for i, char in enumerate(data):
        if i % 2:
            s += ["." for _ in range(int(char))]
        else:
            s += [str(i // 2) for _ in range(int(char))]

    space_idxs, fill_chars = [], []
    for i, char in enumerate(s):
        if char == ".":
            space_idxs.append(i)
        else:
            fill_chars.append(char)

    for i in space_idxs:
        s[i] = fill_chars.pop()
    return sum([i * int(v) for i, v in enumerate(s[:len(fill_chars) + len(space_idxs)])])


def two() -> int:
    """
    Start over, now compacting the amphipod's hard drive using this new method instead. What is the resulting filesystem
    checksum?
    """
    s = list()
    for i, char in enumerate(data):
        if char == '0':
            continue
        if i % 2:
            s += [tuple("." for _ in range(int(char)))]
        else:
            s += [tuple(str(i // 2) for _ in range(int(char)))]

    space_idxs, fill_idxs = {}, {}
    for i, tup in enumerate(s):
        if not tup or "." in tup:
            space_idxs[i] = len(tup)
        else:
            fill_idxs[i] = len(tup)

    for file_idx, file_size in reversed(list(fill_idxs.items())):
        for space_idx, space in space_idxs.items():
            if space >= file_size and file_idx > space_idx:
                if s[space_idx][0] == ".":
                    s[space_idx], s[file_idx] = s[file_idx], s[space_idx]
                else:
                    s[space_idx] = s[space_idx][:len(s[space_idx]) - space] + s[file_idx]
                    s[file_idx] = tuple(["." for _ in range(file_size)])
                fill_idxs.pop(file_idx)
                space_idxs[space_idx] = space - file_size
                if space > file_size:
                    s[space_idx] += tuple(["." for _ in range(space - file_size)])
                    s[file_idx] = tuple(["." for _ in range(file_size)])
                break
    return sum([i * int(v) for i, v in enumerate([c for tup in s for c in tup]) if v != "."])


print(f"1. {one()}")
print(f"2. {two()}")
