#!/usr/bin/env python
from enum import Enum, IntEnum
from collections import deque
import random


class CardSuit(Enum):
    """Suit Enum class for a playing card"""
    CLUBS = 1
    DIAMONDS = 2
    HEARTS = 3
    SPADES = 4


class CardValue(IntEnum):
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
        self.__value = value
        self.__suit = suit

    def __str__(self):
        """This method gets called when print() is called on a Card"""
        return "{} {}  ".format(self.__suit, self.__value)

    def getValue(self):
        return self.__value


class Deck:
    """Deck of Playing Cards class"""
    def __init__(self):
        """Initialize the Deck of Cards with all 52 cards"""
        self.__cards = []
        for suit in CardSuit:
            for value in CardValue:
                self.__cards.append(Card(suit, value))

    def print_cards(self):
        """Prints the cards in the deck"""
        for card in self.__cards:
            print(card, end=" ")
        print()

    def shuffleAndDivide(self):
        """Shuffles the cards in the deck and divides it into two parts"""
        random.shuffle(self.__cards)
        # Divide the cards in the deck into two parts
        first_part = []
        second_part = []
        while self.__cards:
            first_part.append(self.__cards.pop(0))
            second_part.append(self.__cards.pop(0))
        # first_part = self.__cards[::2]
        # # Second part has all the odd indexed elements
        # second_part = self.__cards[1::2]
        return first_part, second_part


class NoCardsRemaining(Exception):
    """Raise this error when a player has no cards remaining"""
    pass


class Player:
    def __init__(self, cards):
        self.__cards = deque(cards)

    def number_of_cards(self):
        return len(self.__cards)

    def add_cards(self, cards):
        """Adds the cards to this player's cards"""
        self.__cards.extend(cards)

    def draw_cards(self, count):
        """Draws number of cards specified by count"""
        if self.number_of_cards() < count:
            raise NoCardsRemaining
        return [self.__cards.popleft() for _ in range(count)]

    def show_all_cards(self):
        """Shows all the cards that the player has"""
        for card in self.__cards:
            print(card, end=" ")
        print()
        return


class WarGame:
    """War Game Class"""
    WAR_NUMBER_OF_CARDS = 3
    MAIN_SEPARATOR = "====================================================="
    SUB_SEPARATOR = "-----------------------------------------------------"
    MAX_ROUNDS = 1000

    def __init__(self):
        print(self.MAIN_SEPARATOR)
        print("WAR CARDS GAME")
        print(self.MAIN_SEPARATOR)
        # Initialize a deck of Cards
        self.__deck = Deck()

        # Shuffle the deck and divide it into two parts
        player1_cards, player2_cards = self.__deck.shuffleAndDivide()

        # Create two players with the two parts created
        self.__player1 = Player(player1_cards)
        self.__player2 = Player(player2_cards)

        # Whether war is on
        self.__war = False

        # Stores the cards on the table
        self.__table = []

        # Variable to store the number of rounds
        self.__rounds = 0

    def play(self):
        """This is each round of the Game"""

        # Increase the number of rounds by 1
        self.__rounds += 1

        if self.__rounds > self.MAX_ROUNDS:
            raise SystemExit("Number of rounds exceeded maximum - {}. GAME ENDS IN A DRAW".
                             format(self.MAX_ROUNDS))

        # If number of rounds is greater than MAX_ROUNDS
        print(self.MAIN_SEPARATOR)
        if not self.__player1.number_of_cards():
            print("PLAYER 2 WINS THE GAME")
            exit(0)
        elif not self.__player2.number_of_cards():
            print("PLAYER 1 WINS THE GAME")
            exit(0)

        # If war is ON, draw WAR_NUMBER_OF_CARDS cards from each player
        if self.__war:
            try:
                player1_cards = self.__player1.draw_cards(self.WAR_NUMBER_OF_CARDS)
                self.__table.extend(player1_cards)
            except NoCardsRemaining:
                print("Player 1 has no cards left.\nPLAYER 2 WINS THE GAME")
                exit(0)

            try:
                player2_cards = self.__player2.draw_cards(self.WAR_NUMBER_OF_CARDS)
                self.__table.extend(player2_cards)
            except NoCardsRemaining:
                print("Player 2 has no cards left.\nPLAYER 1 WINS THE GAME")
                exit(0)
            self.__print_table_cards()

        # Get the next card from each player
        player1_card = None
        player2_card = None
        try:
            player1_card = self.__player1.draw_cards(1)[0]
            print("Player 1: {}".format(player1_card))
        except NoCardsRemaining:
            print("Player 1 has no cards left.\nPLAYER 2 WINS THE GAME")
            exit(0)

        try:
            player2_card = self.__player2.draw_cards(1)[0]
            print("Player 2: {}".format(player2_card))
        except NoCardsRemaining:
            print("Player 2 has no cards left.\nPLAYER 1 WINS THE GAME")
            exit(0)

        if player1_card.getValue() == player2_card.getValue():
            # If both the cards have equal value, then add both cards to the table and declare war
            self.__table.append(player1_card)
            self.__table.append(player2_card)
            self.__war = True
            print("WARRRRRRRRRRRRRR")
        elif player1_card.getValue() > player2_card.getValue():
            # Player 1 keeps all the cards since Player 1 card's value is greater than that of Player 2
            self.__player1.add_cards([player1_card, player2_card])
            self.__player1.add_cards(self.__table)
            self.__table = []
            self.__war = False
            print("Player 1 Wins this round")
        else:
            self.__player2.add_cards([player1_card, player2_card])
            self.__player2.add_cards(self.__table)
            self.__table = []
            self.__war = False
            print("Player 2 Wins this round")

        self.__print_players_cards()
        print(self.MAIN_SEPARATOR)

    def __print_players_cards(self):
        """Print the cards of both the players"""
        print(self.SUB_SEPARATOR)
        print("Player 1 cards: ", end=" ")
        self.__player1.show_all_cards()
        print("Player 2 cards: ", end=" ")
        self.__player2.show_all_cards()
        print(self.SUB_SEPARATOR)

    def __print_table_cards(self):
        """Prints the card on the table"""
        print("Cards on table: ", end=" ")
        for card in self.__table:
            print(card, end=" ")
        print()












