from utils.point import Point, manhattan_distance


class TelescopeReport:
    def __init__(self, lines: list[str], spacing=2) -> None:
        self.galaxies: list[Point] = list()
        offset_y = 0
        for y, line in enumerate(lines):
            offset_y += (spacing - 1) if line.count("#") == 0 else 0
            offset_x = 0
            for x, char in enumerate(line):
                column = [line[x] for line in lines]
                offset_x += (spacing - 1) if column.count("#") == 0 else 0
                if char == "#":
                    self.galaxies.append((x + offset_x, y + offset_y))

    @property
    def distances_between_galaxies(self) -> list[int]:
        distances = list[int]()
        for i, a in enumerate(self.galaxies[0:-1]):
            for b in self.galaxies[i + 1 :]:
                distances.append(manhattan_distance(a, b))
        return distances
