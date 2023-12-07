from .camel_cards import JokerCamelCardsGame


def solve(lines):
    game = JokerCamelCardsGame(lines)
    return sum(game.winnings)
