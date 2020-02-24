# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'question_form.ui',
# licensing of 'question_form.ui' applies.
#
# Created: Mon Feb 24 10:25:48 2020
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(539, 471)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 319, 55, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 350, 24, 17))
        self.label_2.setObjectName("label_2")
        self.txtBody = QtWidgets.QLineEdit(Form)
        self.txtBody.setGeometry(QtCore.QRect(80, 320, 431, 25))
        self.txtBody.setObjectName("txtBody")
        self.txtAnswer = QtWidgets.QLineEdit(Form)
        self.txtAnswer.setGeometry(QtCore.QRect(80, 382, 421, 25))
        self.txtAnswer.setObjectName("txtAnswer")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 381, 46, 17))
        self.label_3.setObjectName("label_3")
        self.btnAdd = QtWidgets.QPushButton(Form)
        self.btnAdd.setGeometry(QtCore.QRect(429, 426, 80, 25))
        self.btnAdd.setObjectName("btnAdd")
        self.cboTags = QtWidgets.QComboBox(Form)
        self.cboTags.setGeometry(QtCore.QRect(80, 351, 201, 25))
        self.cboTags.setObjectName("cboTags")
        self.questionView = QtWidgets.QTableView(Form)
        self.questionView.setGeometry(QtCore.QRect(20, 40, 491, 261))
        self.questionView.setObjectName("questionView")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(30, 10, 91, 17))
        self.label_4.setObjectName("label_4")
        self.label_3.setBuddy(self.txtAnswer)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Form", "Question:", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Form", "Tag:", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("Form", "Answer:", None, -1))
        self.btnAdd.setText(QtWidgets.QApplication.translate("Form", "Add", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("Form", "Questions", None, -1))

