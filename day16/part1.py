from .energizer import Energizer
from .light import Light


def solve(lines):
    energizer = Energizer(lines)
    traversed_tiles = energizer.fire_beam(Light())
    return len(traversed_tiles)
