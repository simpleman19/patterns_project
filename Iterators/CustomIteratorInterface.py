class CustomIteratorInterface(object):
    values = None
    position = -1

    def set_values(self, values):
        raise NotImplementedError()

    def next(self):
        raise NotImplementedError()

    def first(self):
        if self.values is not None:
            return self.values[0]
        else:
            return None

    def last(self):
        if self.values is not None:
            return self.values[len(self.values) - 1]
        else:
            return None

    def has_next(self):
        raise NotImplementedError()

    def reset(self):
        self.position = 0
