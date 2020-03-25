# This Python file uses the following encoding: utf-8
import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtGui import QStandardItemModel, QStandardItem, QIcon
from PySide2.QtCore import QItemSelectionModel, Slot, QObject, SIGNAL

#from pyside2.QtWidgets import QApplication, QMainWindow
#from pyside2.QtGui import QStandardItemModel, QStandardItem, QIcon
#from pyside2.QtCore import QItemSelectionModel, Slot, QObject, SIGNAL

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
        self.ui.actionSave.triggered.connect(self.handle_action_save)
        self.ui.actionDelete.triggered.connect(self.handle_action_delete)
        self.ui.actionNew.triggered.connect(self.handle_action_new)
        self.ui.tabWidget.tabCloseRequested.connect(self.closeTab)
        # this is old school style
        # QObject.connect(self.ui.tabWidget, SIGNAL('tabCloseRequested(int)'), self.closeTab)

        # view, navTree holds model instance, navModel
        # self.ui.navTree.setModel(self.navModel)
        self.ui.navTree.setModel(NavigationModel())
        self.ui.navTree.setSortingEnabled(False)
        self.selection_model = self.ui.navTree.selectionModel()
        self.selection_model.selectionChanged.connect(self.navigationselected)

        # keep the dictionary of views (inherit from QWidget) with a integer key that are in tabs
        self.tab_instances = {}

        #self.ui.navTree.show()

    @Slot()
    def handle_action_save(self):
        view = self.get_current_view()
        if view is not None:
            view.save()

    @Slot()
    def handle_action_new(self):
        view = self.get_current_view()
        if view is not None:
            view.new()

    @Slot()
    def handle_action_delete(self):
        view = self.get_current_view()
        if view is not None:
            view.delete()

    @Slot(int)
    def closeTab(self, index):
        self.ui.tabWidget.removeTab(index)
        if index in self.tab_instances:
            del self.tab_instances[index]

    @Slot()
    def addTabClick(self):
        self.ui.tabWidget.addTab(TabSample(), "New")

    @Slot()
    def handle_action_christmas_tree(self):
        view = ChristmasTreeView()
        tab_index = self.ui.tabWidget.addTab(view, "Graphics View")
        self.tab_instances[tab_index] = view
        self.ui.tabWidget.setCurrentIndex(tab_index)

    @Slot()
    def handle_action_database_test(self):
        view = QuestionFormView(self)
        new_index = self.ui.tabWidget.addTab(view, "Questions")
        self.tab_instances[new_index] = view
        self.ui.tabWidget.setCurrentIndex(new_index)


    @Slot()
    def navigationselected(self, selected, deselected):
        items = selected.indexes()
        for x in items:
            print(x.data())

    def enable_save(self, enable_state):
        self.ui.actionSave.setEnabled(enable_state)

    def enable_new(self, enable_state):
        self.ui.actionNew.setEnabled(enable_state)

    def enable_delete(self, enable_state):
        self.ui.actionDelete.setEnabled(enable_state)

    def get_current_view(self):
        """ returns the current view instance based on the currently selected tab index """
        view = None
        current_index = self.ui.tabWidget.currentIndex()
        if current_index >= 0 and current_index in self.tab_instances:
            view = self.tab_instances[current_index]
        return view


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

