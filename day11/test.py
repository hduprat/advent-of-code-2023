import unittest

from day11 import part1
from day11.telescope import TelescopeReport

list = [
    "...#......",
    ".......#..",
    "#.........",
    "..........",
    "......#...",
    ".#........",
    ".........#",
    "..........",
    ".......#..",
    "#...#.....",
]


class Day11Tests(unittest.TestCase):
    """
    Day 11 tests
    """

    def test_part1_solved(self):
        """
        Solves the example case from part 1
        """
        self.assertEqual(374, part1.solve(list))

    def test_part2_solved(self):
        """
        Solves the example case from part 2
        """
        older_report = TelescopeReport(list, spacing=10)
        self.assertEqual(1030, sum(older_report.distances_between_galaxies))

        oldest_report = TelescopeReport(list, spacing=100)
        self.assertEqual(8410, sum(oldest_report.distances_between_galaxies))
