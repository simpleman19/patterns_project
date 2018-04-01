class Visualizer:
    """ Super class for all visualizers.
        Used to enforce Template Methods. """

    def configure(self):
        raise NotImplementedError

    def style_render(self):
        raise NotImplementedError
