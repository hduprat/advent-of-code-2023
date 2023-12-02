from .game import Game


def solve(lines):
    total = 0
    for game in map(Game, lines):
        if game.is_possible():
            total += game.id
    return total
