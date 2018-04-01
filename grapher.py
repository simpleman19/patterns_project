from world import WorldVisualizer
from die_visualizer import DiceVisualizer
from tkinter import *


class App:
    """ Custom GUI class for creating graphs """

    def __init__(self, master):
        """ Should have a GUI element for each graph """

        frame = Frame(master)
        frame.pack()
        # when specifying a command, do not specify arguments. Just give it the name.
        # otherwise it will call the function on when declared. Not as an event.
        #
        # add new GUI items here:
        # World Population
        world_b = Button(frame, text='World', command=graph_world)
        world_b.grid(row=2, columnspan=2)
        # Dice Frequency
        dice_b = Button(frame, text='Dice', command=graph_dice)
        dice_b.grid(row=1, columnspan=2)
        # Random Walk


def graph_world():
    """ Class method: Creates a world population graph """
    # configure then style_render is the order needed per template
    wv = WorldVisualizer()
    wv.configure()
    wv.style_render()
    print("World Population graph from 2010 created.")


def graph_dice():
    """ Class method: Creates a dice frequency histogram """
    dv = DiceVisualizer()
    dv.configure()
    dv.style_render()
    print("Dice Frequency graph created")


root = Tk()
root.wm_title('Speed Grapher')
app = App(root)
root.mainloop()
