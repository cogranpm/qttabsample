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
        self.data_set = data
        self.column_count = 3
        self.row_count = len(self.data_set)


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
        if not index.isValid():
            return None
        column = index.column()
        row = index.row()
        if role == Qt.DisplayRole:
            if column == 0:
                list_item = self.data_set[row]
                return list_item['body']
            elif column == 1:
                return self.data_set[row]['tag']
            else:
                return self.data_set[row]['answer']
        # more stuff
        return None

    def flags(self, index):
        if not index.isValid():
            return Qt.ItemIsEnabled
        return Qt.ItemFlags(QAbstractTableModel.flags(self, index))

    # todo, should we look at
    # insertRows, removeRows, setData (for editing)

class question_form_view(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        tags = ['collections', 'other', 'functional']
        for tag in tags:
            self.ui.cboTags.addItem(tag, tag)
        data = [{'body': 'something', 'tag': 'collections', 'answer': 'answer'}, {'body': 'who invented perl', 'tag': 'functional', 'answer': 'Larry Wall'}]

        self.model = question_model(data)
        self.ui.questionView.setModel(self.model)
        self.ui.btnAdd.clicked.connect(self.add_click)
        self.db = dataset.connect('sqlite:///kernai.db')
        self.questions = self.db['questions']

    def showEvent(self, event: QShowEvent):
        for question in self.db['questions']:
            print(question['body'])
            print(question['answer'])

    @Slot()
    def add_click(self):
        new_question = {}
        new_question["body"] = self.ui.txtBody.text()
        new_question["tag"] = self.ui.cboTags.itemData(self.ui.cboTags.currentIndex())
        new_question["answer"] = self.ui.txtAnswer.text()
        print(new_question)
        self.questions.insert(new_question)


