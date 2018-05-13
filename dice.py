import random

class Dice(object):

    def __init__(self, sides=6):  
        if isinstance(sides, int):
            self.sides = sides
        else: 
            raise TypeError("Number of sides must be a int")

    def roll(self):
        """"""
        return random.randint(1, self.sides)

    def rolln(self, n=1):
        """Roll n dice.
        Returned as a list.
        """
        return [random.randint(1, self.sides) for _ in range(n)]


