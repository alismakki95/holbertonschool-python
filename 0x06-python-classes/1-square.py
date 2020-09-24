#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").__doc__)'"""


class Square:
    """python3 -c 'print(__import__("my_module").MyClass.__doc__)'"""
    __size = 0

    def __init__(self, new_size=0):
        """python3 -c 'print(__import__("my_module").MyClass.my_functi
        on.__doc__)'"""
        """Initialize class."""
        if new_size is not 0:
            self.__size = new_size
