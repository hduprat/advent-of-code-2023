import re
from typing import Callable


class Network:
    directions = ["L", "R"]

    def __init__(self, lines) -> None:
        self.network = dict[str, tuple[str, str]]()
        self.i = 0
        for line in lines:
            match = re.fullmatch("(\w+) = \((\w+), (\w+)\)", line.strip())
            if match:
                self.network[match.group(1)] = [match.group(2), match.group(3)]

    def walk(self, current: str, direction: str) -> str:
        index = self.directions.index(direction)
        if index is None:
            raise Exception("Unknown instruction" + direction)
        return self.network[current][index]

    def walk_through(
        self,
        instructions,
        start_node="AAA",
        stop_condition: Callable[[str], bool] = lambda n: n == "ZZZ",
    ) -> [str]:
        path = [start_node]
        while stop_condition(path[-1]) == False:
            direction = instructions[self.i % len(instructions)]
            path.append(self.walk(path[-1], direction))
            self.i += 1
        return path

    @property
    def nodes(self) -> [str]:
        return list(self.network.keys())
