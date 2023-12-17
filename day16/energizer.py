from utils.point import Point
from .light import (
    Light,
    LightModifier,
    Mirror,
    Splitter,
    AlreadySplitBySplitterException,
)


class Energizer:
    def __init__(self, lines: list[str]) -> None:
        self.rows = len(lines)
        self.columns = len(lines[0].strip())
        self.beams: set[Light] = set()

        self.map = dict[Point, LightModifier]()
        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                match char:
                    case "/" | "\\":
                        self.map[(x, y)] = Mirror(char)
                    case "-" | "|":
                        self.map[(x, y)] = Splitter(char)
                    case _:
                        pass

    @property
    def are_beams_active(self):
        for beam in self.beams:
            if beam.has_stopped == False:
                return True

        return False

    def fire_beam(self, initial_beam: Light) -> set[Point]:
        Light.tiles.clear()
        Light.split_by.clear()

        self.beams.add(initial_beam)
        while self.are_beams_active:
            new_beams = set()
            for beam in self.beams:
                if beam.has_stopped:
                    continue
                beam.advance()
                (x, y) = beam.position
                if x not in range(0, self.columns) or y not in range(0, self.rows):
                    beam.stop()
                if (x, y) in self.map:
                    light_modifier = self.map[(x, y)]
                    try:
                        new_beam = (
                            light_modifier.change_light(beam)
                            if light_modifier
                            else None
                        )
                        if new_beam:
                            new_beams.add(new_beam)
                    except AlreadySplitBySplitterException:
                        beam.stop()

            self.beams = self.beams.union(new_beams)

        tiles = set(
            filter(
                lambda t: t[0] in range(0, self.columns)
                and t[1] in range(0, self.rows),
                Light.tiles,
            )
        )
        return tiles

    def __str__(self) -> str:
        string = ""
        for y in range(0, self.rows):
            for x in range(0, self.columns):
                if (x, y) in Light.tiles:
                    string += "#"
                elif (x, y) not in self.map:
                    string += "."
                else:
                    string += self.map[(x, y)].type
            string += "\n"
        return string
