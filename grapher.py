from visualizer import Visualizer
from world import WorldVisualizer
from die_visualizer import DiceVisualizer
from walker_visualizer import WalkerVisualizer
from temperature_visualizer import TemperatureVisualizer
from api_visualizer import APIVisualizer
from function_visualizer import FunctionVisualizer
from tkinter import *


class App:
    """ Custom GUI class for creating graphs
        Provides an example of Event-Driven programming
        Enhancements: Make the GUI prettier
                      Make graphs more flexible via the inclusion of GUI-specifiable parameters
                      Add additional Behavioral Design Patterns """

    # using the visualizer at the class level establishes the Template Method AND Observer patterns.
    # the visualizer can also be considered a Null Object because it throws errors if it is used
    # directly. This is because it must have something to visualize!
    v = Visualizer()
    # using these redo buttons allows the previous graph to be reprinted. This is the Memento pattern
    dice_redo_b = None
    walker_redo_b = None

    col_span = 4

    gui_items = {}

    def __init__(self, master):
        """ Should have at least one GUI element for each graph.
            Class level components are only used if the component is needed in two commands. """

        frame = Frame(master, width=1000, height=1000)
        frame.pack()

        self.command = StringVar()

        row = 0
        # when specifying a command, do not specify arguments. Just give it the name.
        # otherwise it will call the function on when declared. Not as an event.
        #
        # add new GUI items here:

        # Dice Frequency. Note a callback function enables the redo_b, so it is class scoped.
        self.dice_b = Button(frame, text='Dice', command=graph_dice)
        self.dice_b.grid(row=row, column=0, columnspan=2)
        App.dice_redo_b = Button(frame, text='Dice Redo', command=regraph_dice, state=DISABLED)
        App.dice_redo_b.grid(row=row, column=2, columnspan=2)
        row += 1

        # Random Walk
        self.walker_b = Button(frame, text='Random Walk', command=graph_walk)
        self.walker_b.grid(row=row, column=0, columnspan=2)
        App.walker_redo_b = Button(frame, text='Walk Redo', command=regraph_walk, state=DISABLED)
        App.walker_redo_b.grid(row=row, column=2, columnspan=2)
        row += 1

        # Command Input
        self.command_input = Entry(frame, text="Command:", textvariable=self.command)
        self.command_input.grid(row=row, column=0, columnspan=4)
        self.run_command_b = Button(frame, text="Run Command", command=(lambda e=self.command_input: self.run_command(e.get())))
        self.run_command_b.grid(row=row, column=4, columnspan=2)
        row += 1

        # World Population
        self.gui_items[WorldVisualizer.STR_REPR] = build_gui_item(frame, WorldVisualizer, self.set_command)

        # High - Low Temperature (Death Valley)
        self.gui_items[TemperatureVisualizer.STR_REPR] = build_gui_item(frame, TemperatureVisualizer, self.set_command)

        # GitHub Most Popular Python Projects (API Scrape)
        self.gui_items[APIVisualizer.STR_REPR] = build_gui_item(frame, APIVisualizer, self.set_command)

        # Simple Scatter Plot
        self.gui_items[FunctionVisualizer.STR_REPR] = build_gui_item(frame, FunctionVisualizer, self.set_command)

        # Setup grid
        for x in self.gui_items.keys():
            self.gui_items[x]['item'].grid(row=row, column=self.gui_items[x]['column'], columnspan=self.col_span)
            row += 1

    # Interpreter
    def run_command(self, command):
        arguments = {}
        vis = command.split(',', 1)
        items = vis[1].split(',', 1)
        for i in items:
            x = i.split(':')
            arguments[x[0].strip()] = x[1].strip()
        gui_item = self.gui_items[vis[0].split(':')[1].strip()]
        App.v = gui_item['class']()
        App.v.configure(**arguments)
        App.v.style_render()
        print("Ran command: " + command)

    def set_command(self, repr):
        self.command.set(self.gui_items[repr]['command'])


# Factory
def build_gui_item(frame, item_class, set_command_ptr):
    return {'class': item_class,
            'column': 0,
            'command': item_class.COMMAND,
            'item': Button(frame, text='Load {} Command'.format(item_class.STR_REPR),
                           command=(lambda e=item_class.STR_REPR: set_command_ptr(e)))
            }


def graph_dice():
    """ Class method: Creates a dice frequency histogram """
    App.d = DiceVisualizer()
    App.d.configure()
    # The regraph button should only be enabled after an initial graphing (i.e. memento is populated)
    App.dice_redo_b.configure(state=NORMAL)
    App.d.style_render()
    print("Dice Frequency graph created.")


def regraph_dice():
    """ Class method: Recreates the last drawn dice frequency histogram """
    App.d = DiceVisualizer()
    App.d.reprint()
    print("Previous Dice Frequency graph restored.")


def graph_walk():
    """ Class method: Creates a random walk """
    App.w = WalkerVisualizer()
    App.w.configure()
    App.walker_redo_b.configure(state=NORMAL)
    App.w.style_render()
    print("Random Walk created.")


def regraph_walk():
    """ Class method: Recreates the last random walk """
    App.w = WalkerVisualizer()
    App.w.reprint()
    print("Previous Random Walk graph restored.")

root = Tk()
root.wm_title('Speed Grapher')
app = App(root)
root.mainloop()
