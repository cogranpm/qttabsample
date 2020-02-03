from PySide2.QtCore import Signal, Slot
from PySide2.QtGui import QBrush, QPen, QFont, QShowEvent, QResizeEvent
from PySide2.QtWidgets import QWidget, QMessageBox, QGraphicsScene, QGraphicsItem
from PySide2.QtCore import Qt
from question_form import Ui_Form

import dataset


class question_form_view(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.btnAdd.clicked.connect(self.add_click)

    def showEvent(self, event: QShowEvent):
        self.db = dataset.connect('sqlite:///kernai.db')
        self.questions = self.db['questions']
        for question in self.db['questions']:
            print(question['body'])
            print(question['answer'])

    def add_click(self):
        new_question = {}
        new_question["body"] = self.ui.txtBody.text()
        new_question["tag"] = self.ui.txtTag.text()
        new_question["answer"] = self.ui.txtAnswer.text()
        self.questions.insert(new_question)


