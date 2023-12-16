from .dish import Dish, Direction


def solve(lines):
    dish = Dish(lines)
    dish.tilt(Direction.NORTH)
    return dish.load
