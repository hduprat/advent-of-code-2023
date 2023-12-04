from .scratchcard import Scratchcard


def solve(lines):
    return sum(map(lambda line: Scratchcard(line).points, lines))
