# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'question_form.ui'
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


class Ui_Form(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(664, 591)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lblHeader = QLabel(Form)
        self.lblHeader.setObjectName(u"lblHeader")

        self.verticalLayout_2.addWidget(self.lblHeader)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnSoundTest = QPushButton(Form)
        self.btnSoundTest.setObjectName(u"btnSoundTest")

        self.horizontalLayout.addWidget(self.btnSoundTest)

        self.btnDelete = QPushButton(Form)
        self.btnDelete.setObjectName(u"btnDelete")
        self.btnDelete.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout.addWidget(self.btnDelete)

        self.btnAdd = QPushButton(Form)
        self.btnAdd.setObjectName(u"btnAdd")
        self.btnAdd.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout.addWidget(self.btnAdd)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.questionView = QTableView(Form)
        self.questionView.setObjectName(u"questionView")
        self.questionView.setAlternatingRowColors(True)
        self.questionView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.questionView.horizontalHeader().setCascadingSectionResizes(True)
        self.questionView.horizontalHeader().setProperty("showSortIndicator", True)
        self.questionView.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout.addWidget(self.questionView)

        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.txtBody = QLineEdit(self.groupBox)
        self.txtBody.setObjectName(u"txtBody")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.txtBody)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.cboTags = QComboBox(self.groupBox)
        self.cboTags.setObjectName(u"cboTags")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.cboTags)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.txtAnswer = QPlainTextEdit(self.groupBox)
        self.txtAnswer.setObjectName(u"txtAnswer")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.txtAnswer)

        self.txtID = QLineEdit(self.groupBox)
        self.txtID.setObjectName(u"txtID")
        self.txtID.setEnabled(False)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.txtID)

        self.lblId = QLabel(self.groupBox)
        self.lblId.setObjectName(u"lblId")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.lblId)


        self.verticalLayout.addWidget(self.groupBox)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.btnSave = QPushButton(Form)
        self.btnSave.setObjectName(u"btnSave")
        self.btnSave.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_2.addWidget(self.btnSave)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lblHeader.setText(QCoreApplication.translate("Form", u"Questions", None))
        self.btnSoundTest.setText(QCoreApplication.translate("Form", u"Tests", None))
        self.btnDelete.setText(QCoreApplication.translate("Form", u"&Delete", None))
        self.btnAdd.setText(QCoreApplication.translate("Form", u"&Add", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Edit", None))
        self.label.setText(QCoreApplication.translate("Form", u"Question:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Tag:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Answer:", None))
        self.lblId.setText(QCoreApplication.translate("Form", u"ID", None))
        self.btnSave.setText(QCoreApplication.translate("Form", u"&Save", None))
    # retranslateUi

