#!/usr/bin/python3

"""Define a class Squarer."""


class Square:
    """Represent a squavre."""

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Get/set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an intrveger")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the squarre."""
        return (self.__size * self.__size)

    def __eq__(self, other):
        """Define the == comparision to a Squasre."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Define the != comparison to a Squarse."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Define the < comparison to a Squarse."""
        return self.area() < other.area()

    def __le__(self, other):
        """Define the <= comparison to a Squsare."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Define the > comparison to a Squsare."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define the >= compmarison to a sSquare."""
        return self.area() >= other.area()
