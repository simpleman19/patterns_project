from world import WorldVisualizer
from tkinter import *


class App:
    """ Custom GUI class for creating graphs """

    def __init__(self, master):
        """ Should have a GUI element for each graph """

        frame = Frame(master)
        frame.pack()
        # when specifying a command, do not specify arguments. Just give it the name.
        # otherwise it will call the function on when declared. Not as an event.
        world_b = Button(frame, text='World', command=graph_world)
        world_b.grid(row=2, columnspan=2)


def graph_world():
    """ Class method: Creates a world population graph """

    wv = WorldVisualizer()
    wv.configure()
    wv.style_render()
    print("World Population graph from 2010 created.")


root = Tk()
root.wm_title('Speed Grapher')
app = App(root)
root.mainloop()
