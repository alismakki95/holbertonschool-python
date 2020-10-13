#!/usr/bin/python3
""" Rectangle class Module"""
from models.base import Base


class Rectangle(Base):
    """ Rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialize """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Getter width """
        return self.__width

    @width.setter
    def width(self, width):
        """ Setter width """
        self.validator_size(width, "width")
        self.__width = width

    @property
    def height(self):
        """ Getter height """
        return self.__height

    @height.setter
    def height(self, height):
        """ Setter height """
        self.validator_size(height, "height")
        self.__height = height

    @property
    def x(self):
        """ Getter x """
        return self.__x

    @x.setter
    def x(self, x):
        """ Setter x """
        self.validator_angle(x, "x")
        self.__x = x

    @property
    def y(self):
        """ Getter y """
        return self.__y

    @y.setter
    def y(self, y):
        """ Setter y """
        self.validator_angle(y, "y")
        self.__y = y

    def validator_size(self, value, property):
        """ Validator size of rectangle """
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(property))
        elif value <= 0:
            raise ValueError('{} must be > 0'.format(property))

    def validator_angle(self, value, property):
        """ Validator angle of rectangle """
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(property))
        elif value < 0:
            raise ValueError('{} must be >= 0'.format(property))

    def area(self):
        """ Area of rectangle """
        return self.__width * self.__height

    def display(self):
        """ Display """
        print("\n" * self.__y, end="")
        for x in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """ __str__ """
        return ("[{}] ({}) {}/{} - {}/{}".format(
                self.__class__.__name__, self.id,
                self.x, self.y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """ Update """
        for i in range(len(args)):
            if i == 0:
                self.id = args[0]
            elif i == 1:
                self.__width = args[1]
            elif i == 2:
                self.__height = args[2]
            elif i == 3:
                self.__x = args[3]
            elif i == 4:
                self.__y = args[4]
        if not args:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == 'width':
                    self.__width = value
                if key == 'height':
                    self.__height = value
                if key == 'x':
                    self.__x = value
                if key == 'y':
                    self.__y = value

    def to_dictionary(self):
        """ Dictionary """
        return {
            'x': self.x,
            'y': self.y,
            'id': self.id,
            'height': self.height,
            'width': self.width
        }
