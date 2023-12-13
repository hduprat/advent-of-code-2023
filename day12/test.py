import unittest

from day12 import part1, part2


list = [
    "???.### 1,1,3",
    ".??..??...?##. 1,1,3",
    "?#?#?#?#?#?#?#? 1,3,1,6",
    "????.#...#... 4,1,1",
    "????.######..#####. 1,6,5",
    "?###???????? 3,2,1",
]


class Day12Tests(unittest.TestCase):
    """
    Day 12 tests
    """

    def test_part1_solved(self):
        """
        Solves the example case from part 1
        """
        self.assertEqual(21, part1.solve(list))

    def test_part2_solved(self):
        """
        Solves the example case from part 2
        """
        self.assertEqual(525152, part2.solve(list))
