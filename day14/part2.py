from .dish import Dish


def solve(lines):
    dish = Dish(lines)
    cache = []
    i = 0

    while str(dish) not in cache:
        cache.append(str(dish))
        dish.spin()
        i += 1
    cycle_length = i - cache.index(str(dish))

    i += cycle_length * ((1000000000 - i) // cycle_length)
    while i < 1000000000:
        dish.spin()
        i += 1

    return dish.load
