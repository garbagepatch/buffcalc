# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fixit.ui'
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
        MainWindow.resize(866, 526)
        MainWindow.setMaximumSize(QSize(2000, 16777215))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 851, 481))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.gridLayoutWidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.Panel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setLineWidth(3)
        self.frame_2.setMidLineWidth(1)
        self.gridLayoutWidget_3 = QWidget(self.frame_2)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(0, 0, 401, 171))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(50, 0, 0, 0)
        self.comboBox = QComboBox(self.gridLayoutWidget_3)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_3.addWidget(self.comboBox, 0, 1, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget_3)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 1, 0, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget_3)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 2, 0, 1, 1)

        self.customAMW = QLineEdit(self.gridLayoutWidget_3)
        self.customAMW.setObjectName(u"customAMW")
        self.customAMW.setEnabled(True)
        self.customAMW.setStyleSheet(u"hidden: true")
        self.customAMW.setInputMethodHints(Qt.ImhNone)

        self.gridLayout_3.addWidget(self.customAMW, 2, 1, 1, 1)

        self.customHAMW = QLineEdit(self.gridLayoutWidget_3)
        self.customHAMW.setObjectName(u"customHAMW")

        self.gridLayout_3.addWidget(self.customHAMW, 1, 1, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget_3)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)

        self.checkBox = QCheckBox(self.gridLayoutWidget_3)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout_3.addWidget(self.checkBox, 0, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(30, 0, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 2, 2, 1, 1)


        self.gridLayout.addWidget(self.frame_2, 0, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(20)
        self.label_6.setFont(font)

        self.verticalLayout.addWidget(self.label_6)

        self.line = QFrame(self.gridLayoutWidget)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(5, 5))
        self.line.setSizeIncrement(QSize(5, 5))
        self.line.setBaseSize(QSize(5, 5))
        font1 = QFont()
        font1.setPointSize(24)
        self.line.setFont(font1)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setLineWidth(3)
        self.line.setMidLineWidth(2)
        self.line.setFrameShape(QFrame.HLine)

        self.verticalLayout.addWidget(self.line)

        self.label_7 = QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_7)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.frame_3 = QFrame(self.gridLayoutWidget)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QFrame.Panel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_3.setLineWidth(3)
        self.frame_3.setMidLineWidth(1)
        self.gridLayoutWidget_2 = QWidget(self.frame_3)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(0, 0, 421, 301))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_2.setContentsMargins(10, 0, 0, 0)
        self.haResultsLabel = QLabel(self.gridLayoutWidget_2)
        self.haResultsLabel.setObjectName(u"haResultsLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.haResultsLabel.sizePolicy().hasHeightForWidth())
        self.haResultsLabel.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setPointSize(12)
        self.haResultsLabel.setFont(font2)
        self.haResultsLabel.setScaledContents(True)
        self.haResultsLabel.setAlignment(Qt.AlignCenter)
        self.haResultsLabel.setWordWrap(True)

        self.gridLayout_2.addWidget(self.haResultsLabel, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(30, 0, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 2, 1, 1)

        self.haResults = QLineEdit(self.gridLayoutWidget_2)
        self.haResults.setObjectName(u"haResults")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.haResults.sizePolicy().hasHeightForWidth())
        self.haResults.setSizePolicy(sizePolicy2)
        self.haResults.setMaximumSize(QSize(100, 16777215))
        self.haResults.setFont(font2)
        self.haResults.setInputMethodHints(Qt.ImhDigitsOnly)
        self.haResults.setMaxLength(6)
        self.haResults.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.haResults, 0, 1, 1, 1)

        self.aResults = QLineEdit(self.gridLayoutWidget_2)
        self.aResults.setObjectName(u"aResults")
        self.aResults.setMaximumSize(QSize(100, 16777215))
        self.aResults.setFont(font2)
        self.aResults.setInputMethodHints(Qt.ImhDigitsOnly)
        self.aResults.setMaxLength(6)
        self.aResults.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.aResults, 1, 1, 1, 1)

        self.aResultsLabel = QLabel(self.gridLayoutWidget_2)
        self.aResultsLabel.setObjectName(u"aResultsLabel")
        self.aResultsLabel.setFont(font2)
        self.aResultsLabel.setScaledContents(True)
        self.aResultsLabel.setAlignment(Qt.AlignCenter)
        self.aResultsLabel.setWordWrap(True)

        self.gridLayout_2.addWidget(self.aResultsLabel, 1, 0, 1, 1)

        self.calculateButton = QPushButton(self.gridLayoutWidget_2)
        self.calculateButton.setObjectName(u"calculateButton")
        sizePolicy2.setHeightForWidth(self.calculateButton.sizePolicy().hasHeightForWidth())
        self.calculateButton.setSizePolicy(sizePolicy2)
        self.calculateButton.setFlat(False)

        self.gridLayout_2.addWidget(self.calculateButton, 2, 2, 1, 1)

        self.gridLayout_2.setColumnStretch(1, 1)

        self.gridLayout.addWidget(self.frame_3, 2, 1, 1, 1)

        self.frame = QFrame(self.gridLayoutWidget)
        self.frame.setObjectName(u"frame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
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
        self.formLayoutWidget.setGeometry(QRect(0, 0, 421, 315))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignCenter)
        self.formLayout.setFormAlignment(Qt.AlignCenter)
        self.formLayout.setHorizontalSpacing(20)
        self.formLayout.setVerticalSpacing(20)
        self.formLayout.setContentsMargins(10, 10, 20, 10)
        self.initialAmountHALabel = QLabel(self.formLayoutWidget)
        self.initialAmountHALabel.setObjectName(u"initialAmountHALabel")
        self.initialAmountHALabel.setFont(font2)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.initialAmountHALabel)

        self.initialAmountHALineEdit = QLineEdit(self.formLayoutWidget)
        self.initialAmountHALineEdit.setObjectName(u"initialAmountHALineEdit")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.initialAmountHALineEdit.sizePolicy().hasHeightForWidth())
        self.initialAmountHALineEdit.setSizePolicy(sizePolicy4)
        self.initialAmountHALineEdit.setMaximumSize(QSize(100, 16777215))
        self.initialAmountHALineEdit.setFont(font2)
        self.initialAmountHALineEdit.setInputMethodHints(Qt.ImhDigitsOnly)
        self.initialAmountHALineEdit.setMaxLength(6)
        self.initialAmountHALineEdit.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.initialAmountHALineEdit)

        self.initialAmountALabel = QLabel(self.formLayoutWidget)
        self.initialAmountALabel.setObjectName(u"initialAmountALabel")
        self.initialAmountALabel.setFont(font2)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.initialAmountALabel)

        self.initialAmountALineEdit = QLineEdit(self.formLayoutWidget)
        self.initialAmountALineEdit.setObjectName(u"initialAmountALineEdit")
        sizePolicy4.setHeightForWidth(self.initialAmountALineEdit.sizePolicy().hasHeightForWidth())
        self.initialAmountALineEdit.setSizePolicy(sizePolicy4)
        self.initialAmountALineEdit.setMaximumSize(QSize(100, 16777215))
        self.initialAmountALineEdit.setFont(font2)
        self.initialAmountALineEdit.setInputMethodHints(Qt.ImhDigitsOnly)
        self.initialAmountALineEdit.setMaxLength(6)
        self.initialAmountALineEdit.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.initialAmountALineEdit)

        self.measuredPHLabel = QLabel(self.formLayoutWidget)
        self.measuredPHLabel.setObjectName(u"measuredPHLabel")
        self.measuredPHLabel.setFont(font2)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.measuredPHLabel)

        self.measuredPHLineEdit = QLineEdit(self.formLayoutWidget)
        self.measuredPHLineEdit.setObjectName(u"measuredPHLineEdit")
        sizePolicy4.setHeightForWidth(self.measuredPHLineEdit.sizePolicy().hasHeightForWidth())
        self.measuredPHLineEdit.setSizePolicy(sizePolicy4)
        self.measuredPHLineEdit.setMaximumSize(QSize(100, 16777215))
        self.measuredPHLineEdit.setFont(font2)
        self.measuredPHLineEdit.setInputMethodHints(Qt.ImhDigitsOnly)
        self.measuredPHLineEdit.setMaxLength(6)
        self.measuredPHLineEdit.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.measuredPHLineEdit)

        self.targetPLabel = QLabel(self.formLayoutWidget)
        self.targetPLabel.setObjectName(u"targetPLabel")
        self.targetPLabel.setFont(font2)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.targetPLabel)

        self.targetpHLineEdit = QLineEdit(self.formLayoutWidget)
        self.targetpHLineEdit.setObjectName(u"targetpHLineEdit")
        sizePolicy4.setHeightForWidth(self.targetpHLineEdit.sizePolicy().hasHeightForWidth())
        self.targetpHLineEdit.setSizePolicy(sizePolicy4)
        self.targetpHLineEdit.setMaximumSize(QSize(100, 16777215))
        self.targetpHLineEdit.setFont(font2)
        self.targetpHLineEdit.setInputMethodHints(Qt.ImhDigitsOnly)
        self.targetpHLineEdit.setMaxLength(6)
        self.targetpHLineEdit.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.targetpHLineEdit)

        self.molarityOfBufferLabel = QLabel(self.formLayoutWidget)
        self.molarityOfBufferLabel.setObjectName(u"molarityOfBufferLabel")
        self.molarityOfBufferLabel.setFont(font2)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.molarityOfBufferLabel)

        self.molarityOfBufferLineEdit = QLineEdit(self.formLayoutWidget)
        self.molarityOfBufferLineEdit.setObjectName(u"molarityOfBufferLineEdit")
        sizePolicy4.setHeightForWidth(self.molarityOfBufferLineEdit.sizePolicy().hasHeightForWidth())
        self.molarityOfBufferLineEdit.setSizePolicy(sizePolicy4)
        self.molarityOfBufferLineEdit.setMaximumSize(QSize(100, 16777215))
        self.molarityOfBufferLineEdit.setFont(font2)
        self.molarityOfBufferLineEdit.setInputMethodHints(Qt.ImhDigitsOnly)
        self.molarityOfBufferLineEdit.setMaxLength(6)
        self.molarityOfBufferLineEdit.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.molarityOfBufferLineEdit)


        self.gridLayout.addWidget(self.frame, 2, 0, 1, 1)

        self.gridLayout.setRowStretch(2, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 866, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"HA MW", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"A MW", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Buffer Selection", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Custom", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u" Fix Broken Recipes", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"       If you want to repair a recipe so that you no longer need to titrate it, use this tool. The logic underneath is that if you are just changing the amounts of conjugates to adjust for the pH, then all else being equal the equation becomes the henderson-hasselbach equation and is easily solvable.l", None))
        self.haResultsLabel.setText(QCoreApplication.translate("MainWindow", u"Corrected HA in (g/L)", None))
        self.aResultsLabel.setText(QCoreApplication.translate("MainWindow", u"Corrected A in (g/L)", None))
        self.calculateButton.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
        self.initialAmountHALabel.setText(QCoreApplication.translate("MainWindow", u"Initial Amount HA", None))
        self.initialAmountHALineEdit.setText(QCoreApplication.translate("MainWindow", u"0.000", None))
        self.initialAmountHALineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.initialAmountALabel.setText(QCoreApplication.translate("MainWindow", u"Initial Amount A", None))
        self.initialAmountALineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.measuredPHLabel.setText(QCoreApplication.translate("MainWindow", u"Measured pH", None))
        self.measuredPHLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.targetPLabel.setText(QCoreApplication.translate("MainWindow", u"Target pH", None))
        self.targetpHLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.molarityOfBufferLabel.setText(QCoreApplication.translate("MainWindow", u"Molarity of Buffer", None))
        self.molarityOfBufferLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.00", None))
    # retranslateUi

