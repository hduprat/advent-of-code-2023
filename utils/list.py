def split_list(l: list, start: list = [list()]) -> list[list]:
    if len(l) == 0:
        return start
    if l[0].strip() == "":
        return split_list(l[1:], start + [list()])
    start[len(start) - 1].append(l[0].strip())
    return split_list(l[1:], start)
