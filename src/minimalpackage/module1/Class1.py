from .function1 import function1


class Class1():
    """Class docstring"""
    
    def __init__(self):
        """Doctsring"""
        self.some_attribute = 'some_attribute'

    def some_method(self):
        """Doctsring"""
        return function1() + ' called in some_method()'
