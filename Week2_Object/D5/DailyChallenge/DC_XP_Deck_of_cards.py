import random

# Define the Card class
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"

# Define the Deck class
class Deck:
    def __init__(self):
        self.cards = []
        self._build_deck()

    def _build_deck(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = [Card(suit, value) for suit in suits for value in values]

    def shuffle(self):
        if len(self.cards) != 52:
            self._build_deck()
        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) == 0:
            raise ValueError("All cards have been dealt")
        return self.cards.pop()

# Example usage
deck = Deck()
deck.shuffle()
print(deck.deal())  # Deals a single card
print(len(deck.cards))  # Shows the remaining number of cards in the deck
