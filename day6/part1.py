import re
from math import prod

from .boat_race import BoatRace


class BoatRaceSession:
    races = list[BoatRace]()

    def __init__(self, lines) -> None:
        times = re.findall("\d+", lines[0])
        distances = re.findall("\d+", lines[1])
        if len(times) != len(distances):
            raise Exception("Times and distances should have the same length.")
        for i in range(0, len(times)):
            self.races.append(BoatRace(int(times[i]), int(distances[i])))

    @property
    def ways_to_beat_record(self) -> int:
        return prod(map(lambda r: len(r.victoryTimes), self.races))


def solve(lines):
    session = BoatRaceSession(lines)
    return session.ways_to_beat_record
