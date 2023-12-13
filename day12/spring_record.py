import re
from functools import cmp_to_key, cache

dot_regex = re.compile("\\.+")


class SpringRecord:
    def __init__(self, line: str) -> None:
        [self.string, check] = line.split(" ")
        self.damaged_ranges = tuple([int(range) for range in check.split(",")])
        self.regexes = dict[int, re.Pattern]()
        for range_value in set(self.damaged_ranges):
            self.regexes[range_value] = re.compile(
                f"(?<!#)[#?]{{{range_value}}}(([?.]|\\Z))"
            )

    @cache
    def count_arrangements(
        self, origin_str: str, damaged_ranges: tuple[int], debug: bool = False
    ) -> int:
        print(f"{origin=}, {damaged_ranges=}") if debug else None
        origin = ".".join(filter(lambda e: len(e) > 0, dot_regex.split(origin_str)))

        # if there are less characters than the sum of damaged ranges, there can never be an arrangement.
        if len(origin) < sum(damaged_ranges) + len(damaged_ranges) - 1:
            return 0

        # if there is no damage range available and no "#" is available, it is an arrangement but all "?" are "."
        if len(damaged_ranges) == 0:
            return 1 if origin.count("#") == 0 else 0

        # We take the first range
        range_size = damaged_ranges[0]

        regex = self.regexes[range_size]
        # We are looking for a potential range of "#", followed either by a "." or the end of string
        match = regex.search(origin)

        # No match? Never an arrangement.
        if match is None:
            return 0

        # Match ? It can be an arrangement.
        start, end = match.span(0)

        # If "#" have been neglected before finding the pattern, it is not an arrangement.
        if origin[0:start].count("#") > 0:
            return 0

        damaged_springs = match.group(0)

        # We check all the possible sub-arrangements
        arrangements = self.count_arrangements(origin[end:], damaged_ranges[1:], debug)

        # But let's not forget other possibilities and try the case when the match starts with "?" and can be a "."
        alternative_arrangements = (
            self.count_arrangements(origin[start + 1 :], damaged_ranges, debug)
            if damaged_springs[0] == "?"
            else 0
        )

        return arrangements + alternative_arrangements

    @property
    def arrangements(self):
        return self.count_arrangements(self.string, self.damaged_ranges)


def compare_records(a: SpringRecord, b: SpringRecord) -> int:
    if a.string.count("#") > b.string.count("#"):
        return -1
    if len(a.damaged_ranges) < len(b.damaged_ranges):
        return -1
    return a.string.count("?") - b.string.count("?")


class SpringRecords:
    def __init__(self, lines: list[str]) -> None:
        self.records = sorted(
            [SpringRecord(line) for line in lines], key=cmp_to_key(compare_records)
        )
