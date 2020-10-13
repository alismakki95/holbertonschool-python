#!/usr/bin/python3
""" Square class Module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class """

    def __init__(self, width, x=0, y=0, id=None):
        """ Initialize """
        super().__init__(width, width, x, y, id)

    @property
    def size(self):
        """ Getter for width of square """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter for size of square """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        self.width = value
        self.height = value

    def __str__(self):
        """ __str__ """
        return ("[{}] ({}) {}/{} - {}".format(
                self.__class__.__name__, self.id,
                self.x, self.y, self.width))

    def update(self, *args, **kwargs):
        """ Update """
        if len(args) > 0:
            if args[0] is not None:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
                self.height = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        if not args:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == "size":
                    self.width = value
                    self.height = value

                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value

    def to_dictionary(self):
        """ Dictionary """
        return {'x': self.x, 'y': self.y, 'id': self.id, 'size': self.width}
