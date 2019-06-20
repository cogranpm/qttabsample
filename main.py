# This Python file uses the following encoding: utf-8
import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget
from mainwindow import Ui_MainWindow
from tab_page import Ui_TabPage

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.tabPage = TabPage()
        self.ui.tabWidget.addTab(self.tabPage, "New")


class TabPage(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_TabPage()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
