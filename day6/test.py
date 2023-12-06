import unittest

from day6 import part1, part2

list = [
    "Time:      7  15   30",
    "Distance:  9  40  200",
]


class Day6Tests(unittest.TestCase):
    """
    Day 6 tests
    """

    def test_part1_solved(self):
        """
        Solves the example case from part 1
        """
        self.assertEqual(288, part1.solve(list))

    def test_part2_solved(self):
        """
        Solves the example case from part 2
        """
        self.assertEqual(71503, part2.solve(list))
