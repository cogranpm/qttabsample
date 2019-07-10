# This Python file uses the following encoding: utf-8
import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtGui import QStandardItemModel, QStandardItem, QIcon
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

        # model view approach for a tree, using a default QStandardItemModel so far
        # could implement QAbstractItemModel interface instead
        self.navModel = QStandardItemModel()
        self.navModel.setHorizontalHeaderItem(0, QStandardItem("Name"))
        parent_item = self.navModel.invisibleRootItem()

        itemfrank = QStandardItem("Frank")
        itemfrank.setIcon(QIcon("icons/braindump.png"))
        parent_item.appendRow(itemfrank)

        nigel_item = QStandardItem("Nigel")
        nigel_item.setIcon(QIcon("icons/braindump.png"))
        parent_item.appendRow(nigel_item)

        nigel_sub_item = QStandardItem("passport")
        nigel_sub_item.setIcon(QIcon("icons/braindump.png"))

        nigel_item.appendRow(nigel_sub_item)

        # view, navTree holds model instance, navModel
        # self.ui.navTree.setModel(self.navModel)
        self.ui.navTree.setModel(NavigationModel())
        self.ui.navTree.setSortingEnabled(False)
        #self.ui.navTree.show()


    def addTabClick(self):
        self.ui.tabWidget.addTab(TabSample(), "New")


if __name__ == "__main__":
    try:
        app = QApplication([])
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())
    except Exception:
        print ("error in main")
        pass
