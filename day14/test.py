import unittest

from day14 import part1, part2

list = [
    "O....#....",
    "O.OO#....#",
    ".....##...",
    "OO.#O....O",
    ".O.....O#.",
    "O.#..O.#.#",
    "..O..#O..O",
    ".......O..",
    "#....###..",
    "#OO..#....",
]


class Day14Tests(unittest.TestCase):
    """
    Day 14 tests
    """

    def test_part1_solved(self):
        """
        Solves the example case from part 1
        """
        self.assertEqual(136, part1.solve(list))

    def test_part2_solved(self):
        """
        Solves the example case from part 2
        """
        self.assertEqual(64, part2.solve(list))
