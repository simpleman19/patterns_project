from die import Die
from dice_histogram_chart import DiceHistogram
from visualizer import Visualizer
from caretaker import Caretaker as ct


class DiceVisualizer(Visualizer):
    """ Visualizes a histogram of dice frequencies.
        At present: supports two 6 sided dice.
        Enhancement: add functionality for any number of dice with any number of sides. """

    c = ct()

    def __init__(self):
        self.die_1 = Die()
        self.die_2 = Die()
        self.results = []
        self.frequencies = []

    def configure(self):
        for roll_num in range(1000):
            result = self.die_1.roll() + self.die_2.roll()
            self.results.append(result)
        max_result = self.die_1.num_sides + self.die_2.num_sides
        for value in range(2, max_result + 1):
            frequency = self.results.count(value)
            self.frequencies.append(frequency)
        # setup caretaker with a dice memento
        DiceVisualizer.c.set_dice_memento(self.die_1, self.die_2, self.frequencies, self.results)

    def style_render(self):
        hist = DiceHistogram()
        hist.title = "Results of rolling two D6 1000 times"
        hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        hist.x_title = "Result"
        hist.y_title = "Frequency of Result"
        hist.add('D6 + D6', self.frequencies)
        hist.render('dice_visual.svg')

    def reprint(self):
        if DiceVisualizer.c.frequencies is not None:
            hist = DiceHistogram()
            hist.title = "Results of rolling two D6 1000 times"
            hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
            hist.x_title = "Result"
            hist.y_title = "Frequency of Result"
            hist.add('D6 + D6', DiceVisualizer.c.frequencies)
            hist.render('dice_visual.svg')
        else:
            print("cannot reprint a graph that hasn't been printed the first time!")


if __name__ == "__main__":
    """ Test code """
    dv = DiceVisualizer()
    dv.configure()
    dv.style_render()
    print("printed a graph via configure and style")
    dv.reprint()
    print("reprinted the graph via caretaker/memento")
