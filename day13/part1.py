from .mirror import MirrorField


def solve(lines):
    field = MirrorField(lines)
    return field.score
