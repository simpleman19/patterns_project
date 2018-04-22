import matplotlib.pyplot as plt
from visualizer import Visualizer


class FunctionVisualizer(Visualizer):
    """ Graphs a simple mathematical function """

    STR_REPR = 'function'

    def __init__(self):
        # default graph is square function
        self.power = 2
        self.x_values = list(range(-100, 100))
        self.y_values = [x**2 for x in self.x_values]

    def configure(self, power=None):
        if power is not None:
            self.power = int(power)
            self.y_values = [x ** self.power for x in self.x_values]
        plt.scatter(self.x_values, self.y_values, c=self.y_values, cmap=plt.cm.Blues, edgecolor='none', s=40)

    def style_render(self):
        plt.title('Function Visualizer', fontsize=24)
        plt.xlabel("Value", fontsize=14)
        plt.ylabel("Value^{}".format(self.power), fontsize=14)
        plt.tick_params(axis='both', which='major', labelsize=14)
        plt.show()


if __name__ == "__main__":
    """ TDD: Test Code """
    fv = FunctionVisualizer()
    fv.configure()
    fv.style_render()
