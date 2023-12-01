import unittest

from day1 import part1, part2


class Day1Tests(unittest.TestCase):
    """
    Day 1 tests
    """

    def test_part1_solved(self):
        """
        Solves the example case from part 1
        """
        list = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
        self.assertEqual(142, part1.solve(list))

    def test_part2_solved(self):
        """
        Solves the example case from part 2
        """
        list = [
            "two1nine",
            "eightwothree",
            "abcone2threexyz",
            "xtwone3four",
            "4nineeightseven2",
            "zoneight234",
            "7pqrstsixteen",
        ]
        self.assertEqual(281, part2.solve(list))
