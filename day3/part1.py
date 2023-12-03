from .engine import Engine


def solve(lines):
    engine = Engine(lines)

    return sum(engine.part_numbers)
