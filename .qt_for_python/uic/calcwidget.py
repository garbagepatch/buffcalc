# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calcwidget.ui'
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
        Form.resize(1082, 481)
        self.gridLayoutWidget = QWidget(Form)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 1071, 451))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setHorizontalSpacing(100)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.line_3 = QFrame(self.gridLayoutWidget)
        self.line_3.setObjectName(u"line_3")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_3.sizePolicy().hasHeightForWidth())
        self.line_3.setSizePolicy(sizePolicy)
        self.line_3.setMinimumSize(QSize(0, 10))
        self.line_3.setFrameShadow(QFrame.Plain)
        self.line_3.setLineWidth(2)
        self.line_3.setMidLineWidth(1)
        self.line_3.setFrameShape(QFrame.HLine)

        self.gridLayout.addWidget(self.line_3, 7, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.formLayout.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setLabelAlignment(Qt.AlignCenter)
        self.formLayout.setFormAlignment(Qt.AlignCenter)
        self.formLayout.setVerticalSpacing(15)
        self.formLayout.setContentsMargins(-1, 5, 5, 5)
        self.bufferTypeLabel = QLabel(self.gridLayoutWidget)
        self.bufferTypeLabel.setObjectName(u"bufferTypeLabel")
        font = QFont()
        font.setPointSize(12)
        self.bufferTypeLabel.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.bufferTypeLabel)

        self.bufferTypeComboBox = QComboBox(self.gridLayoutWidget)
        self.bufferTypeComboBox.setObjectName(u"bufferTypeComboBox")
        self.bufferTypeComboBox.setFont(font)
        self.bufferTypeComboBox.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.bufferTypeComboBox)

        self.totalBufferMolarityLabel = QLabel(self.gridLayoutWidget)
        self.totalBufferMolarityLabel.setObjectName(u"totalBufferMolarityLabel")
        self.totalBufferMolarityLabel.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.totalBufferMolarityLabel)

        self.totalBufferMolarityLineEdit = QLineEdit(self.gridLayoutWidget)
        self.totalBufferMolarityLineEdit.setObjectName(u"totalBufferMolarityLineEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.totalBufferMolarityLineEdit.sizePolicy().hasHeightForWidth())
        self.totalBufferMolarityLineEdit.setSizePolicy(sizePolicy1)
        self.totalBufferMolarityLineEdit.setFont(font)
        self.totalBufferMolarityLineEdit.setInputMethodHints(Qt.ImhDigitsOnly)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.totalBufferMolarityLineEdit)

        self.sodiumChlorideMolarityLabel_2 = QLabel(self.gridLayoutWidget)
        self.sodiumChlorideMolarityLabel_2.setObjectName(u"sodiumChlorideMolarityLabel_2")
        self.sodiumChlorideMolarityLabel_2.setFont(font)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.sodiumChlorideMolarityLabel_2)

        self.sodiumChlorideMolarityLineEdit = QLineEdit(self.gridLayoutWidget)
        self.sodiumChlorideMolarityLineEdit.setObjectName(u"sodiumChlorideMolarityLineEdit")
        sizePolicy1.setHeightForWidth(self.sodiumChlorideMolarityLineEdit.sizePolicy().hasHeightForWidth())
        self.sodiumChlorideMolarityLineEdit.setSizePolicy(sizePolicy1)
        self.sodiumChlorideMolarityLineEdit.setFont(font)
        self.sodiumChlorideMolarityLineEdit.setInputMethodHints(Qt.ImhDigitsOnly)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.sodiumChlorideMolarityLineEdit)

        self.targetPHLabel = QLabel(self.gridLayoutWidget)
        self.targetPHLabel.setObjectName(u"targetPHLabel")
        self.targetPHLabel.setFont(font)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.targetPHLabel)

        self.targetPHLineEdit = QLineEdit(self.gridLayoutWidget)
        self.targetPHLineEdit.setObjectName(u"targetPHLineEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.targetPHLineEdit.sizePolicy().hasHeightForWidth())
        self.targetPHLineEdit.setSizePolicy(sizePolicy2)
        self.targetPHLineEdit.setFont(font)
        self.targetPHLineEdit.setInputMethodHints(Qt.ImhDigitsOnly)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.targetPHLineEdit)

        self.targetTemperatureLabel = QLabel(self.gridLayoutWidget)
        self.targetTemperatureLabel.setObjectName(u"targetTemperatureLabel")
        self.targetTemperatureLabel.setFont(font)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.targetTemperatureLabel)

        self.targetTemperatureLineEdit = QLineEdit(self.gridLayoutWidget)
        self.targetTemperatureLineEdit.setObjectName(u"targetTemperatureLineEdit")
        sizePolicy1.setHeightForWidth(self.targetTemperatureLineEdit.sizePolicy().hasHeightForWidth())
        self.targetTemperatureLineEdit.setSizePolicy(sizePolicy1)
        self.targetTemperatureLineEdit.setFont(font)
        self.targetTemperatureLineEdit.setInputMethodHints(Qt.ImhDigitsOnly)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.targetTemperatureLineEdit)

        self.Calculate = QPushButton(self.gridLayoutWidget)
        self.Calculate.setObjectName(u"Calculate")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.Calculate.sizePolicy().hasHeightForWidth())
        self.Calculate.setSizePolicy(sizePolicy3)
        self.Calculate.setMinimumSize(QSize(20, 0))
        self.Calculate.setMaximumSize(QSize(177, 16777215))
        font1 = QFont()
        font1.setPointSize(13)
        self.Calculate.setFont(font1)
        self.Calculate.setFlat(False)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.Calculate)


        self.verticalLayout_2.addLayout(self.formLayout)


        self.gridLayout.addLayout(self.verticalLayout_2, 3, 0, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        font2 = QFont()
        font2.setPointSize(20)
        self.label_4.setFont(font2)
        self.label_4.setFrameShape(QFrame.NoFrame)
        self.label_4.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)
        self.label_6.setFrameShape(QFrame.NoFrame)
        self.label_6.setFrameShadow(QFrame.Raised)
        self.label_6.setScaledContents(True)
        self.label_6.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.gridLayout.addWidget(self.label_6, 5, 1, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy4 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy4)
        self.label_3.setFont(font2)
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)

        self.line_4 = QFrame(self.gridLayoutWidget)
        self.line_4.setObjectName(u"line_4")
        sizePolicy.setHeightForWidth(self.line_4.sizePolicy().hasHeightForWidth())
        self.line_4.setSizePolicy(sizePolicy)
        self.line_4.setMinimumSize(QSize(0, 10))
        self.line_4.setFrameShadow(QFrame.Plain)
        self.line_4.setLineWidth(2)
        self.line_4.setMidLineWidth(1)
        self.line_4.setFrameShape(QFrame.HLine)

        self.gridLayout.addWidget(self.line_4, 7, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setSpacing(50)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetMinimumSize)
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.haResultBox = QLineEdit(self.gridLayoutWidget)
        self.haResultBox.setObjectName(u"haResultBox")
        sizePolicy4.setHeightForWidth(self.haResultBox.sizePolicy().hasHeightForWidth())
        self.haResultBox.setSizePolicy(sizePolicy4)
        self.haResultBox.setMinimumSize(QSize(0, 0))
        self.haResultBox.setMaximumSize(QSize(100, 16777215))
        self.haResultBox.setFont(font)
        self.haResultBox.setMaxLength(8)
        self.haResultBox.setAlignment(Qt.AlignCenter)
        self.haResultBox.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.haResultBox)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setFont(font)
        self.label.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.label)


        self.gridLayout_2.addLayout(self.horizontalLayout_4, 0, 1, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetMinimumSize)
        self.aResultBox = QLineEdit(self.gridLayoutWidget)
        self.aResultBox.setObjectName(u"aResultBox")
        sizePolicy4.setHeightForWidth(self.aResultBox.sizePolicy().hasHeightForWidth())
        self.aResultBox.setSizePolicy(sizePolicy4)
        self.aResultBox.setMinimumSize(QSize(0, 0))
        self.aResultBox.setMaximumSize(QSize(100, 16777215))
        self.aResultBox.setFont(font)
        self.aResultBox.setMaxLength(7)
        self.aResultBox.setAlignment(Qt.AlignCenter)
        self.aResultBox.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.aResultBox)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setFont(font)
        self.label_2.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.horizontalLayout_3.setStretch(0, 5)
        self.horizontalLayout_3.setStretch(1, 1)

        self.gridLayout_2.addLayout(self.horizontalLayout_3, 1, 1, 1, 1)

        self.haChoiceCombo = QComboBox(self.gridLayoutWidget)
        self.haChoiceCombo.setObjectName(u"haChoiceCombo")
        sizePolicy2.setHeightForWidth(self.haChoiceCombo.sizePolicy().hasHeightForWidth())
        self.haChoiceCombo.setSizePolicy(sizePolicy2)
        self.haChoiceCombo.setFont(font)

        self.gridLayout_2.addWidget(self.haChoiceCombo, 0, 0, 1, 1)

        self.aChoiceCombo = QComboBox(self.gridLayoutWidget)
        self.aChoiceCombo.setObjectName(u"aChoiceCombo")
        self.aChoiceCombo.setFont(font)
        self.aChoiceCombo.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.gridLayout_2.addWidget(self.aChoiceCombo, 1, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setSizeConstraint(QLayout.SetMinimumSize)
        self.aResultBox_2 = QLineEdit(self.gridLayoutWidget)
        self.aResultBox_2.setObjectName(u"aResultBox_2")
        sizePolicy4.setHeightForWidth(self.aResultBox_2.sizePolicy().hasHeightForWidth())
        self.aResultBox_2.setSizePolicy(sizePolicy4)
        self.aResultBox_2.setMinimumSize(QSize(0, 0))
        self.aResultBox_2.setMaximumSize(QSize(100, 16777215))
        self.aResultBox_2.setFont(font)
        self.aResultBox_2.setMaxLength(7)
        self.aResultBox_2.setAlignment(Qt.AlignCenter)
        self.aResultBox_2.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.aResultBox_2)

        self.label_8 = QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName(u"label_8")
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setFont(font)
        self.label_8.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.label_8)

        self.horizontalLayout_5.setStretch(0, 5)
        self.horizontalLayout_5.setStretch(1, 1)

        self.gridLayout_2.addLayout(self.horizontalLayout_5, 2, 1, 1, 1)

        self.sodiumChlorideMolarityLabel = QLabel(self.gridLayoutWidget)
        self.sodiumChlorideMolarityLabel.setObjectName(u"sodiumChlorideMolarityLabel")
        self.sodiumChlorideMolarityLabel.setFont(font)

        self.gridLayout_2.addWidget(self.sodiumChlorideMolarityLabel, 2, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.horizontalSpacer = QSpacerItem(40, 5, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.gridLayout.addLayout(self.horizontalLayout, 3, 1, 1, 1)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setFieldGrowthPolicy(QFormLayout.FieldsStayAtSizeHint)
        self.formLayout_2.setFormAlignment(Qt.AlignCenter)
        self.formLayout_2.setHorizontalSpacing(20)
        self.formLayout_2.setVerticalSpacing(0)
        self.formLayout_2.setContentsMargins(0, 0, 20, 0)
        self.conductivityMSCmLabel = QLabel(self.gridLayoutWidget)
        self.conductivityMSCmLabel.setObjectName(u"conductivityMSCmLabel")
        self.conductivityMSCmLabel.setFont(font)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.conductivityMSCmLabel)

        self.conductivityMSCmLineEdit = QLineEdit(self.gridLayoutWidget)
        self.conductivityMSCmLineEdit.setObjectName(u"conductivityMSCmLineEdit")
        sizePolicy4.setHeightForWidth(self.conductivityMSCmLineEdit.sizePolicy().hasHeightForWidth())
        self.conductivityMSCmLineEdit.setSizePolicy(sizePolicy4)
        self.conductivityMSCmLineEdit.setFont(font)
        self.conductivityMSCmLineEdit.setMaxLength(5)
        self.conductivityMSCmLineEdit.setReadOnly(True)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.conductivityMSCmLineEdit)


        self.gridLayout.addLayout(self.formLayout_2, 8, 0, 1, 1)

        self.line = QFrame(self.gridLayoutWidget)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(0, 10))
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setLineWidth(2)
        self.line.setMidLineWidth(1)
        self.line.setFrameShape(QFrame.HLine)

        self.gridLayout.addWidget(self.line, 2, 0, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(20)
        self.gridLayout_3.setVerticalSpacing(6)
        self.titrantEdit = QLineEdit(self.gridLayoutWidget)
        self.titrantEdit.setObjectName(u"titrantEdit")
        sizePolicy3.setHeightForWidth(self.titrantEdit.sizePolicy().hasHeightForWidth())
        self.titrantEdit.setSizePolicy(sizePolicy3)
        self.titrantEdit.setMinimumSize(QSize(100, 0))
        self.titrantEdit.setMaximumSize(QSize(100, 16777215))
        self.titrantEdit.setFont(font)
        self.titrantEdit.setInputMethodHints(Qt.ImhDigitsOnly)

        self.gridLayout_3.addWidget(self.titrantEdit, 0, 1, 1, 1)

        self.bufferEdit = QLineEdit(self.gridLayoutWidget)
        self.bufferEdit.setObjectName(u"bufferEdit")
        sizePolicy3.setHeightForWidth(self.bufferEdit.sizePolicy().hasHeightForWidth())
        self.bufferEdit.setSizePolicy(sizePolicy3)
        self.bufferEdit.setMinimumSize(QSize(100, 0))
        self.bufferEdit.setMaximumSize(QSize(50, 16777215))
        self.bufferEdit.setFont(font)
        self.bufferEdit.setInputMethodHints(Qt.ImhDigitsOnly)

        self.gridLayout_3.addWidget(self.bufferEdit, 1, 1, 1, 1)

        self.comboBox = QComboBox(self.gridLayoutWidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy1.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy1)
        self.comboBox.setFont(font)

        self.gridLayout_3.addWidget(self.comboBox, 0, 0, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 0, 2, 1, 1)

        self.titratename = QLabel(self.gridLayoutWidget)
        self.titratename.setObjectName(u"titratename")

        self.gridLayout_3.addWidget(self.titratename, 1, 2, 1, 1)

        self.buffercomp = QLabel(self.gridLayoutWidget)
        self.buffercomp.setObjectName(u"buffercomp")
        self.buffercomp.setFont(font)
        self.buffercomp.setScaledContents(True)

        self.gridLayout_3.addWidget(self.buffercomp, 1, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_3, 8, 1, 1, 1)

        self.label_9 = QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 1, 0, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)
        self.label_5.setFrameShape(QFrame.NoFrame)
        self.label_5.setFrameShadow(QFrame.Raised)
        self.label_5.setScaledContents(True)
        self.label_5.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)

        self.line_2 = QFrame(self.gridLayoutWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setMinimumSize(QSize(0, 10))
        self.line_2.setFrameShadow(QFrame.Plain)
        self.line_2.setLineWidth(2)
        self.line_2.setMidLineWidth(1)
        self.line_2.setFrameShape(QFrame.HLine)

        self.gridLayout.addWidget(self.line_2, 2, 1, 1, 1)

        self.label_10 = QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 6, 0, 1, 1)

        self.label_11 = QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 1, 1, 1, 1)

        self.label_12 = QLabel(self.gridLayoutWidget)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 6, 1, 1, 1)


        self.retranslateUi(Form)

        self.Calculate.setDefault(False)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.bufferTypeLabel.setText(QCoreApplication.translate("Form", u"Buffer Type", None))
        self.totalBufferMolarityLabel.setText(QCoreApplication.translate("Form", u"Total Buffer Molarity", None))
        self.sodiumChlorideMolarityLabel_2.setText(QCoreApplication.translate("Form", u"Sodium Chloride Molarity", None))
        self.targetPHLabel.setText(QCoreApplication.translate("Form", u"Target pH ", None))
        self.targetTemperatureLabel.setText(QCoreApplication.translate("Form", u"Target Temperature (C)", None))
        self.targetTemperatureLineEdit.setText(QCoreApplication.translate("Form", u"25.0", None))
        self.Calculate.setText(QCoreApplication.translate("Form", u"Calculate", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Target Buffer Selection", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"With Strong Acid or Base", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Results and Component Selection", None))
        self.haResultBox.setText(QCoreApplication.translate("Form", u"0.0000", None))
        self.label.setText(QCoreApplication.translate("Form", u"g/L", None))
        self.aResultBox.setText(QCoreApplication.translate("Form", u"0.0000", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"g/L", None))
        self.haChoiceCombo.setCurrentText("")
        self.haChoiceCombo.setPlaceholderText(QCoreApplication.translate("Form", u"Acidic Component", None))
        self.aChoiceCombo.setPlaceholderText(QCoreApplication.translate("Form", u"Basic Component", None))
        self.aResultBox_2.setText(QCoreApplication.translate("Form", u"0.0000", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"g/L", None))
        self.sodiumChlorideMolarityLabel.setText(QCoreApplication.translate("Form", u"Sodium Chloride", None))
        self.conductivityMSCmLabel.setText(QCoreApplication.translate("Form", u"Conductivity (mS/cm)", None))
        self.titrantEdit.setText(QCoreApplication.translate("Form", u"0.000", None))
        self.bufferEdit.setText(QCoreApplication.translate("Form", u"0.000", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"10N Sodium Hydroxide", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"6N Hydrochloric Acid", None))

        self.label_7.setText(QCoreApplication.translate("Form", u"mL", None))
        self.titratename.setText(QCoreApplication.translate("Form", u"g/L", None))
        self.buffercomp.setText("")
        self.label_9.setText(QCoreApplication.translate("Form", u"      Select the buffer you want to calculate fill out the information, and calculate", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Conductivity", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"     Far less accurate this should be considered a floor the conductiivty should be no lower than this.", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"    Select different hydrated conjugates if desired", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"           If titrating with the selected conjugate above", None))
    # retranslateUi

