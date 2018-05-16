from deck import Card
from typing import Optional

class Player(object):
    """Player in the game."""
    def __init__(self, name: Optional[str] = None):
        """Start wth nothing."""
        if not isinstance(name, str) and name is not None:
            raise TypeError("Player name must be string")
        self.name = name
        self.score = 0  # Game Score  
        self.hand = []  # Cards in hand
        self.cubes = 0  # Inventory
        self.ability = None  # Special character 

    def add_score(self, points: int):
        if not isinstance(points, int):
            raise TypeError("Points must be int, not {0}".format(type(points)))
        elif points < 0:
            raise ValueError("Points must be positive")
        self.score += points

    def pickup_cubes(self, number: int):
        if not isinstance(number, int):
            raise TypeError("Number must be int, not {0}".format(type(number)))
        elif number < 0:
            raise ValueError("Number must be positive")
        self.cubes += number

    def pay_cubes(self, number):
        # TODO: Limit cubes to pay? 5-6?
        # TODO: Fail if payment greater then number of cubes you have?
        if not isinstance(number, int):
            raise TypeError("Number must be int, not {0}".format(type(number)))
        elif number < 0:
            raise ValueError("Number must be positive")
        elif number > self.cubes:
            raise PaymentError("You do not have enough cubes.")
        self.cubes -= number

    def reward(self, points, cubes):
        """Reward after defeating card."""
        self.add_score(points)
        self.pickup_cubes(cubes)

    def draw_card(self, card: Card):
        """Add card to hand.
        
        IDEA: Maybe pass this Deck and draw from the deck here?
        """
        self.hand.append(card)
    
    def play_card(self, index: int):
        """Play the card in index location."""
        assert index< len(self.hand), "Choose a card from the hand, len={}, index={}".format(len(self.hand), index)


class PaymentError(Exception):
    """Cannot pay for move."""
    pass
