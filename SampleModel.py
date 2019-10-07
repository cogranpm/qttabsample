""" demo of qt notiion of entity with properties
could also use the python notion, which uses @ attributes
"""
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
