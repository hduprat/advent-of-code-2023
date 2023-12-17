from .hash import hash


def solve(lines):
    instructions = lines[0].strip().split(",")
    return sum(map(hash, instructions))
