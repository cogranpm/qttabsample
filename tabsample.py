# This Python file uses the following encoding: utf-8
from PySide2.QtCore import Signal, Slot
from PySide2.QtWidgets import QWidget, QMessageBox
from tab_page import Ui_TabPage
from SampleModel import Model
from SampleModel import Person

class TabSample(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_TabPage()
        self.ui.setupUi(self)
        self.ui.btnTest.clicked.connect(self.test_clicked)

    def test_clicked(self):

        # mucking about with models
        model = Model(None)
        model.model_changed.connect(self.model_changed)
        model.pint = 444
        model.pfloat = 777.777
        model.pcomplex = 9.848744774
        model.pstring = "hello there" + model.pstring
        model.pbool = True

        person = Person("fred", "munroe")
        person.first_name = "senior"
        person.last_name = "frog"
        print(person.last_name)

        msg = QMessageBox()
        msg.setText("clicked button")
        msg.setInformativeText("Model values: Int:{0} Float:{1} Complex:{2} String:{3} Bool:{4}".format(model.pint, model.pfloat, model.pcomplex, model.pstring, model.pbool))
        msg.setStandardButtons(QMessageBox.Cancel)
        msg.setDefaultButton(QMessageBox.Cancel)
        ret = msg.exec_()

    @Slot(str)
    def model_changed(self, message):
        print("model changed:" + message)

