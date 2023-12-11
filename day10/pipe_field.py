from utils import tuple as tuples
from utils.point import Point


class PipeField:
    def __init__(self, lines: set[str]) -> None:
        self.connections = dict[Point, set[Point]]()
        for y, line in enumerate(lines):
            for x, pipe in enumerate(line):
                match pipe:
                    case "-":
                        self.connections[(x, y)] = set()
                        self.connections[(x, y)].add((x - 1, y))
                        self.connections[(x, y)].add((x + 1, y))
                    case "|":
                        self.connections[(x, y)] = set()
                        self.connections[(x, y)].add((x, y - 1))
                        self.connections[(x, y)].add((x, y + 1))
                    case "L":
                        self.connections[(x, y)] = set()
                        self.connections[(x, y)].add((x, y - 1))
                        self.connections[(x, y)].add((x + 1, y))
                    case "J":
                        self.connections[(x, y)] = set()
                        self.connections[(x, y)].add((x, y - 1))
                        self.connections[(x, y)].add((x - 1, y))
                    case "7":
                        self.connections[(x, y)] = set()
                        self.connections[(x, y)].add((x, y + 1))
                        self.connections[(x, y)].add((x - 1, y))
                    case "F":
                        self.connections[(x, y)] = set()
                        self.connections[(x, y)].add((x, y + 1))
                        self.connections[(x, y)].add((x + 1, y))
                    case "S":
                        self.connections[(x, y)] = set()
                        self.starting_point = (x, y)

    @property
    def loop(self) -> list[Point]:
        northwards = tuples.add(self.starting_point, (0, -1))
        eastwards = tuples.add(self.starting_point, (1, 0))
        southwards = tuples.add(self.starting_point, (0, 1))
        westwards = tuples.add(self.starting_point, (-1, 0))
        for point in [northwards, eastwards, southwards, westwards]:
            if (
                self.connections.get(point, None)
                and self.starting_point in self.connections[point]
            ):
                self.connections[self.starting_point].add(point)

        loop = [self.starting_point]
        while loop.count(self.starting_point) == 1:
            curr = loop[-1]
            prev = loop[-2] if len(loop) > 1 else None
            [enter, exit] = self.connections[curr]
            loop.append(enter if prev == exit else exit)
        return loop[:-1]

    @property
    def inner_area(self) -> set[Point]:
        inner_area = set()

        loop = self.loop
        outer_y = min(map(lambda p: p[1], loop))
        outer_x = min(map(lambda q: q[0], filter(lambda p: p[1] == outer_y, loop)))

        index = loop.index((outer_x, outer_y))
        outer_loop = loop[index + 1 :] + loop[:index]

        in_vector = (0, 1) if outer_loop[0][1] == outer_y else (1, 0)
        inner_point = tuples.add((outer_x, outer_y), in_vector)

        if inner_point not in loop:
            inner_area.add(inner_point)

        for x, y in outer_loop:
            inner_point = tuples.add((x, y), in_vector)
            if inner_point not in loop:
                inner_area.add(inner_point)

            prev, next = self.connections[(x, y)]
            vec = tuples.sub(next, prev)

            new_vector = tuples.add(in_vector, vec)
            if 0 in new_vector:
                in_vector = new_vector
                inner_point = tuples.add((x, y), in_vector)
                if inner_point not in loop:
                    inner_area.add(inner_point)
                continue

            new_vector = tuples.sub(in_vector, vec)
            if 0 in new_vector:
                in_vector = new_vector
                inner_point = tuples.add((x, y), in_vector)
                if inner_point not in loop:
                    inner_area.add(inner_point)
                continue

        return self.expand_area(inner_area)

    def expand_area(self, area: set[Point]) -> set[Point]:
        loop = self.loop
        new_area = area.copy()
        for x, y in area:
            if (x + 1, y) not in loop:
                new_area.add((x + 1, y))
            if (x - 1, y) not in loop:
                new_area.add((x - 1, y))
            if (x, y - 1) not in loop:
                new_area.add((x, y - 1))
            if (x, y + 1) not in loop:
                new_area.add((x, y + 1))
        return self.expand_area(new_area) if len(new_area) > len(area) else new_area
