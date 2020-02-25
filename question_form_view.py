from PySide2.QtCore import Signal, Slot, Qt, QAbstractTableModel, QModelIndex, QAbstractItemModel, QObject
from PySide2.QtGui import QBrush, QPen, QFont, QShowEvent, QResizeEvent, QColor, QStandardItemModel, QStandardItem
from PySide2.QtWidgets import QWidget, QMessageBox, QGraphicsScene, QGraphicsItem, QAbstractItemView, QDataWidgetMapper
import typing
from question_form import Ui_Form
import dataset
from collections import OrderedDict
from models import QuestionModel

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
        # each record in a table is an ordered dict with all the fields
        for record in all_data:
            data.append(record)

        # store the abstract table model derived instance
        self.model = QuestionModel(data)
        self.table.setModel(self.model)
        self.selections = self.table.selectionModel()
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.selectionModel().selectionChanged.connect(self.select_item)

        self.mapper.setModel(self.model)
        # note, it's essential this stuff comes after the call to setModel on the QDataWidgetMapper instance
        self.mapper.addMapping(self.ui.txtID, 0)
        self.mapper.addMapping(self.ui.txtBody, 1)
        self.mapper.addMapping(self.ui.cboTags, 2)
        self.mapper.addMapping(self.ui.txtAnswer, 3)


    def showEvent(self, event: QShowEvent):
        print('I am called when form is shown')

    def clear_fields(self):
        self.ui.txtID.setText('')
        self.ui.txtAnswer.setPlainText('')
        self.ui.txtBody.setText('')
        self.ui.cboTags.setCurrentIndex(0)

    @Slot()
    def select_item(self):
        selected_row_index: int = self.selections.selectedIndexes()[0].row()
        # selected_data = self.model.data_set[selected_row_index]
        self.mapper.setCurrentIndex(selected_row_index)

    @Slot()
    def add_click(self):
        #new_question = {"body": self.ui.txtBody.text(), "tag": self.ui.cboTags.itemData(self.ui.cboTags.currentIndex()),
        #               "answer": self.ui.txtAnswer.text()}
        new_question = {'id': -1, 'body': '', 'tag': '', 'answer': ''}
        self.model.beginInsertRows(QModelIndex(), self.model.row_count, self.model.row_count)
        self.model.data_set.append(new_question)
        self.model.endInsertRows()
        # this next line is essential when adding rows
        self.model.row_count = self.model.row_count + 1
        self.mapper.toLast()
        #self.clear_fields()

    @Slot()
    def save_click(self):
        current_index = self.mapper.currentIndex()

        # does not keep the type of the data, all becomes a string
        body = self.get_model_data(current_index, 1)
        tag = self.get_model_data(current_index, 2)
        answer = self.get_model_data(current_index, 3)
        record_id = self.get_model_data(current_index, 0)
        # lets update the database
        if record_id == -1:
            self.data_table.insert(dict(body= body, tag= tag, answer= answer))
        else:
            self.data_table.upsert(dict(id=record_id, body= body, tag= tag, answer= answer), ['id'])

    def get_model_data(self, row, column):
        index: QModelIndex = self.mapper.model().index(row, column)
        return self.mapper.model().data(index)






