# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tab_page.ui',
# licensing of 'tab_page.ui' applies.
#
# Created: Thu Jun 27 12:27:28 2019
#      by: pyside2-uic  running on PySide2 5.12.4
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_TabPage(object):
    def setupUi(self, TabPage):
        TabPage.setObjectName("TabPage")
        TabPage.resize(696, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(TabPage)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtWidgets.QSplitter(TabPage)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.treeWidget = QtWidgets.QTreeWidget(self.splitter)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.groupBox = QtWidgets.QGroupBox(self.splitter)
        self.groupBox.setObjectName("groupBox")
        self.btnTest = QtWidgets.QPushButton(self.groupBox)
        self.btnTest.setGeometry(QtCore.QRect(20, 40, 88, 27))
        self.btnTest.setObjectName("btnTest")
        self.verticalLayout.addWidget(self.splitter)

        self.retranslateUi(TabPage)
        QtCore.QMetaObject.connectSlotsByName(TabPage)

    def retranslateUi(self, TabPage):
        TabPage.setWindowTitle(QtWidgets.QApplication.translate("TabPage", "Form", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("TabPage", "GroupBox", None, -1))
        self.btnTest.setText(QtWidgets.QApplication.translate("TabPage", "Test", None, -1))

