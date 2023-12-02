import unittest

from day2 import part1, part2

list = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
]


class Day2Tests(unittest.TestCase):
    """
    Day 2 tests
    """

    def test_part1_solved(self):
        """
        Solves the example case from part 1
        """
        self.assertEqual(8, part1.solve(list))

    def test_part2_solved(self):
        """
        Solves the example case from part 2
        """
        self.assertEqual(2286, part2.solve(list))
