from .energizer import Energizer
from .light import Light


def solve(lines):
    energizer = Energizer(lines)
    max = 0

    for y, _ in enumerate(lines):
        beam = Light((-1, y), (1, 0))
        tiles_energized = len(energizer.fire_beam(beam))
        max = tiles_energized if tiles_energized > max else max

        beam = Light((len(lines[0]), y), (-1, 0))
        tiles_energized = len(energizer.fire_beam(beam))
        max = tiles_energized if tiles_energized > max else max

    for x, _ in enumerate(lines[0]):
        beam = Light((x, -1), (0, 1))
        tiles_energized = len(energizer.fire_beam(beam))
        max = tiles_energized if tiles_energized > max else max

        beam = Light((x, len(lines)), (0, -1))
        tiles_energized = len(energizer.fire_beam(beam))
        max = tiles_energized if tiles_energized > max else max

    return max
