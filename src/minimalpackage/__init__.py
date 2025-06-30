"""minimalpackage docstring"""

from .module1.function1 import function1
from .module1.Class1 import Class1

from .module2.function2 import function2
from .module2.Class2 import Class2

from ._version import __version__


__all__ = [
    'function1',
    'function2',
    'Class1',
    'Class2',
]
