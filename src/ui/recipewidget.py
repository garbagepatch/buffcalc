# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'recipewidget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(900, 497)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.gridLayoutWidget_2 = QWidget(Form)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(0, 0, 852, 481))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.gridLayoutWidget_2)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setMinimumSize(QSize(454, 1))
        self.frame_2.setFrameShape(QFrame.Panel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setLineWidth(3)
        self.frame_2.setMidLineWidth(1)
        self.gridLayoutWidget_3 = QWidget(self.frame_2)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(0, 0, 451, 171))
        self.gridLayout_5 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(50, 0, 0, 0)
        self.comboBox_2 = QComboBox(self.gridLayoutWidget_3)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout_5.addWidget(self.comboBox_2, 0, 1, 1, 1)

        self.label_13 = QLabel(self.gridLayoutWidget_3)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_5.addWidget(self.label_13, 1, 0, 1, 1)

        self.label_14 = QLabel(self.gridLayoutWidget_3)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_5.addWidget(self.label_14, 2, 0, 1, 1)

        self.customAMW = QLineEdit(self.gridLayoutWidget_3)
        self.customAMW.setObjectName(u"customAMW")
        self.customAMW.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.customAMW.sizePolicy().hasHeightForWidth())
        self.customAMW.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setPointSize(12)
        self.customAMW.setFont(font)
        self.customAMW.setStyleSheet(u"hidden: true")
        self.customAMW.setInputMethodHints(Qt.ImhNone)

        self.gridLayout_5.addWidget(self.customAMW, 2, 1, 1, 1)

        self.customHAMW = QLineEdit(self.gridLayoutWidget_3)
        self.customHAMW.setObjectName(u"customHAMW")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.customHAMW.sizePolicy().hasHeightForWidth())
        self.customHAMW.setSizePolicy(sizePolicy3)
        self.customHAMW.setFont(font)

        self.gridLayout_5.addWidget(self.customHAMW, 1, 1, 1, 1)

        self.label_15 = QLabel(self.gridLayoutWidget_3)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_5.addWidget(self.label_15, 0, 0, 1, 1)

        self.checkBox = QCheckBox(self.gridLayoutWidget_3)
        self.checkBox.setObjectName(u"checkBox")
        sizePolicy3.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy3)
        self.checkBox.setFont(font)

        self.gridLayout_5.addWidget(self.checkBox, 0, 2, 1, 1)


        self.gridLayout_4.addWidget(self.frame_2, 0, 1, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_16 = QLabel(self.gridLayoutWidget_2)
        self.label_16.setObjectName(u"label_16")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy4)
        font1 = QFont()
        font1.setPointSize(20)
        self.label_16.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_16)

        self.line_5 = QFrame(self.gridLayoutWidget_2)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setMinimumSize(QSize(5, 5))
        self.line_5.setSizeIncrement(QSize(5, 5))
        self.line_5.setBaseSize(QSize(5, 5))
        font2 = QFont()
        font2.setPointSize(24)
        self.line_5.setFont(font2)
        self.line_5.setFrameShadow(QFrame.Sunken)
        self.line_5.setLineWidth(3)
        self.line_5.setMidLineWidth(2)
        self.line_5.setFrameShape(QFrame.HLine)

        self.verticalLayout_3.addWidget(self.line_5)

        self.label_17 = QLabel(self.gridLayoutWidget_2)
        self.label_17.setObjectName(u"label_17")
        sizePolicy4.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy4)
        self.label_17.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.label_17)


        self.gridLayout_4.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.frame_3 = QFrame(self.gridLayoutWidget_2)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy4.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy4)
        self.frame_3.setFrameShape(QFrame.Panel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_3.setLineWidth(3)
        self.frame_3.setMidLineWidth(1)
        self.gridLayoutWidget_4 = QWidget(self.frame_3)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(0, 0, 451, 301))
        self.gridLayout_6 = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_6.setContentsMargins(10, 0, 0, 0)
        self.haResultsLabel = QLabel(self.gridLayoutWidget_4)
        self.haResultsLabel.setObjectName(u"haResultsLabel")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.haResultsLabel.sizePolicy().hasHeightForWidth())
        self.haResultsLabel.setSizePolicy(sizePolicy5)
        self.haResultsLabel.setFont(font)
        self.haResultsLabel.setScaledContents(True)
        self.haResultsLabel.setAlignment(Qt.AlignCenter)
        self.haResultsLabel.setWordWrap(True)

        self.gridLayout_6.addWidget(self.haResultsLabel, 0, 0, 1, 1)

        self.haResults = QLineEdit(self.gridLayoutWidget_4)
        self.haResults.setObjectName(u"haResults")
        sizePolicy2.setHeightForWidth(self.haResults.sizePolicy().hasHeightForWidth())
        self.haResults.setSizePolicy(sizePolicy2)
        self.haResults.setMaximumSize(QSize(150, 16777215))
        self.haResults.setFont(font)
        self.haResults.setInputMethodHints(Qt.ImhDigitsOnly)
        self.haResults.setMaxLength(6)
        self.haResults.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.haResults, 0, 1, 1, 1)

        self.aResults = QLineEdit(self.gridLayoutWidget_4)
        self.aResults.setObjectName(u"aResults")
        self.aResults.setMaximumSize(QSize(150, 16777215))
        self.aResults.setFont(font)
        self.aResults.setInputMethodHints(Qt.ImhDigitsOnly)
        self.aResults.setMaxLength(6)
        self.aResults.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.aResults, 1, 1, 1, 1)

        self.aResultsLabel = QLabel(self.gridLayoutWidget_4)
        self.aResultsLabel.setObjectName(u"aResultsLabel")
        self.aResultsLabel.setFont(font)
        self.aResultsLabel.setScaledContents(True)
        self.aResultsLabel.setAlignment(Qt.AlignCenter)
        self.aResultsLabel.setWordWrap(True)

        self.gridLayout_6.addWidget(self.aResultsLabel, 1, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame_3, 2, 1, 1, 1)

        self.frame = QFrame(self.gridLayoutWidget_2)
        self.frame.setObjectName(u"frame")
        sizePolicy3.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy3)
        self.frame.setMinimumSize(QSize(0, 300))
        self.frame.setMaximumSize(QSize(500, 16777215))
        self.frame.setFrameShape(QFrame.Panel)
        self.frame.setFrameShadow(QFrame.Sunken)
        self.frame.setLineWidth(3)
        self.frame.setMidLineWidth(1)
        self.formLayoutWidget = QWidget(self.frame)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(0, 0, 401, 301))
        self.formLayout_3 = QFormLayout(self.formLayoutWidget)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setLabelAlignment(Qt.AlignCenter)
        self.formLayout_3.setFormAlignment(Qt.AlignCenter)
        self.formLayout_3.setHorizontalSpacing(20)
        self.formLayout_3.setVerticalSpacing(20)
        self.formLayout_3.setContentsMargins(10, 10, 20, 10)
        self.initialAmountHALabel = QLabel(self.formLayoutWidget)
        self.initialAmountHALabel.setObjectName(u"initialAmountHALabel")
        self.initialAmountHALabel.setFont(font)

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.initialAmountHALabel)

        self.initialAmountHALineEdit = QLineEdit(self.formLayoutWidget)
        self.initialAmountHALineEdit.setObjectName(u"initialAmountHALineEdit")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.initialAmountHALineEdit.sizePolicy().hasHeightForWidth())
        self.initialAmountHALineEdit.setSizePolicy(sizePolicy6)
        self.initialAmountHALineEdit.setMaximumSize(QSize(100, 16777215))
        self.initialAmountHALineEdit.setFont(font)
        self.initialAmountHALineEdit.setInputMethodHints(Qt.ImhDigitsOnly)
        self.initialAmountHALineEdit.setMaxLength(6)
        self.initialAmountHALineEdit.setAlignment(Qt.AlignCenter)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.initialAmountHALineEdit)

        self.initialAmountALabel = QLabel(self.formLayoutWidget)
        self.initialAmountALabel.setObjectName(u"initialAmountALabel")
        self.initialAmountALabel.setFont(font)

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.initialAmountALabel)

        self.initialAmountALineEdit = QLineEdit(self.formLayoutWidget)
        self.initialAmountALineEdit.setObjectName(u"initialAmountALineEdit")
        sizePolicy6.setHeightForWidth(self.initialAmountALineEdit.sizePolicy().hasHeightForWidth())
        self.initialAmountALineEdit.setSizePolicy(sizePolicy6)
        self.initialAmountALineEdit.setMaximumSize(QSize(100, 16777215))
        self.initialAmountALineEdit.setFont(font)
        self.initialAmountALineEdit.setInputMethodHints(Qt.ImhDigitsOnly)
        self.initialAmountALineEdit.setMaxLength(6)
        self.initialAmountALineEdit.setAlignment(Qt.AlignCenter)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.initialAmountALineEdit)

        self.measuredPHLabel = QLabel(self.formLayoutWidget)
        self.measuredPHLabel.setObjectName(u"measuredPHLabel")
        self.measuredPHLabel.setFont(font)

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.measuredPHLabel)

        self.measuredPHLineEdit = QLineEdit(self.formLayoutWidget)
        self.measuredPHLineEdit.setObjectName(u"measuredPHLineEdit")
        sizePolicy6.setHeightForWidth(self.measuredPHLineEdit.sizePolicy().hasHeightForWidth())
        self.measuredPHLineEdit.setSizePolicy(sizePolicy6)
        self.measuredPHLineEdit.setMaximumSize(QSize(100, 16777215))
        self.measuredPHLineEdit.setFont(font)
        self.measuredPHLineEdit.setInputMethodHints(Qt.ImhDigitsOnly)
        self.measuredPHLineEdit.setMaxLength(6)
        self.measuredPHLineEdit.setAlignment(Qt.AlignCenter)

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.measuredPHLineEdit)

        self.targetPLabel = QLabel(self.formLayoutWidget)
        self.targetPLabel.setObjectName(u"targetPLabel")
        self.targetPLabel.setFont(font)

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.targetPLabel)

        self.targetpHLineEdit = QLineEdit(self.formLayoutWidget)
        self.targetpHLineEdit.setObjectName(u"targetpHLineEdit")
        sizePolicy6.setHeightForWidth(self.targetpHLineEdit.sizePolicy().hasHeightForWidth())
        self.targetpHLineEdit.setSizePolicy(sizePolicy6)
        self.targetpHLineEdit.setMaximumSize(QSize(100, 16777215))
        self.targetpHLineEdit.setFont(font)
        self.targetpHLineEdit.setInputMethodHints(Qt.ImhDigitsOnly)
        self.targetpHLineEdit.setMaxLength(6)
        self.targetpHLineEdit.setAlignment(Qt.AlignCenter)

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.targetpHLineEdit)

        self.molarityOfBufferLabel = QLabel(self.formLayoutWidget)
        self.molarityOfBufferLabel.setObjectName(u"molarityOfBufferLabel")
        self.molarityOfBufferLabel.setFont(font)

        self.formLayout_3.setWidget(4, QFormLayout.LabelRole, self.molarityOfBufferLabel)

        self.molarityOfBufferLineEdit = QLineEdit(self.formLayoutWidget)
        self.molarityOfBufferLineEdit.setObjectName(u"molarityOfBufferLineEdit")
        sizePolicy6.setHeightForWidth(self.molarityOfBufferLineEdit.sizePolicy().hasHeightForWidth())
        self.molarityOfBufferLineEdit.setSizePolicy(sizePolicy6)
        self.molarityOfBufferLineEdit.setMaximumSize(QSize(100, 16777215))
        self.molarityOfBufferLineEdit.setFont(font)
        self.molarityOfBufferLineEdit.setInputMethodHints(Qt.ImhDigitsOnly)
        self.molarityOfBufferLineEdit.setMaxLength(6)
        self.molarityOfBufferLineEdit.setAlignment(Qt.AlignCenter)

        self.formLayout_3.setWidget(4, QFormLayout.FieldRole, self.molarityOfBufferLineEdit)

        self.calculateButton = QPushButton(self.formLayoutWidget)
        self.calculateButton.setObjectName(u"calculateButton")
        sizePolicy6.setHeightForWidth(self.calculateButton.sizePolicy().hasHeightForWidth())
        self.calculateButton.setSizePolicy(sizePolicy6)
        self.calculateButton.setMaximumSize(QSize(100, 16777215))
        self.calculateButton.setAutoDefault(True)
        self.calculateButton.setFlat(False)

        self.formLayout_3.setWidget(5, QFormLayout.FieldRole, self.calculateButton)


        self.gridLayout_4.addWidget(self.frame, 2, 0, 1, 1)

        self.gridLayout_4.setRowStretch(2, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"HA MW", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"A MW", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"Buffer Selection", None))
        self.checkBox.setText(QCoreApplication.translate("Form", u"Custom", None))
        self.label_16.setText(QCoreApplication.translate("Form", u" Fix Broken Recipes", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"       If you want to repair a recipe so that you no longer need to titrate it, use this tool. The logic underneath is that if you are just changing the amounts of conjugates to adjust for the pH, then all else being equal the equation becomes the henderson-hasselbach equation and is easily solvable.l", None))
        self.haResultsLabel.setText(QCoreApplication.translate("Form", u"Corrected HA in (g/L)", None))
        self.aResultsLabel.setText(QCoreApplication.translate("Form", u"Corrected A in (g/L)", None))
        self.initialAmountHALabel.setText(QCoreApplication.translate("Form", u"Initial Amount HA", None))
        self.initialAmountHALineEdit.setText(QCoreApplication.translate("Form", u"0.000", None))
        self.initialAmountHALineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"0.00", None))
        self.initialAmountALabel.setText(QCoreApplication.translate("Form", u"Initial Amount A", None))
        self.initialAmountALineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"0.00", None))
        self.measuredPHLabel.setText(QCoreApplication.translate("Form", u"Measured pH", None))
        self.measuredPHLineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"0.00", None))
        self.targetPLabel.setText(QCoreApplication.translate("Form", u"Target pH", None))
        self.targetpHLineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"0.00", None))
        self.molarityOfBufferLabel.setText(QCoreApplication.translate("Form", u"Molarity of Buffer", None))
        self.molarityOfBufferLineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"0.00", None))
        self.calculateButton.setText(QCoreApplication.translate("Form", u"Calculate", None))
    # retranslateUi

