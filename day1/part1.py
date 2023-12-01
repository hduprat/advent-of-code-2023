import re


def _find_first_digit(line):
    match = re.search("\d", line)
    return int(match.group(0))


def _find_last_digit(line):
    match = re.search("(\d)[^\d]*$", line)
    return int(match.group(1))


def solve(lines):
    numbers = [_find_last_digit(line) + 10 * _find_first_digit(line) for line in lines]
    return sum(numbers)
