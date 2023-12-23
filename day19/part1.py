from utils.list import split_list
from .rating import PART_REGEX, RatingSystem


def solve(lines):
    [workflows, raw_parts] = split_list(lines)
    rating_system = RatingSystem(workflows)
    parts: list[dict[str, int]] = []
    for raw_part in raw_parts:
        part = dict()
        result = PART_REGEX.findall(raw_part)
        for var, val in result:
            part[var] = int(val)
        parts.append(part)

    total_rating = 0
    for part in parts:
        total_rating += sum(part.values()) if rating_system.check(part) == "A" else 0

    return total_rating
