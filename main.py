# This Python file uses the following encoding: utf-8
import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtGui import QStandardItemModel, QStandardItem, QIcon
from PySide2.QtCore import QItemSelectionModel
from mainwindow import Ui_MainWindow
from tabsample import TabSample
from christmas_tree_view import ChristmasTreeView
from models import NavigationItem, NavigationModel

# database stuff, to be moved elsewhere
import dataset

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnAddTab.clicked.connect(self.addTabClick)
        self.ui.actionQuit.triggered.connect(QApplication.quit)
        self.ui.actionChristmas_Tree.triggered.connect(self.handle_action_christmas_tree)
        self.ui.actionDatabase_Test.triggered.connect(self.handle_action_database_test)

        # view, navTree holds model instance, navModel
        # self.ui.navTree.setModel(self.navModel)
        self.ui.navTree.setModel(NavigationModel())
        self.ui.navTree.setSortingEnabled(False)
        self.selection_model = self.ui.navTree.selectionModel()
        self.selection_model.selectionChanged.connect(self.navigationselected)

        #self.ui.navTree.show()


    def addTabClick(self):
        self.ui.tabWidget.addTab(TabSample(), "New")

    def handle_action_christmas_tree(self):
        tab_index = self.ui.tabWidget.addTab(ChristmasTreeView(), "Graphics View")
        self.ui.tabWidget.setCurrentIndex(tab_index)

    def handle_action_database_test(self):
        print("database test")
        db = dataset.connect('sqlite:///kernai.db')
        questions = db['questions']
        # questions.insert(dict(body='declare a map with 3 values', tag='collections', expected_answer='{"name":"fred", "name":"thelma", "name":"louise"}'))
        # questions.insert(dict(body='declare a list with 3 values', tag='collections', expected_answer='["fred", "themlma", "louise"]'))
        for question in db['questions']:
            print(question['body'])


    def navigationselected(self, selected, deselected):
        items = selected.indexes()
        for x in items:
            print(x.data())


if __name__ == "__main__":
    try:
        app = QApplication([])
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())
    except Exception as inst:
        print("error in main: ", inst)
        pass
