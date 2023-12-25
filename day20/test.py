import unittest

from day20 import part1, part2

example = [
    "broadcaster -> a, b, c",
    "%a -> b",
    "%b -> c",
    "%c -> inv",
    "&inv -> a",
]

more_interesting_example = [
    "broadcaster -> a",
    "%a -> inv, con",
    "&inv -> b",
    "%b -> con",
    "&con -> output",
]


class Day20Tests(unittest.TestCase):
    """
    Day 20 tests
    """

    def test_part1_solved(self):
        """
        Solves the example case from part 1
        """
        self.assertEqual(32000000, part1.solve(example))
        self.assertEqual(11687500, part1.solve(more_interesting_example))
