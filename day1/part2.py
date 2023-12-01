import re

DIGIT_REGEX = "(?=(\d|one|two|three|four|five|six|seven|eight|nine))"
DIGIT_TO_INT = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def _find_first_digit(line):
    match = re.findall(DIGIT_REGEX, line)
    digit = match[0]
    return int(digit) if len(digit) == 1 else DIGIT_TO_INT[digit]


def _find_last_digit(line):
    match = re.findall(DIGIT_REGEX, line)
    digit = match[-1]
    return int(digit) if len(digit) == 1 else DIGIT_TO_INT[digit]


def solve(lines):
    numbers = [_find_last_digit(line) + 10 * _find_first_digit(line) for line in lines]
    return sum(numbers)
