"""
Digital Ready Summer 2024
Card Game Project

The rank class is an enumeration of the possible ranks of a card in a deck of cards. 
"""
from enum import Enum

class Rank(Enum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13