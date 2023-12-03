from .engine import Engine


def solve(lines):
    engine = Engine(lines)

    return sum(engine.gear_ratios)
