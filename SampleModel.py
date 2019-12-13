""" demo of qt notiion of entity with properties
could also use the python notion, which uses @ attributes
"""
from dataclasses import dataclass
from datetime import date

from PySide2.QtCore import QObject, Signal, Slot, Property


class Model(QObject):
    model_changed = Signal(str)

    def __init__(self, parent= None):
        super().__init__(parent)
        self._int = 0
        self._float = 0.0
        self._bool = False
        self._complex = 0.0
        self._string = "hello"


    def getint(self):
        return self._int

    def setint(self, val):
        self._int = val
        self.model_changed.emit("int changed")

    def getfloat(self):
        return self._float

    def setfloat(self, val):
        self._float = val
        self.model_changed.emit("float changed")

    def getbool(self):
        return self._bool

    def setbool(self, val):
        self._bool = val
        self.model_changed.emit("bool changed")

    def getcomplex(self):
        return self._complex

    def setcomplex(self, val):
        self._complex = val
        self.model_changed.emit("complex changed")

    def getstring(self):
        return self._string

    def setstring(self, val):
        self._string = val
        self.model_changed.emit("string changed")

    pint = Property(int, getint, setint)
    pfloat = Property(float, getfloat, setfloat)
    pbool = Property(bool, getbool, setbool)
    pcomplex = Property(complex, getcomplex, setcomplex)
    pstring = Property(str, getstring, setstring)


class Person:

    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @first_name.setter
    def first_name(self, val):
        self._first_name = val

    @last_name.setter
    def last_name(self, val):
        self._last_name = val


# creates an immutable value object
@dataclass(frozen=True)
class Order:
    id: int
    qty: int
    notes: str
    created: date

