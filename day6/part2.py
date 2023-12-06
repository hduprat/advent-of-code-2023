import re

from .boat_race import BoatRace


def solve(lines):
    time = int("".join(re.findall("\d+", lines[0])))
    distance = int("".join(re.findall("\d+", lines[1])))

    return len(BoatRace(time, distance).victoryTimes)
