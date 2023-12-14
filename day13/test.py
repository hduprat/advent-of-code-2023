import unittest

from day13 import part1, part2

list = [
    "#.##..##.",
    "..#.##.#.",
    "##......#",
    "##......#",
    "..#.##.#.",
    "..##..##.",
    "#.#.##.#.",
    "",
    "#...##..#",
    "#....#..#",
    "..##..###",
    "#####.##.",
    "#####.##.",
    "..##..###",
    "#....#..#",
]


class Day13Tests(unittest.TestCase):
    """
    Day 13 tests
    """

    def test_part1_solved(self):
        """
        Solves the example case from part 1
        """
        self.assertEqual(405, part1.solve(list))

    def test_part2_solved(self):
        """
        Solves the example case from part 2
        """
        self.assertEqual(400, part2.solve(list))
