# This Python file uses the following encoding: utf-8
from PySide2.QtWidgets import QWidget
from tab_page import Ui_TabPage

class TabSample(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_TabPage()
        self.ui.setupUi(self)
        self.ui.btnTest.clicked.connect(self.test_clicked)

    def test_clicked(self):
        print ('clicked me')
