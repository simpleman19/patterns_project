from random import randint

class Die:
    """ A class representing a die  """

    def __init__(self, num_sides=6):
        """ 6 sides by default  """
        self.num_sides = num_sides

    def roll(self):
        """ Return a random value between 1 and num_sides  """
        return randint(1, self.num_sides)
