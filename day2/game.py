import re


class Game:
    def __init__(self, line):
        match = re.match("Game (\d+): (.+)", line)
        self.id = int(match.group(1))
        game_line = match.group(2)
        dice_lines = game_line.split("; ")
        self.dicesets = list(map(DiceSet, dice_lines))

    def is_possible(self):
        for ds in self.dicesets:
            if ds.is_possible() != True:
                return False
        return True

    def min_power(self) -> int:
        min_red = min_green = min_blue = None
        for ds in self.dicesets:
            if min_red is None or min_red < ds.red:
                min_red = ds.red
            if min_green is None or min_green < ds.green:
                min_green = ds.green
            if min_blue is None or min_blue < ds.blue:
                min_blue = ds.blue

        return min_red * min_blue * min_green


class DiceSet:
    def __init__(self, line):
        red_match = re.search("(\d+) red", line)
        green_match = re.search("(\d+) green", line)
        blue_match = re.search("(\d+) blue", line)
        self.red = int(red_match.group(1)) if red_match is not None else 0
        self.green = int(green_match.group(1)) if green_match is not None else 0
        self.blue = int(blue_match.group(1)) if blue_match is not None else 0

    def is_possible(self):
        if self.red > 12:
            return False
        if self.green > 13:
            return False
        if self.blue > 14:
            return False
        return True
