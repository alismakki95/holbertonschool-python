#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").__doc__)'"""


class Square:
    """python3 -c 'print(__import__("my_module").MyClass.__doc__)'"""
    __size = 0

    def __init__(self, size=0):
        """python3 -c 'print(__import__("my_module").MyClass.my_function
        .__doc__)'"""
        """Initialize class."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """python3 -c 'print(__import__("my_module").MyClass.my_function
        .__doc__)'"""
        """Square area."""
        return (self.__size * self.__size)

    @property
    def size(self):
        """python3 -c 'print(__import__("my_module").MyClass.my_function
        .__doc__)'"""
        """getter def"""
        return self.__size

    @size.setter
    def size(self, value):
        """python3 -c 'print(__import__("my_module").MyClass.my_function
        .__doc__)'"""
        """setter def"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
