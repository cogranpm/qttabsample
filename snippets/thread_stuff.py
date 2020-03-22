# are event loops an alternative to threading
import sys
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import QEventLoop, QTimer, Signal, Slot

@Slot()
def timer_expired():
    print("the timer expired")
    event_loop.quit()

app = QApplication(sys.argv)

# you can start up an event loop and tell it to quit when a signal of some sort is fired,
# say from a timer expired signal
event_loop = QEventLoop()
timer = QTimer()
timer.setSingleShot(True)
timer.setInterval(200)
timer.timeout.connect(timer_expired)
timer.start()
event_loop.exec_()
