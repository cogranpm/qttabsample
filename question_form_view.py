from PySide2.QtCore import Signal, Slot, Qt, QAbstractTableModel, QModelIndex, QAbstractItemModel, QObject
from PySide2.QtGui import QBrush, QPen, QFont, QShowEvent, QResizeEvent, QColor, QStandardItemModel, QStandardItem
from PySide2.QtWidgets import QWidget, QMessageBox, QGraphicsScene, QGraphicsItem, QAbstractItemView, QDataWidgetMapper, QMessageBox
import typing
from question_form import Ui_Form
import dataset
from collections import OrderedDict
from models import QuestionModel
#import audio
import threading
import time
from datetime import date


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
        self.ui.btnDelete.clicked.connect(self.delete_click)

        self.ui.btnSoundTest.clicked.connect(self.sound_test_click)
        self.audio_recording = False
        self.audio_thread = None
        #self.default_mic = audio.get_default_mic()
        #self.default_speaker = audio.get_default_speaker()

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


    def run_delete_query(self, id:int):
        self.data_table.delete(id=id)

    @Slot()
    def sound_test_click(self):
        self.audio_recording = not self.audio_recording
        if self.audio_recording:
            self.ui.btnSoundTest.setText("Stop Audio")
            #self.audio_thread = threading.Thread(target=audio.test_sound_card, args=('Recording...', self.default_mic, 'demo.wav'))
            #self.audio_thread.start()
            #audio.test_sound_card()
        else:
            self.audio_thread.do_run = False
            self.audio_thread.join()
            # should put this on another killable thread
            #audio.play_audio(self.default_speaker)
            self.ui.btnSoundTest.setText("Start Audio")

        # audio.test_pyaudio()


    @Slot()
    def select_item(self):
        selected_row_index: int = self.selections.selectedIndexes()[0].row()
        # selected_data = self.model.data_set[selected_row_index]
        self.mapper.setCurrentIndex(selected_row_index)

    @Slot()
    def delete_click(self):
        if not (self.mapper.currentIndex() >= 0 and self.mapper.currentIndex() < len(self.model.data_set)):
            return
        confirm: int = QMessageBox.question(self, "Delete, are you sure?", "Do you wish to delete?", QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.StandardButton.Yes:
            question = self.model.data_set[self.mapper.currentIndex()]
            self.run_delete_query(question['id'])
            self.model.beginRemoveRows(QModelIndex(), self.mapper.currentIndex(), self.mapper.currentIndex())
            del self.model.data_set[self.mapper.currentIndex() - 1]
            self.model.endRemoveRows()
            self.model.row_count = self.model.row_count - 1
            self.clear_fields()


    @Slot()
    def add_click(self):
        #new_question = {"body": self.ui.txtBody.text(), "tag": self.ui.cboTags.itemData(self.ui.cboTags.currentIndex()),
        #               "answer": self.ui.txtAnswer.text()}
        today = date.today()
        print(date.fromtimestamp(time.time()))
        new_question = {'id': -1, 'body': '', 'tag': '', 'answer': ''}
        self.model.beginInsertRows(QModelIndex(), self.model.row_count, self.model.row_count)
        self.model.data_set.append(new_question)
        self.model.endInsertRows()
        # this next line is essential when adding rows
        self.model.row_count = self.model.row_count + 1
        self.mapper.toLast()
        self.ui.txtBody.setFocus()
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






