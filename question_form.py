# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'question_form.ui',
# licensing of 'question_form.ui' applies.
#
# Created: Mon Feb 24 22:10:08 2020
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(664, 591)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.btnAdd = QtWidgets.QPushButton(Form)
        self.btnAdd.setObjectName("btnAdd")
        self.verticalLayout_2.addWidget(self.btnAdd)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.questionView = QtWidgets.QTableView(Form)
        self.questionView.setAlternatingRowColors(True)
        self.questionView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.questionView.setObjectName("questionView")
        self.verticalLayout.addWidget(self.questionView)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.txtBody = QtWidgets.QLineEdit(self.groupBox)
        self.txtBody.setObjectName("txtBody")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txtBody)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.cboTags = QtWidgets.QComboBox(self.groupBox)
        self.cboTags.setObjectName("cboTags")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.cboTags)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.txtAnswer = QtWidgets.QPlainTextEdit(self.groupBox)
        self.txtAnswer.setObjectName("txtAnswer")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txtAnswer)
        self.verticalLayout.addWidget(self.groupBox)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.txtID = QtWidgets.QLineEdit(Form)
        self.txtID.setObjectName("txtID")
        self.verticalLayout_2.addWidget(self.txtID)
        self.btnSave = QtWidgets.QPushButton(Form)
        self.btnSave.setObjectName("btnSave")
        self.verticalLayout_2.addWidget(self.btnSave)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("Form", "Questions", None, -1))
        self.btnAdd.setText(QtWidgets.QApplication.translate("Form", "Add", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("Form", "Edit", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Form", "Question:", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Form", "Tag:", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("Form", "Answer:", None, -1))
        self.btnSave.setText(QtWidgets.QApplication.translate("Form", "Save", None, -1))

