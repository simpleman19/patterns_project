class Visualizer:
    """ Super class for all visualizers.
        Used to enforce Template Methods. """

    STR_REPR = 'Visualizer'
    COMMAND = 'NotImplemented'

    def configure(self):
        raise NotImplementedError

    def style_render(self):
        raise NotImplementedError
