"""
minimalpackage
==============

docstring
"""

__all__ = [
    "module1",
    "module2",
    "__version__",
]

from . import module1, module2
from ._version import __version__
