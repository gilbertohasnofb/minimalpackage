from .function1 import function1


class Class1():
    
    def __init__(self):
        self.some_attribute = 'some_attribute'

    def some_method(self):
        return function1() + ' called in some_method()'