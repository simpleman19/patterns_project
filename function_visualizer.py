import matplotlib.pyplot as plt
from visualizer import Visualizer


class FunctionVisualizer(Visualizer):
    """ Graphs a simple mathematical function """

    def __init__(self):
        # default graph is square function
        self.x_values = list(range(1001))
        self.y_values = [x**2 for x in self.x_values]

    def configure(self):
        plt.scatter(self.x_values, self.y_values, c=self.y_values, cmap=plt.cm.Blues, edgecolor='none', s=40)

    def style_render(self):
        plt.title("Square Numbers", fontsize=24)
        plt.xlabel("Value", fontsize=14)
        plt.ylabel("Square of Value", fontsize=14)
        plt.tick_params(axis='both', which='major', labelsize=14)
        plt.show()


if __name__ == "__main__":
    """ TDD: Test Code """
    fv = FunctionVisualizer()
    fv.configure()
    fv.style_render()
