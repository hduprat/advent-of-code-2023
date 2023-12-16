from enum import Enum
from functools import cache


class Direction(Enum):
    NORTH = 1
    WEST = 2
    SOUTH = 3
    EAST = 4


def partition_rocks_blocks(rocks: list[int], blocks: list[int]) -> list[list[int]]:
    _blocks = blocks
    _rocks = sorted(rocks)
    output = [[]]

    for rock in _rocks:
        if len(_blocks) == 0:
            output[-1].append(rock)
        elif rock < _blocks[0]:
            output[-1].append(rock)
        else:
            while len(_blocks) > 0 and rock >= _blocks[0]:
                output.append([])
                _blocks = _blocks[1:]
            output[-1].append(rock)

    for _ in _blocks:
        output.append([])
    return output


class Dish:
    def __init__(self, lines: list[str]) -> None:
        self.lines = len(lines)
        self.columns = len(lines[0])

        self.x_blocks = dict[int, list[int]]()
        self.y_blocks = dict[int, list[int]]()
        self.x_rocks = dict[int, list[int]]()
        self.y_rocks = dict[int, list[int]]()

        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                match char:
                    case "#":
                        if y in self.x_blocks:
                            self.x_blocks[y].append(x)
                        else:
                            self.x_blocks[y] = [x]

                        if x in self.y_blocks:
                            self.y_blocks[x].append(y)
                        else:
                            self.y_blocks[x] = [y]
                    case "O":
                        if y in self.x_rocks:
                            self.x_rocks[y].append(x)
                        else:
                            self.x_rocks[y] = [x]

                        if x in self.y_rocks:
                            self.y_rocks[x].append(y)
                        else:
                            self.y_rocks[x] = [y]

    def tilt(self, dir: Direction) -> None:
        rocks = (
            self.x_rocks
            if dir == Direction.EAST or dir == Direction.WEST
            else self.y_rocks
        )

        blocks = (
            self.x_blocks
            if dir == Direction.EAST or dir == Direction.WEST
            else self.y_blocks
        )

        new_rocks = dict()

        for i in rocks:
            if i not in blocks:
                if dir == Direction.EAST or dir == Direction.SOUTH:
                    new_rocks[i] = [
                        (self.lines - 1 - r) for r in range(0, len(rocks[i]))
                    ]
                else:
                    new_rocks[i] = [r for r in range(0, len(rocks[i]))]

            else:
                new_rocks[i] = []
                rocks_before_blocks = partition_rocks_blocks(rocks[i], blocks[i])
                for j, rock_range in enumerate(rocks_before_blocks):
                    if dir == Direction.WEST or dir == Direction.NORTH:
                        new_rocks[i].extend(
                            [
                                blocks[i][j - 1] + 1 + r if j > 0 else r
                                for r, _ in enumerate(rock_range)
                            ]
                        )
                    else:
                        new_rocks[i].extend(
                            [
                                blocks[i][j] - 1 - r
                                if j < len(blocks[i])
                                else self.lines - 1 - r
                                for r, _ in enumerate(rock_range)
                            ]
                        )

        if dir == Direction.EAST or dir == Direction.WEST:
            self.x_rocks = new_rocks
            self.update_y_rocks()
        else:
            self.y_rocks = new_rocks
            self.update_x_rocks()

    def update_y_rocks(self):
        output = dict()
        for y in self.x_rocks:
            for x in self.x_rocks[y]:
                if x in output:
                    output[x].append(y)
                else:
                    output[x] = [y]

        self.y_rocks = output

    def update_x_rocks(self):
        output = dict()
        for x in self.y_rocks:
            for y in self.y_rocks[x]:
                if y in output:
                    output[y].append(x)
                else:
                    output[y] = [x]

        self.x_rocks = output

    def spin(self):
        self.tilt(Direction.NORTH)
        self.tilt(Direction.WEST)
        self.tilt(Direction.SOUTH)
        self.tilt(Direction.EAST)

    @property
    def load(self) -> int:
        return sum([len(rocks) * (self.lines - y) for y, rocks in self.x_rocks.items()])

    def __str__(self) -> str:
        output = list()
        for y in range(0, self.lines):
            line = ""
            for x in range(0, self.columns):
                if y in self.x_rocks and x in self.x_rocks[y]:
                    line += "O"
                elif y in self.x_blocks and x in self.x_blocks[y]:
                    line += "#"
                else:
                    line += "."
            output.append(line)
        output.append("")
        return "\n".join(output)
