import re
from .almanac import BaseAlmanac


class Almanac(BaseAlmanac):
    def __init__(self, lines) -> None:
        self.seeds = list(
            map(int, re.match("seeds: ([\d ]+)", lines[0]).group(1).split(" "))
        )
        super().__init__(lines)


def solve(lines):
    locations = Almanac(lines).locations
    return min(locations)
