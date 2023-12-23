from utils.list import split_list
from .rating import RatingSystem


def solve(lines):
    [workflows, _] = split_list(lines)
    rating_system = RatingSystem(workflows)
    return rating_system.count_accepted_repartitions()
