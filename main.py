# This Python file uses the following encoding: utf-8
import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtGui import QStandardItemModel, QStandardItem, QIcon
from PySide2.QtCore import QItemSelectionModel
from mainwindow import Ui_MainWindow
from tabsample import TabSample
from models import NavigationItem, NavigationModel

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnAddTab.clicked.connect(self.addTabClick)
        self.ui.actionQuit.triggered.connect(QApplication.quit)



        # view, navTree holds model instance, navModel
        # self.ui.navTree.setModel(self.navModel)
        self.ui.navTree.setModel(NavigationModel())
        self.ui.navTree.setSortingEnabled(False)
        self.selection_model = self.ui.navTree.selectionModel()
        self.selection_model.selectionChanged.connect(self.navigationselected)

        #self.ui.navTree.show()


    def addTabClick(self):
        self.ui.tabWidget.addTab(TabSample(), "New")

    def navigationselected(self, selected, deselected):
        print(selected)
        print(self.selection_model.selectedIndexes())


if __name__ == "__main__":
    try:
        app = QApplication([])
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())
    except Exception:
        print ("error in main")
        pass
