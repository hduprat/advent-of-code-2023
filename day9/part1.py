from .oasis import OASIS


def solve(lines):
    oasis = OASIS(lines)
    return sum([ex[-1] for ex in oasis.extrapolations])
