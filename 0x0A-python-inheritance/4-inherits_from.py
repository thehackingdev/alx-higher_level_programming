#!/usr/bin/python3
"""4-inherits_from.py
"""


def inherits_from(obj, a_class):
    """Return whether objct inherits from a_class.
    obj: an object.
    a_class: a class.
    """
    return(issubclass(type(obj), a_class) and not (type(obj) is a_class))
