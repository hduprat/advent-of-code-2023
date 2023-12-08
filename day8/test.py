import unittest

from day8 import part1, part2


class Day8Tests(unittest.TestCase):
    """
    Day 8 tests
    """

    def test_part1_solved(self):
        """
        Solves the example case from part 1
        """
        simpleList = [
            "RL",
            "",
            "AAA = (BBB, CCC)",
            "BBB = (DDD, EEE)",
            "CCC = (ZZZ, GGG)",
            "DDD = (DDD, DDD)",
            "EEE = (EEE, EEE)",
            "GGG = (GGG, GGG)",
            "ZZZ = (ZZZ, ZZZ)",
        ]
        self.assertEqual(2, part1.solve(simpleList))

        complicatedList = [
            "LLR",
            "",
            "AAA = (BBB, BBB)",
            "BBB = (AAA, ZZZ)",
            "ZZZ = (ZZZ, ZZZ)",
        ]
        self.assertEqual(6, part1.solve(complicatedList))

    def test_part2_solved(self):
        """
        Solves the example case from part 2
        """
        list = [
            "LR",
            "",
            "11A = (11B, XXX)",
            "11B = (XXX, 11Z)",
            "11Z = (11B, XXX)",
            "22A = (22B, XXX)",
            "22B = (22C, 22C)",
            "22C = (22Z, 22Z)",
            "22Z = (22B, 22B)",
            "XXX = (XXX, XXX)",
        ]
        self.assertEqual(6, part2.solve(list))
