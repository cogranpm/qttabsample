# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'question_form.ui',
# licensing of 'question_form.ui' applies.
#
# Created: Mon Feb  3 11:07:49 2020
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(539, 471)
        self.listView = QtWidgets.QListView(Form)
        self.listView.setGeometry(QtCore.QRect(20, 10, 256, 188))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.listView.sizePolicy().hasHeightForWidth())
        self.listView.setSizePolicy(sizePolicy)
        self.listView.setObjectName("listView")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(21, 203, 55, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(21, 234, 24, 17))
        self.label_2.setObjectName("label_2")
        self.txtBody = QtWidgets.QLineEdit(Form)
        self.txtBody.setGeometry(QtCore.QRect(82, 203, 441, 25))
        self.txtBody.setObjectName("txtBody")
        self.txtTag = QtWidgets.QLineEdit(Form)
        self.txtTag.setGeometry(QtCore.QRect(82, 234, 108, 25))
        self.txtTag.setObjectName("txtTag")
        self.txtAnswer = QtWidgets.QLineEdit(Form)
        self.txtAnswer.setGeometry(QtCore.QRect(82, 265, 441, 25))
        self.txtAnswer.setObjectName("txtAnswer")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(21, 265, 46, 17))
        self.label_3.setObjectName("label_3")
        self.btnAdd = QtWidgets.QPushButton(Form)
        self.btnAdd.setGeometry(QtCore.QRect(430, 310, 80, 25))
        self.btnAdd.setObjectName("btnAdd")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Form", "Question:", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Form", "Tag:", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("Form", "Answer:", None, -1))
        self.btnAdd.setText(QtWidgets.QApplication.translate("Form", "Add", None, -1))

