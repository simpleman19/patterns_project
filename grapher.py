from world import WorldVisualizer
from die_visualizer import DiceVisualizer
from api_visualizer import APIVisualizer
from tkinter import *


class App:
    """ Custom GUI class for creating graphs
        Provides an example of event-driven programming
        Enhancements: Use the Mementos in Dice and Walkers (specify parameters for Dice and Walker Visualizers)
                      Make the GUI prettier (add parameters for Dice and Walkers. Maybe filepickers for input)
                      Add additional Behavioral Design Patterns """

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
        # High - Low Temperature (Death Valley)
        # GitHub Most Popular Python Projects (API Scrape)
        api_b = Button(frame, text='Github API', command=graph_api_scrape)
        api_b.grid(row=3, columnspan=2)
        # Simple Scatter Plot


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


def graph_api_scrape():
    """ Class method: Creates a histogram detailing the most popular Python projects on Github """
    av = APIVisualizer()
    av.configure()
    av.style_render()
    print("GitHub API graph created.")


root = Tk()
root.wm_title('Speed Grapher')
app = App(root)
root.mainloop()
