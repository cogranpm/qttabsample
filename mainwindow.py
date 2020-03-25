# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1001, 666)
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionChristmas_Tree = QAction(MainWindow)
        self.actionChristmas_Tree.setObjectName(u"actionChristmas_Tree")
        self.actionDatabase_Test = QAction(MainWindow)
        self.actionDatabase_Test.setObjectName(u"actionDatabase_Test")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSave.setEnabled(False)
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        self.actionNew.setEnabled(False)
        self.actionDelete = QAction(MainWindow)
        self.actionDelete.setObjectName(u"actionDelete")
        self.actionDelete.setEnabled(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.frmNav = QFrame(self.splitter)
        self.frmNav.setObjectName(u"frmNav")
        self.frmNav.setFrameShape(QFrame.StyledPanel)
        self.frmNav.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frmNav)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.navTree = QTreeView(self.frmNav)
        self.navTree.setObjectName(u"navTree")

        self.verticalLayout_2.addWidget(self.navTree)

        self.splitter.addWidget(self.frmNav)
        self.frmMain = QFrame(self.splitter)
        self.frmMain.setObjectName(u"frmMain")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frmMain.sizePolicy().hasHeightForWidth())
        self.frmMain.setSizePolicy(sizePolicy)
        self.frmMain.setFrameShape(QFrame.StyledPanel)
        self.frmMain.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frmMain)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btnAddTab = QPushButton(self.frmMain)
        self.btnAddTab.setObjectName(u"btnAddTab")

        self.verticalLayout_3.addWidget(self.btnAddTab)

        self.tabWidget = QTabWidget(self.frmMain)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabsClosable(True)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tabWidget.addTab(self.tab, "")
        self.tabTest = QWidget()
        self.tabTest.setObjectName(u"tabTest")
        self.tabWidget.addTab(self.tabTest, "")

        self.verticalLayout_3.addWidget(self.tabWidget)

        self.splitter.addWidget(self.frmMain)

        self.verticalLayout.addWidget(self.splitter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1001, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuAction = QMenu(self.menubar)
        self.menuAction.setObjectName(u"menuAction")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAction.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionQuit)
        self.menuAction.addAction(self.actionDelete)
        self.menuAction.addAction(self.actionChristmas_Tree)
        self.menuAction.addAction(self.actionDatabase_Test)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addAction(self.actionNew)
        self.toolBar.addAction(self.actionDelete)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
#if QT_CONFIG(shortcut)
        self.actionQuit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionChristmas_Tree.setText(QCoreApplication.translate("MainWindow", u"Christmas Tree", None))
#if QT_CONFIG(shortcut)
        self.actionChristmas_Tree.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+X", None))
#endif // QT_CONFIG(shortcut)
        self.actionDatabase_Test.setText(QCoreApplication.translate("MainWindow", u"Database Test", None))
#if QT_CONFIG(shortcut)
        self.actionDatabase_Test.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+D", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"&Save", None))
#if QT_CONFIG(shortcut)
        self.actionSave.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
#if QT_CONFIG(tooltip)
        self.actionNew.setToolTip(QCoreApplication.translate("MainWindow", u"Add", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionNew.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.actionDelete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
#if QT_CONFIG(tooltip)
        self.actionDelete.setToolTip(QCoreApplication.translate("MainWindow", u"Delete", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionDelete.setShortcut(QCoreApplication.translate("MainWindow", u"Del", None))
#endif // QT_CONFIG(shortcut)
        self.btnAddTab.setText(QCoreApplication.translate("MainWindow", u"Add Tab", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Property", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabTest), QCoreApplication.translate("MainWindow", u"Loaded", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuAction.setTitle(QCoreApplication.translate("MainWindow", u"Action", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

