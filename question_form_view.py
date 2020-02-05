from PySide2.QtCore import Signal, Slot, Qt, QAbstractTableModel, QModelIndex
from PySide2.QtGui import QBrush, QPen, QFont, QShowEvent, QResizeEvent, QColor
from PySide2.QtWidgets import QWidget, QMessageBox, QGraphicsScene, QGraphicsItem


from question_form import Ui_Form

import dataset


class question_model(QAbstractTableModel):

    def __init__(self, columns, data=None):
        QAbstractTableModel.__init__(self)
        self.load_data(data)
        self.columns = columns

    def load_data(self, data):
        self.data = data

    def rowCount(self, parent=QModelIndex):
        return len(self.data)

    def columnCount(self, parent=QModelIndex):
        return len(self.columns)

    def setData(self, index, value, role=Qt.EditRole):
        if role == Qt.EditRole:
            row = index.row()
            column = index.column()
            # got to put value back into the dataset
            self.data[row][column] = value
            #print(value)
            return True
        return False


    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self.columns[section])
            elif orientation == Qt.Vertical:
                pass
        elif role == Qt.TextAlignmentRole:
                if orientation == Qt.Horizontal:
                    return Qt.AlignCenter
        return None

    def flags(self, index):
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable


    def data(self, index, role):
        column = index.column()
        row = index.row()
        # more stuff
        if role == Qt.DisplayRole:
            #return str(self.data[row][column])
            return "fagg off"
        elif role == Qt.TextAlignmentRole:
            return Qt.AlignLeft
        return None

class question_form_view(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        tags = ['collections', 'other', 'functional']
        for tag in tags:
            self.ui.cboTags.addItem(tag, tag)
        data = [['something', 'collections', 'answer'], ['question', 'collections', 'answer']]

        self.model = question_model(['Body', 'Tag', 'Answer'], data)
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


