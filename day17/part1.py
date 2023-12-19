from utils.point import Point
from utils.tuple import add, sub


class Heatmap:
    least_loss: int | None = None
    path_of_least_loss: list[Point] = []
    MAX_STEPS = 3
    paths_tested = 0

    def __init__(self, lines) -> None:
        self.grid = [[int(char) for char in line] for line in lines]
        self.rows = len(lines)
        self.columns = len(lines[0])
        self.target = (self.rows - 1, self.columns - 1)

    def find_path_of_least_loss(
        self, path=[(0, 0)], direction=(1, 0), remaining_steps=MAX_STEPS, heat_loss=0
    ):
        self.paths_tested += 1
        point = path[-1]
        if point[0] not in range(0, self.columns):
            # print(f"Computing stopped because point is out of range: {point}")
            return
        if point[1] not in range(0, self.rows):
            # print(f"Computing stopped because point is out of range: {point}")
            return
        if remaining_steps <= 0:
            # print(
            #     f"Computing stopped because you cannot go further than 3 steps: {point}"
            # )
            return

        if self.least_loss is not None and heat_loss >= self.least_loss:
            # print(
            #     f"Computing stopped because heat loss is already over minimal heat loss: {heat_loss}"
            # )
            return

        if point == self.target:
            new_loss = heat_loss + self.grid[point[1]][point[0]]
            print(f"Target acquired!, {new_loss=}")
            if self.least_loss is None or new_loss < self.least_loss:
                self.least_loss = new_loss
                self.path_of_least_loss = path
                print(
                    f"New path with a minimum heat loss of {new_loss}: {self.path_of_least_loss}"
                )
            return

        for next_direction in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            next_point = add(point, next_direction)
            if next_point not in path:
                self.find_path_of_least_loss(
                    path + [next_point],
                    next_direction,
                    (remaining_steps - 1)
                    if direction is not None and direction == next_direction
                    else self.MAX_STEPS,
                    heat_loss + self.grid[point[1]][point[0]],
                )


def solve(lines):
    heatmap = Heatmap(lines)
    heatmap.find_path_of_least_loss()
    print(heatmap.path_of_least_loss)
    print(heatmap.least_loss)
    print(heatmap.paths_tested)
    return 0
