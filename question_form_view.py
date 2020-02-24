from PySide2.QtCore import Signal, Slot, Qt, QAbstractTableModel, QModelIndex, QAbstractItemModel, QObject
from PySide2.QtGui import QBrush, QPen, QFont, QShowEvent, QResizeEvent, QColor, QStandardItemModel, QStandardItem
from PySide2.QtWidgets import QWidget, QMessageBox, QGraphicsScene, QGraphicsItem, QAbstractItemView, QDataWidgetMapper
import typing
from question_form import Ui_Form
import dataset
from collections import OrderedDict


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

        # declare the list holding data used by the form, local variable that will be referenced by the model
        # is a list of OrderedDict items
        data = []
        self.table = self.ui.questionView
        self.ui.btnAdd.clicked.connect(self.add_click)
        self.ui.btnSave.clicked.connect(self.save_click)
        self.mapper = QDataWidgetMapper()
        # using the dataset sql library to connect to sqlite
        self.db = dataset.connect('sqlite:///kernai.db')
        self.data_table: dataset.Table = self.db['questions']
        # all call is not actually required here, but makes things explicit
        all_data: dataset.util.ResultIter = self.data_table.all()
        widget_model: QStandardItemModel = QStandardItemModel()
        # each record in a table is an ordered dict with all the fields
        index = 0
        for record in all_data:
            data.append(record)
            self.setup_mapper(index, record, widget_model)
            index += 1

        # store the abstract table model derived instance
        self.model = QuestionModel(data)
        self.table.setModel(self.model)
        self.selections = self.table.selectionModel()
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.selectionModel().selectionChanged.connect(self.select_item)

        widget_model.setRowCount(index)
        widget_model.setColumnCount(4)
        self.mapper.setModel(widget_model)
        # note, it's essential this stuff comes after the call to setModel on the QDataWidgetMapper instance
        self.mapper.addMapping(self.ui.txtID, 0)
        self.mapper.addMapping(self.ui.txtBody, 1)
        self.mapper.addMapping(self.ui.cboTags, 2)
        self.mapper.addMapping(self.ui.txtAnswer, 3)


    def showEvent(self, event: QShowEvent):
        print('I am called when form is shown')

    def setup_mapper(self, index: int, row: OrderedDict, model: QStandardItemModel):
        model.setItem(index, 0, QStandardItem(str(row['id'])))
        model.setItem(index, 1, QStandardItem(row['body']))
        model.setItem(index, 2, QStandardItem(row['tag']))
        model.setItem(index, 3, QStandardItem(row['answer']))

    @Slot()
    def select_item(self):
        selected_row_index: int = self.selections.selectedIndexes()[0].row()
        # selected_data = self.model.data_set[selected_row_index]
        self.mapper.setCurrentIndex(selected_row_index)

    @Slot()
    def add_click(self):
        new_question = {"body": self.ui.txtBody.text(), "tag": self.ui.cboTags.itemData(self.ui.cboTags.currentIndex()),
                        "answer": self.ui.txtAnswer.text()}
        self.model.beginInsertRows(QModelIndex(), self.model.row_count, self.model.row_count)
        self.model.data_set.append(new_question)
        self.model.endInsertRows()
        # this next line is essential when adding rows
        self.model.row_count = self.model.row_count + 1

    @Slot()
    def save_click(self):
        current_index = self.mapper.currentIndex()

        # does not keep the type of the data, all becomes a string
        body = self.get_model_data(current_index, 1)
        tag = self.get_model_data(current_index, 2)
        answer = self.get_model_data(current_index, 3)
        id = self.get_model_data(current_index, 0)
        #print(id, body, answer, tag)
        print(type(id))
        # lets update the database
        self.data_table.upsert(dict(id=id, body= body, tag= tag, answer= answer), ['id'])

    def get_model_data(self, row, column):
        index: QModelIndex = self.mapper.model().index(row, column)
        return self.mapper.model().data(index)






