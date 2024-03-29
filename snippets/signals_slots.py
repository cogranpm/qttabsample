import sys
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import QObject, Signal, Slot

@Slot(str)
def say_some_words(words):
    print(words)

class SignalExample(QObject):
    speak = Signal(str)


def test_signal():
    someone = SignalExample()
    someone.speak.connect(say_some_words)
    someone.speak.emit("helloworldlybeings")


app = QApplication(sys.argv)
test_signal()



