"""
Digital Ready Summer 2024
Card Game Project

The suit class is an enumeration of the possible suits of a card in a deck of cards.
"""
from enum import Enum

class Suit(Enum):
    HEARTS = '♥'
    DIAMONDS = '♦'
    CLUBS = '♣'
    SPADES = '♠'