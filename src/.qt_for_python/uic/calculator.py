# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculator.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1085, 556)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 1071, 451))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setHorizontalSpacing(100)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setFrameShape(QFrame.NoFrame)
        self.label_4.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setFont(font)
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)
        self.label_6.setFrameShape(QFrame.NoFrame)
        self.label_6.setFrameShadow(QFrame.Raised)
        self.label_6.setScaledContents(True)
        self.label_6.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.gridLayout.addWidget(self.label_6, 4, 1, 1, 1)

        self.line_3 = QFrame(self.gridLayoutWidget)
        self.line_3.setObjectName(u"line_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.line_3.sizePolicy().hasHeightForWidth())
        self.line_3.setSizePolicy(sizePolicy1)
        self.line_3.setMinimumSize(QSize(0, 10))
        self.line_3.setFrameShadow(QFrame.Plain)
        self.line_3.setLineWidth(2)
        self.line_3.setMidLineWidth(1)
        self.line_3.setFrameShape(QFrame.HLine)

        self.gridLayout.addWidget(self.line_3, 5, 0, 1, 1)

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
        sizePolicy.setHeightForWidth(self.haResultBox.sizePolicy().hasHeightForWidth())
        self.haResultBox.setSizePolicy(sizePolicy)
        self.haResultBox.setMinimumSize(QSize(0, 0))
        self.haResultBox.setMaximumSize(QSize(100, 16777215))
        font1 = QFont()
        font1.setPointSize(12)
        self.haResultBox.setFont(font1)
        self.haResultBox.setMaxLength(8)
        self.haResultBox.setAlignment(Qt.AlignCenter)
        self.haResultBox.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.haResultBox)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setFont(font1)
        self.label.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.label)


        self.gridLayout_2.addLayout(self.horizontalLayout_4, 0, 1, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetMinimumSize)
        self.aResultBox = QLineEdit(self.gridLayoutWidget)
        self.aResultBox.setObjectName(u"aResultBox")
        sizePolicy.setHeightForWidth(self.aResultBox.sizePolicy().hasHeightForWidth())
        self.aResultBox.setSizePolicy(sizePolicy)
        self.aResultBox.setMinimumSize(QSize(0, 0))
        self.aResultBox.setMaximumSize(QSize(100, 16777215))
        self.aResultBox.setFont(font1)
        self.aResultBox.setMaxLength(7)
        self.aResultBox.setAlignment(Qt.AlignCenter)
        self.aResultBox.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.aResultBox)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setFont(font1)
        self.label_2.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.horizontalLayout_3.setStretch(0, 5)
        self.horizontalLayout_3.setStretch(1, 1)

        self.gridLayout_2.addLayout(self.horizontalLayout_3, 1, 1, 1, 1)

        self.haChoiceCombo = QComboBox(self.gridLayoutWidget)
        self.haChoiceCombo.setObjectName(u"haChoiceCombo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.haChoiceCombo.sizePolicy().hasHeightForWidth())
        self.haChoiceCombo.setSizePolicy(sizePolicy2)
        self.haChoiceCombo.setFont(font1)

        self.gridLayout_2.addWidget(self.haChoiceCombo, 0, 0, 1, 1)

        self.aChoiceCombo = QComboBox(self.gridLayoutWidget)
        self.aChoiceCombo.setObjectName(u"aChoiceCombo")
        self.aChoiceCombo.setFont(font1)
        self.aChoiceCombo.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.gridLayout_2.addWidget(self.aChoiceCombo, 1, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setSizeConstraint(QLayout.SetMinimumSize)
        self.aResultBox_2 = QLineEdit(self.gridLayoutWidget)
        self.aResultBox_2.setObjectName(u"aResultBox_2")
        sizePolicy.setHeightForWidth(self.aResultBox_2.sizePolicy().hasHeightForWidth())
        self.aResultBox_2.setSizePolicy(sizePolicy)
        self.aResultBox_2.setMinimumSize(QSize(0, 0))
        self.aResultBox_2.setMaximumSize(QSize(100, 16777215))
        self.aResultBox_2.setFont(font1)
        self.aResultBox_2.setMaxLength(7)
        self.aResultBox_2.setAlignment(Qt.AlignCenter)
        self.aResultBox_2.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.aResultBox_2)

        self.label_8 = QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName(u"label_8")
        sizePolicy1.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy1)
        self.label_8.setFont(font1)
        self.label_8.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.label_8)

        self.horizontalLayout_5.setStretch(0, 5)
        self.horizontalLayout_5.setStretch(1, 1)

        self.gridLayout_2.addLayout(self.horizontalLayout_5, 2, 1, 1, 1)

        self.sodiumChlorideMolarityLabel = QLabel(self.gridLayoutWidget)
        self.sodiumChlorideMolarityLabel.setObjectName(u"sodiumChlorideMolarityLabel")
        self.sodiumChlorideMolarityLabel.setFont(font1)

        self.gridLayout_2.addWidget(self.sodiumChlorideMolarityLabel, 2, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.horizontalSpacer = QSpacerItem(40, 5, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.gridLayout.addLayout(self.horizontalLayout, 2, 1, 1, 1)

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
        self.bufferTypeLabel.setFont(font1)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.bufferTypeLabel)

        self.bufferTypeComboBox = QComboBox(self.gridLayoutWidget)
        self.bufferTypeComboBox.setObjectName(u"bufferTypeComboBox")
        self.bufferTypeComboBox.setFont(font1)
        self.bufferTypeComboBox.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.bufferTypeComboBox)

        self.totalBufferMolarityLabel = QLabel(self.gridLayoutWidget)
        self.totalBufferMolarityLabel.setObjectName(u"totalBufferMolarityLabel")
        self.totalBufferMolarityLabel.setFont(font1)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.totalBufferMolarityLabel)

        self.totalBufferMolarityLineEdit = QLineEdit(self.gridLayoutWidget)
        self.totalBufferMolarityLineEdit.setObjectName(u"totalBufferMolarityLineEdit")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.totalBufferMolarityLineEdit.sizePolicy().hasHeightForWidth())
        self.totalBufferMolarityLineEdit.setSizePolicy(sizePolicy3)
        self.totalBufferMolarityLineEdit.setFont(font1)
        self.totalBufferMolarityLineEdit.setInputMethodHints(Qt.ImhDigitsOnly)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.totalBufferMolarityLineEdit)

        self.sodiumChlorideMolarityLineEdit = QLineEdit(self.gridLayoutWidget)
        self.sodiumChlorideMolarityLineEdit.setObjectName(u"sodiumChlorideMolarityLineEdit")
        sizePolicy3.setHeightForWidth(self.sodiumChlorideMolarityLineEdit.sizePolicy().hasHeightForWidth())
        self.sodiumChlorideMolarityLineEdit.setSizePolicy(sizePolicy3)
        self.sodiumChlorideMolarityLineEdit.setFont(font1)
        self.sodiumChlorideMolarityLineEdit.setInputMethodHints(Qt.ImhDigitsOnly)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.sodiumChlorideMolarityLineEdit)

        self.targetPHLabel = QLabel(self.gridLayoutWidget)
        self.targetPHLabel.setObjectName(u"targetPHLabel")
        self.targetPHLabel.setFont(font1)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.targetPHLabel)

        self.targetPHLineEdit = QLineEdit(self.gridLayoutWidget)
        self.targetPHLineEdit.setObjectName(u"targetPHLineEdit")
        sizePolicy2.setHeightForWidth(self.targetPHLineEdit.sizePolicy().hasHeightForWidth())
        self.targetPHLineEdit.setSizePolicy(sizePolicy2)
        self.targetPHLineEdit.setFont(font1)
        self.targetPHLineEdit.setInputMethodHints(Qt.ImhDigitsOnly)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.targetPHLineEdit)

        self.targetTemperatureLabel = QLabel(self.gridLayoutWidget)
        self.targetTemperatureLabel.setObjectName(u"targetTemperatureLabel")
        self.targetTemperatureLabel.setFont(font1)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.targetTemperatureLabel)

        self.targetTemperatureLineEdit = QLineEdit(self.gridLayoutWidget)
        self.targetTemperatureLineEdit.setObjectName(u"targetTemperatureLineEdit")
        sizePolicy3.setHeightForWidth(self.targetTemperatureLineEdit.sizePolicy().hasHeightForWidth())
        self.targetTemperatureLineEdit.setSizePolicy(sizePolicy3)
        self.targetTemperatureLineEdit.setFont(font1)
        self.targetTemperatureLineEdit.setInputMethodHints(Qt.ImhDigitsOnly)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.targetTemperatureLineEdit)

        self.Calculate = QPushButton(self.gridLayoutWidget)
        self.Calculate.setObjectName(u"Calculate")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.Calculate.sizePolicy().hasHeightForWidth())
        self.Calculate.setSizePolicy(sizePolicy4)
        self.Calculate.setMinimumSize(QSize(20, 0))
        self.Calculate.setMaximumSize(QSize(177, 16777215))
        font2 = QFont()
        font2.setPointSize(13)
        self.Calculate.setFont(font2)
        self.Calculate.setFlat(False)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.Calculate)

        self.sodiumChlorideMolarityLabel_2 = QLabel(self.gridLayoutWidget)
        self.sodiumChlorideMolarityLabel_2.setObjectName(u"sodiumChlorideMolarityLabel_2")
        self.sodiumChlorideMolarityLabel_2.setFont(font1)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.sodiumChlorideMolarityLabel_2)


        self.verticalLayout_2.addLayout(self.formLayout)


        self.gridLayout.addLayout(self.verticalLayout_2, 2, 0, 1, 1)

        self.line = QFrame(self.gridLayoutWidget)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(0, 10))
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setLineWidth(2)
        self.line.setMidLineWidth(1)
        self.line.setFrameShape(QFrame.HLine)

        self.gridLayout.addWidget(self.line, 1, 0, 1, 1)

        self.line_2 = QFrame(self.gridLayoutWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setMinimumSize(QSize(0, 10))
        self.line_2.setFrameShadow(QFrame.Plain)
        self.line_2.setLineWidth(2)
        self.line_2.setMidLineWidth(1)
        self.line_2.setFrameShape(QFrame.HLine)

        self.gridLayout.addWidget(self.line_2, 1, 1, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setFrameShape(QFrame.NoFrame)
        self.label_5.setFrameShadow(QFrame.Raised)
        self.label_5.setScaledContents(True)
        self.label_5.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setFieldGrowthPolicy(QFormLayout.FieldsStayAtSizeHint)
        self.formLayout_2.setFormAlignment(Qt.AlignCenter)
        self.formLayout_2.setHorizontalSpacing(20)
        self.formLayout_2.setVerticalSpacing(0)
        self.formLayout_2.setContentsMargins(0, 0, 20, 0)
        self.conductivityMSCmLabel = QLabel(self.gridLayoutWidget)
        self.conductivityMSCmLabel.setObjectName(u"conductivityMSCmLabel")
        self.conductivityMSCmLabel.setFont(font1)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.conductivityMSCmLabel)

        self.conductivityMSCmLineEdit = QLineEdit(self.gridLayoutWidget)
        self.conductivityMSCmLineEdit.setObjectName(u"conductivityMSCmLineEdit")
        sizePolicy.setHeightForWidth(self.conductivityMSCmLineEdit.sizePolicy().hasHeightForWidth())
        self.conductivityMSCmLineEdit.setSizePolicy(sizePolicy)
        self.conductivityMSCmLineEdit.setFont(font1)
        self.conductivityMSCmLineEdit.setMaxLength(5)
        self.conductivityMSCmLineEdit.setReadOnly(True)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.conductivityMSCmLineEdit)


        self.gridLayout.addLayout(self.formLayout_2, 6, 0, 1, 1)

        self.line_4 = QFrame(self.gridLayoutWidget)
        self.line_4.setObjectName(u"line_4")
        sizePolicy1.setHeightForWidth(self.line_4.sizePolicy().hasHeightForWidth())
        self.line_4.setSizePolicy(sizePolicy1)
        self.line_4.setMinimumSize(QSize(0, 10))
        self.line_4.setFrameShadow(QFrame.Plain)
        self.line_4.setLineWidth(2)
        self.line_4.setMidLineWidth(1)
        self.line_4.setFrameShape(QFrame.HLine)

        self.gridLayout.addWidget(self.line_4, 5, 1, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(20)
        self.gridLayout_3.setVerticalSpacing(6)
        self.titrantEdit = QLineEdit(self.gridLayoutWidget)
        self.titrantEdit.setObjectName(u"titrantEdit")
        sizePolicy4.setHeightForWidth(self.titrantEdit.sizePolicy().hasHeightForWidth())
        self.titrantEdit.setSizePolicy(sizePolicy4)
        self.titrantEdit.setMinimumSize(QSize(100, 0))
        self.titrantEdit.setMaximumSize(QSize(100, 16777215))
        self.titrantEdit.setFont(font1)
        self.titrantEdit.setInputMethodHints(Qt.ImhDigitsOnly)

        self.gridLayout_3.addWidget(self.titrantEdit, 0, 1, 1, 1)

        self.bufferEdit = QLineEdit(self.gridLayoutWidget)
        self.bufferEdit.setObjectName(u"bufferEdit")
        sizePolicy4.setHeightForWidth(self.bufferEdit.sizePolicy().hasHeightForWidth())
        self.bufferEdit.setSizePolicy(sizePolicy4)
        self.bufferEdit.setMinimumSize(QSize(100, 0))
        self.bufferEdit.setMaximumSize(QSize(50, 16777215))
        self.bufferEdit.setFont(font1)
        self.bufferEdit.setInputMethodHints(Qt.ImhDigitsOnly)

        self.gridLayout_3.addWidget(self.bufferEdit, 1, 1, 1, 1)

        self.comboBox = QComboBox(self.gridLayoutWidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy3.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy3)
        self.comboBox.setFont(font1)

        self.gridLayout_3.addWidget(self.comboBox, 0, 0, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 0, 2, 1, 1)

        self.titratename = QLabel(self.gridLayoutWidget)
        self.titratename.setObjectName(u"titratename")

        self.gridLayout_3.addWidget(self.titratename, 1, 2, 1, 1)

        self.buffercomp = QLabel(self.gridLayoutWidget)
        self.buffercomp.setObjectName(u"buffercomp")
        self.buffercomp.setFont(font1)
        self.buffercomp.setScaledContents(True)

        self.gridLayout_3.addWidget(self.buffercomp, 1, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_3, 6, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1085, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.haChoiceCombo.currentTextChanged.connect(self.Calculate.toggle)
        self.aChoiceCombo.currentTextChanged.connect(self.Calculate.click)
        self.bufferTypeComboBox.currentTextChanged.connect(self.conductivityMSCmLineEdit.clear)
        self.bufferTypeComboBox.currentTextChanged.connect(self.haResultBox.clear)
        self.bufferTypeComboBox.currentTextChanged.connect(self.aResultBox.clear)
        self.comboBox.currentTextChanged.connect(self.Calculate.click)

        self.Calculate.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Target Buffer Selection", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Results and Component Selection", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"With Strong Acid or Base", None))
        self.haResultBox.setText(QCoreApplication.translate("MainWindow", u"0.0000", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"g/L", None))
        self.aResultBox.setText(QCoreApplication.translate("MainWindow", u"0.0000", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"g/L", None))
        self.haChoiceCombo.setCurrentText("")
        self.haChoiceCombo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Acidic Component", None))
        self.aChoiceCombo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Basic Component", None))
        self.aResultBox_2.setText(QCoreApplication.translate("MainWindow", u"0.0000", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"g/L", None))
        self.sodiumChlorideMolarityLabel.setText(QCoreApplication.translate("MainWindow", u"Sodium Chloride", None))
        self.bufferTypeLabel.setText(QCoreApplication.translate("MainWindow", u"Buffer Type", None))
        self.totalBufferMolarityLabel.setText(QCoreApplication.translate("MainWindow", u"Total Buffer Molarity", None))
        self.targetPHLabel.setText(QCoreApplication.translate("MainWindow", u"Target pH ", None))
        self.targetTemperatureLabel.setText(QCoreApplication.translate("MainWindow", u"Target Temperature (C)", None))
        self.targetTemperatureLineEdit.setText(QCoreApplication.translate("MainWindow", u"25.0", None))
        self.Calculate.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
        self.sodiumChlorideMolarityLabel_2.setText(QCoreApplication.translate("MainWindow", u"Sodium Chloride Molarity", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Conductivity", None))
        self.conductivityMSCmLabel.setText(QCoreApplication.translate("MainWindow", u"Conductivity (mS/cm)", None))
        self.titrantEdit.setText(QCoreApplication.translate("MainWindow", u"0.000", None))
        self.bufferEdit.setText(QCoreApplication.translate("MainWindow", u"0.000", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"10N Sodium Hydroxide", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"6N Hydrochloric Acid", None))

        self.label_7.setText(QCoreApplication.translate("MainWindow", u"mL", None))
        self.titratename.setText(QCoreApplication.translate("MainWindow", u"g/L", None))
        self.buffercomp.setText("")
    # retranslateUi

