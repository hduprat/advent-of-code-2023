from .oasis import OASIS


def solve(lines):
    oasis = OASIS(lines)
    return sum([ex[0] for ex in oasis.backwards_extrapolations])
