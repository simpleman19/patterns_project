import matplotlib.pyplot as plt
from walker import Walker
from visualizer import Visualizer
from caretaker import Caretaker as ct


class WalkerVisualizer(Visualizer):
    """ Visualizes a random walk of data. """

    STR_REPR = 'walker'

    c = ct()

    def __init__(self):
        self.w = Walker(50000)

    def configure(self):
        self.w.fill_walk()
        # setup walker memento
        WalkerVisualizer.c.set_walker_memento(self.w.num_points, self.w.x_values, self.w.y_values)

    def style_render(self):
        plt.figure(figsize=(10, 6))
        point_numbers = list(range(self.w.num_points))
        plt.scatter(self.w.x_values, self.w.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=1)
        plt.scatter(0, 0, c='green', edgecolors='none', s=100)
        plt.scatter(self.w.x_values[-1], self.w.y_values[-1], c='red', edgecolors='none', s=100)
        plt.axes().get_xaxis().set_visible(False)
        plt.axes().get_yaxis().set_visible(False)
        plt.show()

    def reprint(self):
        plt.figure(figsize=(10, 6))
        point_numbers = list(range(WalkerVisualizer.c.num_points))
        plt.scatter(WalkerVisualizer.c.x_values, WalkerVisualizer.c.y_values, c=point_numbers, cmap=plt.cm.Blues,
                    edgecolor='none', s=1)
        plt.scatter(0, 0, c='green', edgecolors='none', s=100)
        plt.scatter(WalkerVisualizer.c.x_values[-1], WalkerVisualizer.c.y_values[-1], c='red', edgecolors='none', s=100)
        plt.axes().get_xaxis().set_visible(False)
        plt.axes().get_yaxis().set_visible(False)
        plt.show()


if __name__ == "__main__":
    """ TDD: Test Code """
    wv = WalkerVisualizer()
    wv.configure()
    wv.style_render()
    print("printed a graph via configure and style")
    wv.reprint()
    print("reprinted the graph via caretaker/memento")