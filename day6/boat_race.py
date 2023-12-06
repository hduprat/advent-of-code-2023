from math import sqrt, floor, ceil


class BoatRace:
    def __init__(self, time: int, distance: int) -> None:
        self.time = time
        self.distance = distance

    @property
    def victoryTimes(self) -> range:
        sqdelta = sqrt(self.time**2 - 4 * self.distance)
        start = floor((self.time - sqdelta) / 2) + 1
        stop = ceil((self.time + sqdelta) / 2)
        return range(start, stop)
