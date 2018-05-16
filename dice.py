import random

class Dice(object):

    def __init__(self, sides=6):  
        if not isinstance(sides, int):
            raise TypeError("Number of sides must be a int")
        elif sides < 2:
            raise ValueError("Number of sides must be >=2")
        self.sides = sides

    def roll(self):
        """Roll the dice and return the value."""
        return random.randint(1, self.sides)

    def rolln(self, n=1):
        """Roll n dice.

        Returned as a list.
        """
        return [random.randint(1, self.sides) for _ in range(n)]


