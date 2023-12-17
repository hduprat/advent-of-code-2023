type Point = tuple[int, int]


def manhattan_distance(a: Point, b: Point) -> int:
    return sum(map(lambda a_i, b_i: abs(a_i - b_i), a, b))


def scalar(a: Point, b: Point) -> int:
    return sum(map(lambda a_i, b_i: a_i * b_i, a, b))
