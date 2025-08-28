from .function2 import function2


class Class2:
    """Class docstring"""

    def __init__(self):
        """Doctsring"""
        self.some_attribute = "some_attribute"

    def some_method(self):
        """Doctsring"""
        return function2() + " called in some_method()"
