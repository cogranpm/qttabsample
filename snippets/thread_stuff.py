from PySide2.QtCore import QEventLoop
from PySide2.QtCore import QTimer

# event loop example
def event_loop_sample():
    event_loop = QEventLoop()
    timer = QTimer()
    timer.setSingleShot(True)
    timer.setInterval(200)
    timer.start()
    event_loop.exec()
