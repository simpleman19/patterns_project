from random import randint
import pickle


class Die:
    """ A class representing a die  """

    def __init__(self, num_sides=6):
        """ 6 sides by default  """
        self.num_sides = num_sides

    def roll(self):
        """ Return a random value between 1 and num_sides  """
        return randint(1, self.num_sides)

    def create_memento(self):
        return pickle.dumps(vars(self))

    def set_memento(self, memento):
        previous_state = pickle.loads(memento)
        vars(self).clear()
        vars(self).update(previous_state)
