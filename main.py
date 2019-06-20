# This Python file uses the following encoding: utf-8
import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget
from mainwindow import Ui_MainWindow
from tabsample import TabSample


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnAddTab.clicked.connect(self.addTabClick)

    def addTabClick(self):
        self.ui.tabWidget.addTab(TabSample(), "New")


if __name__ == "__main__":
    try:
        app = QApplication([])
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())
    except Exception:
        print ("error in main")
        pass
