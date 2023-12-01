import unittest

from day{{ cookiecutter.day }} import part1, part2


class Day{{ cookiecutter.day }}Tests(unittest.TestCase):
    """
    Day {{ cookiecutter.day }} tests
    """

    def test_part1_solved(self):
        """
        Solves the example case from part 1
        """
        list = []
        self.assertEqual(0, part1.solve(list))

    def test_part2_solved(self):
        """
        Solves the example case from part 2
        """
        list = []
        self.assertEqual(0, part2.solve(list))
