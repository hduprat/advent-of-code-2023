from utils.tuple import add
from utils.point import Point
from utils.list import pairs


class Trench:
    def __init__(self, lines: list[str]) -> None:
        self.edge = [(0, 0)]
        for line in lines:
            [direction, nstr, _] = line.strip().split(" ")
            n = int(nstr)
            match direction:
                case "U":
                    dig_vector = (0, -n)
                case "R":
                    dig_vector = (n, 0)
                case "D":
                    dig_vector = (0, n)
                case "L":
                    dig_vector = (-n, 0)
            (x, y) = add(self.edge[-1], dig_vector)
            self.edge += [(x, y)]

        self.setup_separators()
        self.setup_slices()

        self.min_row = min(self.slices.keys())
        self.max_row = max(self.slices.keys())
        xs = [x for xlist in self.slices.values() for x in xlist]
        self.min_col = min(xs)
        self.max_col = max(xs)

    def setup_separators(self):
        self.slices = dict[tuple[int, int], set[int]]()
        self.separators = dict[int, tuple[int, int]]()

        new_edge = []
        for i, (x0, y0) in enumerate(self.edge[:-1]):
            (x1, y1) = self.edge[i + 1]
            xmin = min(x0, x1)
            xmax = max(x0, x1)
            if y1 == y0:
                # horizontal case
                if y0 in self.separators:
                    self.separators[y0].append((xmin, xmax))
                else:
                    self.separators[y0] = [(xmin, xmax)]

        self.separators = dict(sorted(self.separators.items()))

        for i, (x0, y0) in enumerate(self.edge[:-1]):
            if (x0, y0) not in new_edge:
                new_edge.append((x0, y0))
            (x1, y1) = self.edge[i + 1]

            if x1 == x0:
                sign = (y1 - y0) // abs(y1 - y0)

                for y in self.separators:
                    if y in range(y0 + sign, y1, sign):
                        new_edge.append((x0, y))
                        self.separators[y].append((x0, x0))

        self.edge = new_edge

    def setup_slices(self):
        connections = dict[Point, list[Point]]()
        for i, (x, y) in enumerate(self.edge):
            connections[x, y] = [
                self.edge[i - 1],
                self.edge[(i + 1) % len(self.edge)],
            ]

        separator_keys = list(self.separators.keys())
        for j, y0 in enumerate(separator_keys[:-1]):
            upper_separator = list(filter(lambda p: p[1] == y0, self.edge))

            y1 = separator_keys[j + 1]
            self.slices[y0, y1] = set()
            for x, y in upper_separator:
                common_points = list(
                    filter(lambda p: p[0] == x and p[1] == y1, connections[x, y])
                )
                if len(common_points) > 0:
                    self.slices[y0, y1].add(common_points[0][0])

    @property
    def volume(self):
        output = 0

        print(f"{self.separators=}\n{self.slices=}")
        for y in self.separators:
            slice_width = 0
            for x_0, x_1 in self.separators[y]:
                slice_width += x_1 - x_0 + 1
            output += slice_width
        print(output)

        for p in self.slices:
            slice_width = 0
            for x_0, x_1 in pairs(sorted(self.slices[p])):
                slice_width += x_1 - x_0 + 1
            slice_height = p[1] - p[0] - 1
            output += slice_width * slice_height

        return output


def solve(lines):
    trench = Trench(lines)
    return trench.volume
