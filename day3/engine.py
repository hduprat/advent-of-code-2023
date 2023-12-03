import re


class Engine:
    def __init__(self, lines):
        self.part_numbers = list()
        self.star_symbols = dict()
        for i in range(0, len(lines)):
            line = lines[i].strip()
            for number in re.finditer("\d+", line):
                adjacent = range(
                    max(0, number.start() - 1), min(number.end() + 1, len(line))
                )
                symbol_match = re.search(
                    "[^.\d]", lines[i][adjacent.start : adjacent.stop]
                )
                if symbol_match:
                    self.part_numbers.append(int(number.group(0)))
                    self.update_star_symbols(
                        symbol_match.group(0),
                        symbol_match.start() + adjacent.start,
                        i,
                        int(number.group(0)),
                    )
                    continue
                symbol_match = (
                    re.search("[^.\d]", lines[i - 1][adjacent.start : adjacent.stop])
                    if i > 0
                    else None
                )
                if symbol_match:
                    self.part_numbers.append(int(number.group(0)))
                    self.update_star_symbols(
                        symbol_match.group(0),
                        symbol_match.start() + adjacent.start,
                        i - 1,
                        int(number.group(0)),
                    )
                    continue
                symbol_match = (
                    re.search("[^.\d]", lines[i + 1][adjacent.start : adjacent.stop])
                    if i < len(lines) - 1
                    else None
                )
                if symbol_match:
                    self.part_numbers.append(int(number.group(0)))
                    self.update_star_symbols(
                        symbol_match.group(0),
                        symbol_match.start() + adjacent.start,
                        i + 1,
                        int(number.group(0)),
                    )
                    continue

    def update_star_symbols(self, symbol, x, y, number):
        key = str(x) + "," + str(y)
        if symbol != "*":
            return
        if key in self.star_symbols:
            self.star_symbols[key].append(number)
        else:
            self.star_symbols[key] = [number]

    @property
    def gear_ratios(self):
        gear_ratios = list()
        for numbers in self.star_symbols.values():
            if len(numbers) == 2:
                gear_ratios.append(numbers[0] * numbers[1])
        return gear_ratios
