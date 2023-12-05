import re
from .almanac import BaseAlmanac, MappingItem
from utils.range import cut


class RangeAlmanac(BaseAlmanac):
    def __init__(self, lines) -> None:
        self.seeds = list(
            map(
                lambda t: range(int(t[0]), int(t[0]) + int(t[1])),
                re.findall("(\d+) (\d+)", lines[0]),
            )
        )
        super().__init__(lines)

    def map_all_to(
        self, values: list[range], mapping_items: list[MappingItem]
    ) -> list[range]:
        results = set()
        rest = set(values)
        for mapping_item in mapping_items:
            outs = list()
            for value in rest:
                (intersection, out) = cut(value, mapping_item.source_range)
                if intersection:
                    results.add(
                        range(
                            intersection.start
                            - mapping_item.source
                            + mapping_item.destination,
                            intersection.stop
                            - mapping_item.source
                            + mapping_item.destination,
                        )
                    )
                if out:
                    outs.extend(out)
            rest = set(outs)
        return list(results.union(rest))


def solve(lines):
    locations = RangeAlmanac(lines).locations
    return min(map(lambda l: l.start, locations))
