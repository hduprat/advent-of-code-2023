from utils.point import Point, scalar
from utils.tuple import add


class Light:
    tiles: set[Point] = set()
    split_by = set()  # set of splitters
    has_stopped = False

    def __init__(self, position: Point = (-1, 0), direction: Point = (1, 0)) -> None:
        self.position = position
        self.direction = direction
        self.tiles.add(self.position)

    def advance(self):
        self.position = add(self.position, self.direction)
        self.tiles.add(self.position)

    def stop(self):
        self.has_stopped = True


class LightModifier:
    def __init__(self, type) -> None:
        self.type = type

    def change_light(self, _: Light) -> Light | None:
        return None


class Mirror(LightModifier):
    def __init__(self, type: str) -> None:
        match type:
            case "/":
                self.multiplicator = -1
            case "\\":
                self.multiplicator = 1
            case _:
                raise Exception("Wrong mirror")
        super().__init__(type)

    def change_light(self, light: Light) -> Light | None:
        light.direction = (
            self.multiplicator * light.direction[1],
            self.multiplicator * light.direction[0],
        )


class AlreadySplitBySplitterException(Exception):
    pass


class Splitter(LightModifier):
    def __init__(self, type) -> None:
        match type:
            case "-":
                self.vector = (1, 0)
            case "|":
                self.vector = (0, 1)
            case _:
                raise Exception("Wrong splitter")
        super().__init__(type)

    def change_light(self, light: Light) -> Light | None:
        if scalar(light.direction, self.vector) != 0:
            return None

        if self in light.split_by:
            raise AlreadySplitBySplitterException
        light.split_by.add(self)
        light.direction = self.vector
        return Light(
            position=light.position, direction=(-self.vector[0], -self.vector[1])
        )
