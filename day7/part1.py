from .camel_cards import CamelCardsGame


def solve(lines):
    game = CamelCardsGame(lines)
    return sum(game.winnings)
