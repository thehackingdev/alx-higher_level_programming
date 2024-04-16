#!/usr/bin/python3
""" Module that contains a function that writes to a text file
"""


def write_file(filename="", text=""):
    """  writes to a text file

    Args:
        filename: filename
        text: written text

    Raises
        Exception:  file can be opened

    """

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
