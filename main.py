# This Python file uses the following encoding: utf-8
import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtGui import QStandardItemModel, QStandardItem, QIcon
from PySide2.QtCore import QItemSelectionModel, Slot
from mainwindow import Ui_MainWindow
from tabsample import TabSample
from christmas_tree_view import ChristmasTreeView
from models import NavigationItem, NavigationModel
from question_form_view import QuestionFormView


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

    @Slot()
    def addTabClick(self):
        self.ui.tabWidget.addTab(TabSample(), "New")

    @Slot()
    def handle_action_christmas_tree(self):
        tab_index = self.ui.tabWidget.addTab(ChristmasTreeView(), "Graphics View")
        self.ui.tabWidget.setCurrentIndex(tab_index)

    @Slot()
    def handle_action_database_test(self):
        self.ui.tabWidget.addTab(QuestionFormView(), "Questions")

    @Slot()
    def navigationselected(self, selected, deselected):
        items = selected.indexes()
        for x in items:
            print(x.data())


def run():
    try:
        app = QApplication([])
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())
    except Exception as inst:
        print("error in main: ", inst)   

if __name__ == "__main__":
    run()

