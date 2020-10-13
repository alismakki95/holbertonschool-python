#!/usr/bin/python3
""" Unittest Base class """

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json
import os
import pep8


class TestBase(unittest.TestCase):
    """ Test Base """

    def tearDown(self):
        """ no test """
        Base._Base__nb_objects = 0

    def test_docstring(self):
        """ Test docstring """
        self.assertIsNotNone(Base.__doc__)

    def test_style_pep8(self):
        """ Test pep8 style """
        pep8 = pep8.StyleGuide(quiet=True)
        result = pep8.check_files(['./models/base.py'])
        self.assertEqual(result.total_errors, 0, "Error: Fix pep8")

    def test_instance(self):
        """ Test isInstance """
        b = Base()
        self.assertIsInstance(b, Base)

    def test_has_attrb(self):
        """ Test hasattr """
        self.assertTrue(hasattr(Base, "__init__"))
        self.assertTrue(hasattr(Base, "create"))
        self.assertTrue(hasattr(Base, "to_json_string"))
        self.assertTrue(hasattr(Base, "from_json_string"))
        self.assertTrue(hasattr(Base, "save_to_file"))
        self.assertTrue(hasattr(Base, "load_from_file"))

    def test_create(self):
        """ Test create """
        base = Base()
        test = str(base)
        base1 = Base(12)
        test1 = str(base1)
        base2 = Base()
        test2 = str(base2)
        self.assertTrue(test[:29], '<models.base.Base object at ')
        self.assertTrue(base.id, 1)
        self.assertTrue(test1[:29], '<models.base.Base object at ')
        self.assertTrue(base1.id, 12)
        self.assertTrue(test2[:29], '<models.base.Base object at ')
        self.assertTrue(base2.id, 2)

    def test_nbobjects(self):
        """ Test nb_objects increment """
        base = Base()
        test = base.id
        base1 = Base()
        base2 = Base(id=33)
        base3 = Base(-2)
        self.assertTrue(test + 1, base1)
        self.assertTrue(base2.id, 33)
        self.assertTrue(base3.id, -2)

    def test_priv_nbobjects(self):
        """ Test nb_objects private """
        base = Base(3)
        with self.assertRaises(AttributeError):
            print(base.nb_objects)
        with self.assertRaises(AttributeError):
            print(base.__nb_objects)

    def test_create_rectangle(self):
        """ Test create rectangle """
        r = Rectangle(5, 6, 7)
        r_dictionary = r.to_dictionary()
        r1 = Rectangle.create(**r_dictionary)
        self.assertNotEqual(r, r1)

    def test_create_square(self):
        """ Test create square """
        s = Square(2, 3, 3, 4)
        s_dictionary = s.to_dictionary()
        s1 = Square.create(**s_dictionary)
        self.assertNotEqual(s, s1)

    def test_to_json_string(self):
        """ Test use to_json_string """
        r = Rectangle(10, 7, 2, 8)
        d = r.to_dictionary()
        jd = {'x': 2, 'y': 8, 'id': 1, 'height': 7, 'width': 10}
        jdictionary = Base.to_json_string([d])
        self.assertEqual(d, jd)
        self.assertEqual(type(d), dict)
        self.assertEqual(type(jdictionary), str)

    def test_to_json_string_json(self):
        """ Test use to_json_string JSON """
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertTrue(type(Base.to_json_string(None)) is str)
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertTrue(type(Base.to_json_string([])) is str)
        d = {'id': 7, 'width': 10, 'height': 7, 'x': 4, 'y': 8}
        d1 = {'id': 8, 'width': 2, 'height': 5, 'x': 9, 'y': 3}
        convert = Base.to_json_string([d, d1])
        self.assertTrue(type(convert) is str)
        dic = json.loads(convert)
        self.assertEqual(dic, [d, d1])

    def test_from_json_string(self):
        """ Test from_json_string """
        string = '[{"id": 7, "width": 10, "height": 7, "x": 4, "y": 8}, \
            {"id": 8, "width": 2, "height": 5, "x": 9, "y": 3}]'
        jsconv = Base.from_json_string(string)
        self.assertTrue(type(jsconv) is list)
        self.assertEqual(len(jsconv), 2)

    def test_from_json_string_val_empty(self):
        """ Test from_json_string is empty """
        self.assertEqual(Base.from_json_string(""), [])
        self.assertEqual(Base.from_json_string(None), [])

    def test_save_to_file(self):
        """ Test None instances """
        Rectangle.save_to_file(None)
        with open("Rectangle.json", mode='r') as nfile:
            self.assertEqual([], json.load(nfile))
        Square.save_to_file(None)
        with open("Square.json", mode='r') as nfile:
            self.assertEqual([], json.load(nfile))

    def test_save_to_file_empty(self):
        """ Test empty instances """
        Rectangle.save_to_file([])
        with open("Rectangle.json", mode='r') as nfile:
            self.assertEqual([], json.load(nfile))
        Square.save_to_file([])
        with open("Square.json", mode='r') as nfile:
            self.assertEqual([], json.load(nfile))

    def test_save_and_load_rectangle(self):
        """ Test loads rectangle """
        r = Rectangle(5, 6, 7)
        r1 = Rectangle(10, 5)
        listrectangles = [r, r1]
        Rectangle.save_to_file(listrectangles)
        listrectangle = Rectangle.load_from_file()
        self.assertNotEqual(listrectangles, listrectangle)

    def test_save_and_load_square(self):
        """ Test file square """
        s = Square(5, 6, 7)
        s1 = Square(10, 5, 6)
        listsquares = [s, s1]
        Square.save_to_file(listsquares)
        listsquare = Square.load_from_file()
        self.assertNotEqual(listsquares, listsquare)

    def test_csv_square(self):
        """ Test csv sqr """
        R1 = Rectangle(12, 13, 14, 15)
        R2 = Rectangle(3, 5)
        lR = [R1, R2]
        Rectangle.save_to_file_csv(lR)
        lR2 = Rectangle.load_from_file_csv()
        self.assertTrue(lR[0].__str__() == lR2[0].__str__())
        self.assertTrue(lR[1].__str__() == lR2[1].__str__())

    def test_csv_none_rectangle(self):
        """ Test csv None rectangle """
        Rectangle.save_to_file_csv(None)
        self.assertEqual(Rectangle.load_from_file_csv(), [])
        os.remove("Rectangle.csv")
        self.assertEqual(Rectangle.load_from_file_csv(), [])

    def test_document(self):
        """ Test document """
        self.assertTrue(Base.__init__.__doc__)
        self.assertTrue(Base.create.__doc__)
        self.assertTrue(Base.to_json_string.__doc__)
        self.assertTrue(Base.from_json_string.__doc__)
        self.assertTrue(Base.save_to_file.__doc__)
        self.assertTrue(Base.load_from_file.__doc__)
