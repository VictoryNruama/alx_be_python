# polymorphism_demo.py

import math

class Shape:
    """Base class for geometric shapes."""

    def area(self):
        """Calculate the area of the shape. Must be overridden in subclasses."""
        raise NotImplementedError("Subclasses must implement the area method.")


class Rectangle(Shape):
    """Rectangle shape class, inherits from Shape."""

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Return the area of the rectangle."""
        return self.length * self.width


class Circle(Shape):
    """Circle shape class, inherits from Shape."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Return the area of the circle."""
        return math.pi * (self.radius ** 2)

