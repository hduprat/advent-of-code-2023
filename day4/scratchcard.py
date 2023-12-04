import re


class Scratchcard:
    def __init__(self, line):
        match = re.match("Card\s+(\d+): ([\d\s]+) \| ([\d\s]+)", line)
        if match is None:
            raise Exception("The line does not correspond to a scratchcard.")
        self.id = match.group(1).strip()
        self.winning_numbers = set(map(int, re.split("\s+", match.group(2).strip())))
        self.numbers = set(map(int, re.split("\s+", match.group(3).strip())))

    @property
    def won_numbers(self) -> int:
        return len(self.numbers.intersection(self.winning_numbers))

    @property
    def points(self) -> int:
        if self.won_numbers == 0:
            return 0
        return 2 ** (self.won_numbers - 1)
