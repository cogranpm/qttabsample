from PySide2.QtCore import Signal, Slot, Qt, QAbstractTableModel, QModelIndex
from PySide2.QtGui import QBrush, QPen, QFont, QShowEvent, QResizeEvent, QColor
from PySide2.QtWidgets import QWidget, QMessageBox, QGraphicsScene, QGraphicsItem


from question_form import Ui_Form

import dataset


class question_model(QAbstractTableModel):

    def __init__(self, data=None):
        QAbstractTableModel.__init__(self)
        self.load_data(data)

    def load_data(self, data):
        self.bodys = data[0].values
        self.tags = data[1].values
        self.answers = data[2].values
        self.column_count = 3
        self.row_count = 0

    def rowCount(self, parent=QModelIndex):
        return self.row_count

    def columnCount(self, parent=QModelIndex):
        return self.column_count

    def headerData(self, section, orientation, role):
        if role != Qt.DisplayRole:
            return None
        if orientation == Qt.Horizontal:
            return ("Body", "Tag", "Answer")[section]
        else:
            return "{}".format(section)

    def data(self, index, role=Qt.DisplayRole):
        column = index.column()
        row = index.row()
        # more stuff

class question_form_view(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        tags = ['collections', 'other', 'functional']
        for tag in tags:
            self.ui.cboTags.addItem(tag, tag)
        data = [{'body':'something', 'tag':'collections', 'answer':'answer'}]

        self.model = question_model(data)
        self.ui.questionView.setModel(self.model)
        self.ui.btnAdd.clicked.connect(self.add_click)
        self.db = dataset.connect('sqlite:///kernai.db')
        self.questions = self.db['questions']

    def showEvent(self, event: QShowEvent):
        for question in self.db['questions']:
            print(question['body'])
            print(question['answer'])

    def add_click(self):
        new_question = {}
        new_question["body"] = self.ui.txtBody.text()
        new_question["tag"] = self.ui.cboTags.itemData(self.ui.cboTags.currentIndex())
        new_question["answer"] = self.ui.txtAnswer.text()
        print(new_question)
        self.questions.insert(new_question)


