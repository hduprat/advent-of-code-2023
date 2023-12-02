from .game import Game


def solve(lines):
    total = 0
    for game in map(Game, lines):
        total += game.min_power()
    return total
