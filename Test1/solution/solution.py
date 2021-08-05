from enum import Enum


class Suit(Enum):
    SPADES = 4
    HEARTS = 3
    DIAMONDS = 2
    CLUBS = 1


class PlayingCard:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit


class Player():

    def __init__(self, name):
        self.name = name
        self.hand = []


class Deck:
    def __init__(self):
        self.cards = []
        for i in range(13):
            self.cards.append(PlayingCard(i+2, Suit.SPADES))
            self.cards.append(PlayingCard(i+2, Suit.DIAMONDS))
            self.cards.append(PlayingCard(i+2, Suit.HEARTS))
            self.cards.append(PlayingCard(i+2, Suit.CLUBS))
