#!/usr/bin/python3
"""function Rectangle class."""
from models.base import Base


class Rectangle(Base):
    """class Rectangle inherits rom Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes Rectangle class."""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """set width of Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """set height of Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """set x for the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """set y for the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns area of Rectangle."""
        return self.__height * self.__width

    def display(self):
        """prints in stdout of Rectangle."""
        print("\n" * (self.__y), end="")
        for i in range(self.__height):
            print(" " * (self.__x) + "#" * self.__width)

    def __str__(self):
        """str() representation of the Rectangle."""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height))
