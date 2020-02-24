from PySide2.QtCore import Signal, Slot, Qt, QAbstractTableModel, QModelIndex, QAbstractItemModel, QObject
from PySide2.QtGui import QBrush, QPen, QFont, QShowEvent, QResizeEvent, QColor, QStandardItemModel
from PySide2.QtWidgets import QWidget, QMessageBox, QGraphicsScene, QGraphicsItem, QAbstractItemView
import typing
from question_form import Ui_Form
import dataset


class ItemModel(QStandardItemModel):

    def __init__(self):
        QStandardItemModel.__init__(None)

    def index(self, row:int, column:int, parent:QModelIndex= QModelIndex()) -> QModelIndex:
        pass

    def parent(self) -> QObject:
        pass

    def rowCount(self, parent:QModelIndex= QModelIndex()) -> int:
        pass

    def columnCount(self, parent:QModelIndex= QModelIndex()) -> int:
        pass

    def data(self, index:QModelIndex, role:int=...) -> typing.Any:
        pass

    def setData(self, index:QModelIndex, value:typing.Any, role:int=...) -> bool:
        pass

    def flags(self, index:QModelIndex) -> Qt.ItemFlags:
        pass


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
        #data = [{'body': 'something', 'tag': 'collections', 'answer': 'answer'}, {'body': 'who invented perl', 'tag': 'functional', 'answer': 'Larry Wall'}]
        data = []

        self.table = self.ui.questionView
        self.ui.btnAdd.clicked.connect(self.add_click)
        # using the dataset sql library to connect to sqlite
        self.db = dataset.connect('sqlite:///kernai.db')
        #self.questions = self.db['questions']
        #self.model = QuestionModel(self.questions)

        print(type(self.db['questions']))
        data_table: dataset.Table = self.db['questions']
        print(data_table.columns)
        all_data = data_table.all()
        for record in all_data:
            print(record)
            data.append({'body': record['body'], 'tag': record['tag'], 'answer': record['answer']})

        self.model = QuestionModel(data)
        self.table.setModel(self.model)
        self.selections = self.table.selectionModel()
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.selectionModel().selectionChanged.connect(self.select_item)

    def showEvent(self, event: QShowEvent):
        for question in self.db['questions']:
            print(question['id'])
            print(question['body'])
            print(question['answer'])



    @Slot()
    def select_item(self):
        selected_row = self.selections.selectedIndexes()[0].row()
        selected_data = self.model.data_set[selected_row]
        print(selected_data)


    @Slot()
    def add_click(self):
        new_question = {"body": self.ui.txtBody.text(), "tag": self.ui.cboTags.itemData(self.ui.cboTags.currentIndex()),
                        "answer": self.ui.txtAnswer.text()}
        self.model.beginInsertRows(QModelIndex(), self.model.row_count, self.model.row_count)
        self.model.data_set.append(new_question)
        self.model.endInsertRows()
        self.model.row_count = self.model.row_count + 1
        #self.ui.questionView.update()








