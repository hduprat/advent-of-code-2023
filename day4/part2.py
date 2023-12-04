from .scratchcard import Scratchcard


def solve(lines):
    scratchcards = list(map(Scratchcard, lines))
    scratchcard_amounts = list(map(lambda _: 1, scratchcards))
    for i in range(0, len(scratchcard_amounts)):
        won_scratchcards = scratchcards[i].won_numbers
        for j in range(0, won_scratchcards):
            scratchcard_amounts[i + 1 + j] += scratchcard_amounts[i]

    return sum(scratchcard_amounts)
