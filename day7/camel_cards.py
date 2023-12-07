from functools import cmp_to_key


class CamelCardsGame:
    cards = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]

    def __init__(self, lines: list[str]) -> None:
        self.hands: list[str] = list()
        self.bids: dict[str, int] = dict()
        for line in lines:
            [hand, bid] = line.split(" ")
            self.hands.append(hand)
            self.bids[hand] = int(bid)

    @classmethod
    def hand_type(cls, hand: str) -> int:
        composition = dict[str, int]()
        for card in hand:
            if card in composition:
                composition[card] += 1
            else:
                composition[card] = 1
        max_occurrences = max(composition.values())
        different_cards = len(composition.values())
        if max_occurrences == 1:
            return 0  # high card
        if max_occurrences == 2:
            if different_cards == 4:
                return 1  # one pair
            return 2  # two pairs
        if max_occurrences == 3:
            if different_cards == 3:
                return 3  # three of a kind
            return 4  # full house
        if max_occurrences == 4:
            return 5  # four of a kind
        return 6  # five of a kind

    @classmethod
    def compare_hands(cls, a: str, b: str) -> int:
        a_type = cls.hand_type(a)
        b_type = cls.hand_type(b)
        type_diff = a_type - b_type
        if type_diff != 0:
            return type_diff
        for i in range(0, 5):
            a_card_index = cls.cards.index(a[i])
            b_card_index = cls.cards.index(b[i])
            index_diff = b_card_index - a_card_index
            if index_diff != 0:
                return index_diff

    @property
    def winnings(self) -> list[str]:
        ranked_hands = sorted(self.hands, key=cmp_to_key(type(self).compare_hands))
        return [i * self.bids[hand] for i, hand in enumerate(ranked_hands, start=1)]


class JokerCamelCardsGame(CamelCardsGame):
    cards = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]

    @classmethod
    def hand_type(cls, hand: str) -> int:
        composition = dict[str, int]()
        jokers: int = 0
        for card in hand:
            if card == "J":
                jokers += 1
            else:
                if card in composition:
                    composition[card] += 1
                else:
                    composition[card] = 1
        max_occurrences = (
            max(composition.values()) if len(composition.values()) > 0 else 0
        ) + jokers
        different_cards = len(composition.values())
        if max_occurrences == 1:
            return 0  # high card
        if max_occurrences == 2:
            if different_cards == 4:
                return 1  # one pair
            return 2  # two pairs
        if max_occurrences == 3:
            if different_cards == 3:
                return 3  # three of a kind
            return 4  # full house
        if max_occurrences == 4:
            return 5  # four of a kind
        return 6  # five of a kind
