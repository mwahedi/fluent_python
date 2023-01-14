import collections

"""
namedtuple constructs a simple class we call Card that represents individual
cards. namedtuple can be used to build classes of objects that are just bundles
of attributes with no custom methods
"""
Card = collections.namedtuple('Card', ['rank', 'suit'])


# FrenchDeck is an example of using dunder methods
class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self) -> None:
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


if __name__ == "__main__":
    beer_card = Card('7', 'diamonds')
    print(f"{beer_card} is an object from the Class Card.")

    deck = FrenchDeck()

    # native functions like len() and random.choice can be used
    print(f"The deck has {len(deck)} cards")
    print(f"deck[0] can be invoked and is the first card: {deck[0]}")
    print(f"deck[-1] can be invoked and is the last card: {deck[-1]}")

    from random import choice
    print(f"Let's pick a random card with choice: {choice(deck)}")
    print(f"Again: {choice(deck)}")
    print(f"Again: {choice(deck)}")

    # slicing is possible
    print(f"The first three cards are deck[:3] = {deck[:3]}")
    print(f"All Aces can be called via deck[12::13] = {deck[12::13]}")

    # iterating is possible because of __getitem__
    print("Let's iterate")
    for card in deck:  # doctest: +ELLIPSIS
        if card.suit == 'hearts':
            print(f"card is {card}")

    # We don't have the __contains__ method, thus we do a sequential scan.
    print(f"Card('Q', 'hearts') in deck: {Card('Q', 'hearts') in deck}")
    print(f"Card('7', 'beasts') in deck: {Card('7', 'beasts') in deck}")

    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

    def spades_high(card):
        rank_value = FrenchDeck.ranks.index(card.rank)
        return rank_value * len(suit_values) + suit_values[card.suit]

    print("let's sort")
    for card in sorted(deck, key=spades_high):
        if card.suit == 'hearts':
            print(card)
