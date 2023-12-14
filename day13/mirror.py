from utils.list import split_list
from typing import Callable

type SymmetryFunction = Callable[[int, list[str]], bool]


def is_symmetry_axis(y: int, lines: list[str]) -> bool:
    for i in range(0, y + 1):
        if y + 1 + i == len(lines):
            return True
        if lines[y - i] != lines[y + 1 + i]:
            return False
    return True


class MirrorPattern:
    def __init__(
        self,
        lines: list[str],
        symmetry_func: SymmetryFunction,
    ) -> None:
        self.lines = lines
        self.symmetry_func = symmetry_func

    @property
    def horizontal_reflected_area(self) -> int | None:
        return self.find_horizontal_reflected_area(self.lines)

    @property
    def vertical_reflected_area(self) -> int | None:
        columns = [
            "".join([line[x] for line in self.lines])
            for x, _ in enumerate(self.lines[0])
        ]
        return self.find_horizontal_reflected_area(columns)

    @property
    def score(self) -> int:
        return (self.vertical_reflected_area or 0) + 100 * (
            self.horizontal_reflected_area or 0
        )

    def find_horizontal_reflected_area(self, lines: list[str]) -> int | None:
        for y, _ in enumerate(lines[:-1]):
            if self.symmetry_func(y, lines):
                return y + 1
        return None


class MirrorField:
    def __init__(
        self, lines: list[str], symmetry_func: SymmetryFunction = is_symmetry_axis
    ) -> None:
        self.patterns = [
            MirrorPattern(group, symmetry_func) for group in split_list(lines)
        ]

    @property
    def score(self) -> int:
        scores = [pattern.score for pattern in self.patterns]
        return sum(scores)
