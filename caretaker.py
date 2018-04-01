class Caretaker:
    """ This class holds values that need to be remembered.
        It accepts these values from either a memento object
        or an object that can create a memento directly.
        Access the Caretaker's values directly only after
        setting them with the proper set method. """

    def __init__(self):
        # dice data
        self.die_1 = None
        self.die_2 = None
        self.frequencies = []
        self.results = []

        # walker data
        self.num_points = None
        self.x_values = []
        self.y_values = []

    def set_dice_memento(self, die_1, die_2, frequencies, results):
        self.die_1 = die_1
        self.die_2 = die_2
        self.frequencies = frequencies
        self.results = results

    def set_walker_memento(self, num_points, x_values, y_values):
        self.num_points = num_points
        self.x_values = x_values
        self.y_values = y_values
