from Iterators.CustomIteratorInterface import CustomIteratorInterface
import json


class JsonIterator(CustomIteratorInterface):
    keys = None

    def set_values(self, values):
        if self.is_dict():
            self.keys = values.keys()
        self.values = values
        self.position = 0

    def next(self):
        if self.is_dict() and self.position < len(self.keys):
            self.position += 1
            return self.values[self.keys[self.position-1]]
        elif self.position < len(self.values):
            self.position += 1
            return self.values[self.position-1]
        else:
            return None

    def first(self):
        if self.is_dict():
            return self.values[self.keys[0]]
        elif self.values is not None:
            return self.values[0]
        else:
            return None

    def last(self):
        if self.is_dict():
            return self.values[self.keys[len(self.keys) - 1]]
        elif self.values is not None:
            return self.values[len(self.values) - 1]
        else:
            return None

    def has_next(self):
        if self.values is None:
            return False
        elif self.is_dict() and self.position < len(self.keys):
            return True
        elif self.position < len(self.values) and not self.is_dict():
            return True
        else:
            return False

    def is_dict(self):
        if isinstance(self.values, dict):
            return True
        elif isinstance(self.values, list) or self.values is None:
            return False
        else:
            raise ValueError()


class MyJson(object):
    json = None
    iterator = None

    def __init__(self, input_json):
        if isinstance(input_json, str):
            self.json = json.loads(input_json)
        elif isinstance(input_json, dict):
            self.json = input_json
        elif isinstance(input_json, list):
            self.json = input_json
        else:
            raise ValueError()

    def get_iterator(self):
        if self.iterator is None:
            self.iterator = JsonIterator()
            self.iterator.set_values(self.json)
        return self.iterator
