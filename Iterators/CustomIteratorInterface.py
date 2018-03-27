class CustomIteratorInterface(object):
    values = None
    position = -1

    def set_values(self, values):
        raise NotImplementedError()

    def next(self):
        raise NotImplementedError()

    def first(self):
        raise NotImplementedError()

    def last(self):
        raise NotImplementedError()

    def has_next(self):
        raise NotImplementedError()

    def reset(self):
        self.position = 0
