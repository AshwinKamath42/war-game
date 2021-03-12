#!/usr/bin/env python
from enum import Enum


class CardSuit(Enum):
    """Suit Enum class for a playing card"""
    CLUBS = 1
    DIAMONDS = 2
    HEARTS = 3
    SPADES = 4


class CardValue(Enum):
    """Value Enum class for a playing card"""
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    JACK = 10
    QUEEN = 11
    KING = 12
    ACE = 13


class Card:
    """Playing Card Class"""
    def __init__(self, suit, value):
        """Initializes a Playing card with """
        if not isinstance(suit, CardSuit) or not isinstance(value, CardValue):
            raise SystemExit("Error while instantiation a playing card. Suit or Value is invalid")
        self.value = value
        self.suit = suit

    def __str__(self):
        """This method gets called when print() is called on a Card"""
        return "Playing Card - Suit: {} Value: {}".format(self.suit, self.value)


class Deck:
    """Deck of Playing Cards class"""
    def __init__(self):
        """Initialize the Deck of Cards with all 52 cards"""
        self.cards = []
        for suit in CardSuit:
            for value in CardValue:
                self.cards.append(Card(suit, value))

    def print_cards(self):
        """Prints the cards in the deck"""
        for card in self.cards:
            print(card)



