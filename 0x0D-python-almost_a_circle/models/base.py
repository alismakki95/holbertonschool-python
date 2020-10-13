#!/usr/bin/python3
""" Base class Module"""

import json
import csv
import turtle
import os
import sys


class Base:
    """ Base class """
    __nb_objects = 0
    id = 0

    def __init__(self, id=None):
        """ initialize """
        if id is None:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = self.__nb_objects
        else:
            self.id = id

    @classmethod
    def create(cls, **dictionary):
        """ create """
        if cls.__name__ == "Rectangle":
            new = cls(1, 1, 0, 0)
        elif cls.__name__ == "Square":
            new = cls(1, 0, 0)
        new.update(**dictionary)
        return new

    @staticmethod
    def to_json_string(list_dictionaries):
        """ json to string represent """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """ json to string represent / empty """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """ JSON string on the file """
        with open('{}.json'.format(cls.__name__), 'w') as f:
            if list_objs is None:
                f.write(cls.to_json_string([]))
            else:
                jlist = []
                for i in list_objs:
                    i = i.to_dictionary()
                    jlist.append(i)
                f.write(cls.to_json_string(jlist))

    @classmethod
    def load_from_file(cls):
        """ load_from_files """
        try:
            with open('{}.json'.format(cls.__name__), encoding='utf-8') as f:
                jtxt = f.read()
                clss = cls.from_json_string(jtxt)
                list = []
                for i in clss:
                    list.append(cls.create(**i))
                return list
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ save_to_file_csv """
        filename = cls.__name__ + ".csv"
        if filename == "Rectangle.csv":
            fields = ["id", "width", "height", "x", "y"]
        else:
            fields = ["id", "size", "x", "y"]
        with open(filename, mode="w", newline="") as f:
            if list_objs is None:
                writer = csv.writer(f)
                writer.writerow([[]])
            else:
                writer = csv.DictWriter(f, fieldnames=fields)
                writer.writeheader()
                for x in list_objs:
                    writer.writerow(x.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """ load_from_file_csv """
        try:
            with open('{}.csv'.format(cls.__name__), newline="") as f:
                reader = csv.DictReader(f)
                my_list = []
                for x in reader:
                    for i, n in x.items():
                        x[i] = int(n)
                    my_list.append(x)
                return ([cls.create(**objt) for objt in my_list])
        except FileNotFoundError:
            return ([])

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ draw - Draws squares and rectangles """
        my_turtle = turtle.Turtle()
        for r in list_rectangles:
            my_turtle.setheadint(0)
            my_turtle.penup()
            my_turtle.goto(r.c, r.y)
            my_turtle.pendown()
            my_turtle.forward(r.width)
            my_turtle.right(90)
            my_turtle.forward(r.height)
            my_turtle.right(90)
            my_turtle.forward(r.width)
            my_turtle.right(90)
            my_turtle.forward(r.height)

        for s in list_squares:
            my_turtle.setheadint(0)
            my_turtle.penup()
            my_turtle.goto(s.c, s.y)
            my_turtle.pendown()
            my_turtle.forward(s.size)
            my_turtle.right(90)
            my_turtle.forward(s.size)
            my_turtle.right(90)
            my_turtle.forward(s.size)
            my_turtle.right(90)
            my_turtle.forward(s.size)

        input()
