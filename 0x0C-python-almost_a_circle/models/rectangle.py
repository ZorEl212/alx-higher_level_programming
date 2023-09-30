#!/usr/bin/python3
"""Module for Rectangle class
    Inheriting from Base"""
from models.base import Base


class Rectangle(Base):
    """Class Rectange: Child class inheriting from base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Magic method to intialize a rectange
        Args:
            width: rectangle width
            height: rectangle height
            x: x value
            y: y value"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """gettr for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """settr for width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """gettr for height"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculate the area of the Rectangle."""
        return self.width * self.height

    def display(self):
        """Print the rectangle with '#'"""
        if self.width == 0 or self.height == 0:
            return ""
        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def __str__(self):
        return (f'[Rectangle] ({self.id}) {self.x}/{self.y} - '
                f'{self.width}/{self.height}')

    def update(self, *args, **kwargs):
        """Update the Rectangle."""
        arg_names = ["id", "width", "height", "x", "y"]

        if args:
            for i, arg in enumerate(args):
                if i < len(arg_names) and arg is not None:
                    setattr(self, arg_names[i], arg)
            return

        for k, v in kwargs.items():
            if k in arg_names and v is not None:
                setattr(self, k, v)

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
