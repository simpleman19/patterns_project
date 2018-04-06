from world import WorldVisualizer
from die_visualizer import DiceVisualizer
from walker_visualizer import WalkerVisualizer
from temperature_visualizer import TemperatureVisualizer
from api_visualizer import APIVisualizer
from function_visualizer import FunctionVisualizer
from tkinter import *


class App:
    """ Custom GUI class for creating graphs
        Provides an example of event-driven programming
        Enhancements: Use the Mementos in Dice and Walkers (specify parameters for Dice and Walker Visualizers)
                      Make the GUI prettier (add parameters for Dice and Walkers. Maybe filepickers for input)
                      Add additional Behavioral Design Patterns """

    dice_redo_b = None
    walker_redo_b = None

    def __init__(self, master):
        """ Should have a GUI element for each graph """

        frame = Frame(master)
        frame.pack()
        # when specifying a command, do not specify arguments. Just give it the name.
        # otherwise it will call the function on when declared. Not as an event.
        #
        # add new GUI items here:
        # World Population
        self.world_b = Button(frame, text='World', command=graph_world)
        self.world_b.grid(row=1, column=0, columnspan=2)
        # Dice Frequency. Note a callback function enables the redo_b, so it is class scoped.
        self.dice_b = Button(frame, text='Dice', command=graph_dice)
        self.dice_b.grid(row=2, column=0, columnspan=2)
        App.dice_redo_b = Button(frame, text='Dice Redo', command=regraph_dice, state=DISABLED)
        App.dice_redo_b.grid(row=2, column=2, columnspan=2)
        # Random Walk
        self.walker_b = Button(frame, text='Random Walk', command=graph_walk)
        self.walker_b.grid(row=3, column=0, columnspan=2)
        App.walker_redo_b = Button(frame, text='Walk Redo', command=regraph_walk, state=DISABLED)
        App.walker_redo_b.grid(row=3, column=2, columnspan=2)
        # High - Low Temperature (Death Valley)
        self.temp_b = Button(frame, text='Temp H/L', command=graph_temp)
        self.temp_b.grid(row=4, column=0, columnspan=2)
        # GitHub Most Popular Python Projects (API Scrape)
        self.api_b = Button(frame, text='Github API', command=graph_api_scrape)
        self.api_b.grid(row=5, column=0, columnspan=2)
        # Simple Scatter Plot
        self.func_b = Button(frame, text='Function', command=graph_function)
        self.func_b.grid(row=6, column=0, columnspan=2)


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
    print("Dice Frequency graph created.")
    # The regraph button should only be enabled after an initial graphing (i.e. memento is populated)
    App.dice_redo_b.configure(state=NORMAL)


def regraph_dice():
    """ Class method: Recreates the last drawn dice frequency histogram """
    dv = DiceVisualizer()
    dv.reprint()
    print("Previous Dice Frequency graph restored.")


def graph_walk():
    """ Class method: Creates a random walk """
    wv = WalkerVisualizer()
    wv.configure()
    wv.style_render()
    print("Random Walk created.")
    App.walker_redo_b.configure(state=NORMAL)


def regraph_walk():
    """ Class method: Recreates the last random walk """
    wv = WalkerVisualizer()
    wv.reprint()
    print("Previous Random Walk graph restored.")


def graph_temp():
    """ Class method: Creates a temperature graph with highs and lows """
    tv = TemperatureVisualizer()
    tv.configure()
    tv.style_render()
    print("Temperature graph created.")


def graph_api_scrape():
    """ Class method: Creates a histogram detailing the most popular Python projects on Github
        Demonstrates observer pattern as the API values change regularly """
    av = APIVisualizer()
    av.configure()
    av.style_render()
    print("GitHub API graph created.")


def graph_function():
    """ Class method: Creates a graph of a simple function"""
    fv = FunctionVisualizer()
    fv.configure()
    fv.style_render()
    print("Function graph created.")


root = Tk()
root.wm_title('Speed Grapher')
app = App(root)
root.mainloop()
