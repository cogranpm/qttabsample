from PySide2.QtCore import Signal, Slot, Qt, QAbstractTableModel, QModelIndex
from PySide2.QtGui import QBrush, QPen, QFont, QShowEvent, QResizeEvent, QColor
from PySide2.QtWidgets import QWidget, QMessageBox, QGraphicsScene, QGraphicsItem, QAbstractItemView


from question_form import Ui_Form

import dataset


class QuestionModel(QAbstractTableModel):

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

        #print(f"I am data-ing here, column: {column} row: {row}")
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
        return Qt.ItemFlags(QAbstractTableModel.flags(self, index) | Qt.ItemIsEditable )

    def setData(self, index, value, role: int = Qt.EditRole):
        if role != Qt.EditRole:
            return False

        if index.isValid() and 0 <= index.row() < len(self.data_set):
            question = self.data_set[index.row()]
            if index.column() == 0:
                question["body"] = value
            elif index.column() == 1:
                question["tag"] = value
            elif index.column() == 2:
                question["answer"] = value
            else:
                return False

            self.dataChanged.emit(index, index, 0)
            return True
        return False

    # todo, should we look at
    # insertRows, removeRows, setData (for editing)
    def insertRows(self, position, rows=1, index=QModelIndex()):
        self.beginInsertRows(index, position, position + rows - 1)
        for row in range(rows):
            self.data_set.insert(position + row, {'body': 'how to create immutable map in python', 'tag': 'collections',
                              'answer': 'there is no way to do it'})
        #self.data_set.append({'body': 'how to create immutable map in python', 'tag': 'collections', 'answer': 'there is no way to do it'})
        self.endInsertRows()
        #return QAbstractTableModel.insertRows(self, row, count, index)
        print("bogshite")
        return True

    # def insertRow(self, row, index=QModelIndex()):
    #     self.beginInsertRows(index, row, row)
    #     self.data_set.append({'body': 'how to create immutable map in python', 'tag': 'collections',
    #                           'answer': 'there is no way to do it'})
    #     self.endInsertRows()
    #     return True


class QuestionFormView(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        tags = ['collections', 'other', 'functional']
        for tag in tags:
            self.ui.cboTags.addItem(tag, tag)
        data = [{'body': 'something', 'tag': 'collections', 'answer': 'answer'}, {'body': 'who invented perl', 'tag': 'functional', 'answer': 'Larry Wall'}]

        self.table = self.ui.questionView
        self.model = QuestionModel(data)
        self.table.setModel(self.model)
        self.ui.btnAdd.clicked.connect(self.add_click)

        self.selections = self.table.selectionModel()
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.selectionModel().selectionChanged.connect(self.select_item)

        # using the dataset sql library to connect to sqlite
        self.db = dataset.connect('sqlite:///kernai.db')
        self.questions = self.db['questions']

    def showEvent(self, event: QShowEvent):
        for question in self.db['questions']:
            print(question['body'])
            print(question['answer'])

    @Slot()
    def select_item(self):
        for index in self.selections.selectedIndexes():
            print(index)

    @Slot()
    def add_click(self):
        new_question = {"body": self.ui.txtBody.text(), "tag": self.ui.cboTags.itemData(self.ui.cboTags.currentIndex()),
                        "answer": self.ui.txtAnswer.text()}
        self.model.beginInsertRows(QModelIndex(), self.model.row_count, self.model.row_count)
        self.model.data_set.append(new_question)
        self.model.endInsertRows()
        self.model.row_count = self.model.row_count + 1
        #self.ui.questionView.update()








