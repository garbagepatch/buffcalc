# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dw_displays.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DockWidget(object):
    def setupUi(self, DockWidget):
        if not DockWidget.objectName():
            DockWidget.setObjectName(u"DockWidget")
        DockWidget.resize(592, 557)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.gridLayout = QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.textBrowser = QTextBrowser(self.dockWidgetContents)
        self.textBrowser.setObjectName(u"textBrowser")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setMinimumSize(QSize(0, 0))
        self.textBrowser.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.textBrowser, 2, 1, 1, 1)

        self.label_77 = QLabel(self.dockWidgetContents)
        self.label_77.setObjectName(u"label_77")
        sizePolicy.setHeightForWidth(self.label_77.sizePolicy().hasHeightForWidth())
        self.label_77.setSizePolicy(sizePolicy)
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_77.setFont(font)

        self.gridLayout.addWidget(self.label_77, 0, 1, 1, 1)

        self.label_78 = QLabel(self.dockWidgetContents)
        self.label_78.setObjectName(u"label_78")
        sizePolicy.setHeightForWidth(self.label_78.sizePolicy().hasHeightForWidth())
        self.label_78.setSizePolicy(sizePolicy)
        self.label_78.setFont(font)

        self.gridLayout.addWidget(self.label_78, 0, 2, 1, 1)

        self.label_3 = QLabel(self.dockWidgetContents)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QSize(0, 0))
        self.label_3.setMaximumSize(QSize(16777215, 16777215))
        self.label_3.setFont(font)

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_79 = QLabel(self.dockWidgetContents)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setEnabled(False)
        sizePolicy.setHeightForWidth(self.label_79.sizePolicy().hasHeightForWidth())
        self.label_79.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label_79, 1, 2, 1, 1)

        self.label_4 = QLabel(self.dockWidgetContents)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QSize(0, 0))
        self.label_4.setMaximumSize(QSize(16777215, 16777215))
        self.label_4.setFont(font)

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.textBrowserDis = QTextBrowser(self.dockWidgetContents)
        self.textBrowserDis.setObjectName(u"textBrowserDis")
        self.textBrowserDis.setEnabled(False)
        sizePolicy.setHeightForWidth(self.textBrowserDis.sizePolicy().hasHeightForWidth())
        self.textBrowserDis.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.textBrowserDis, 2, 2, 1, 1)

        self.label_5 = QLabel(self.dockWidgetContents)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QSize(0, 0))
        self.label_5.setMaximumSize(QSize(16777215, 16777215))
        self.label_5.setFont(font)

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)

        self.graphicsView = QGraphicsView(self.dockWidgetContents)
        self.graphicsView.setObjectName(u"graphicsView")
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setMinimumSize(QSize(0, 0))
        self.graphicsView.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.graphicsView, 3, 1, 1, 1)

        self.graphicsViewDis = QGraphicsView(self.dockWidgetContents)
        self.graphicsViewDis.setObjectName(u"graphicsViewDis")
        self.graphicsViewDis.setEnabled(False)
        sizePolicy.setHeightForWidth(self.graphicsViewDis.sizePolicy().hasHeightForWidth())
        self.graphicsViewDis.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.graphicsViewDis, 3, 2, 1, 1)

        self.label_6 = QLabel(self.dockWidgetContents)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QSize(0, 0))
        self.label_6.setMaximumSize(QSize(16777215, 16777215))
        self.label_6.setFont(font)

        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)

        self.calendarWidget = QCalendarWidget(self.dockWidgetContents)
        self.calendarWidget.setObjectName(u"calendarWidget")
        sizePolicy.setHeightForWidth(self.calendarWidget.sizePolicy().hasHeightForWidth())
        self.calendarWidget.setSizePolicy(sizePolicy)
        self.calendarWidget.setMinimumSize(QSize(0, 0))
        self.calendarWidget.setMaximumSize(QSize(350, 16777215))
        font1 = QFont()
        font1.setFamily(u"Lato")
        font1.setPointSize(8)
        font1.setItalic(False)
        self.calendarWidget.setFont(font1)

        self.gridLayout.addWidget(self.calendarWidget, 4, 1, 1, 1)

        self.lcdNumberDis = QLCDNumber(self.dockWidgetContents)
        self.lcdNumberDis.setObjectName(u"lcdNumberDis")
        self.lcdNumberDis.setEnabled(False)
        sizePolicy.setHeightForWidth(self.lcdNumberDis.sizePolicy().hasHeightForWidth())
        self.lcdNumberDis.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.lcdNumberDis, 5, 2, 1, 1)

        self.label_7 = QLabel(self.dockWidgetContents)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMinimumSize(QSize(0, 0))
        self.label_7.setMaximumSize(QSize(16777215, 16777215))
        self.label_7.setFont(font)

        self.gridLayout.addWidget(self.label_7, 5, 0, 1, 1)

        self.lcdNumber = QLCDNumber(self.dockWidgetContents)
        self.lcdNumber.setObjectName(u"lcdNumber")
        sizePolicy.setHeightForWidth(self.lcdNumber.sizePolicy().hasHeightForWidth())
        self.lcdNumber.setSizePolicy(sizePolicy)
        self.lcdNumber.setMinimumSize(QSize(0, 0))
        self.lcdNumber.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.lcdNumber, 5, 1, 1, 1)

        self.label_8 = QLabel(self.dockWidgetContents)
        self.label_8.setObjectName(u"label_8")
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMinimumSize(QSize(0, 0))
        self.label_8.setMaximumSize(QSize(16777215, 16777215))
        self.label_8.setFont(font)

        self.gridLayout.addWidget(self.label_8, 6, 0, 1, 1)

        self.progressBar = QProgressBar(self.dockWidgetContents)
        self.progressBar.setObjectName(u"progressBar")
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setMinimumSize(QSize(0, 0))
        self.progressBar.setMaximumSize(QSize(16777215, 16777215))
        self.progressBar.setValue(24)

        self.gridLayout.addWidget(self.progressBar, 6, 1, 1, 1)

        self.progressBarDis = QProgressBar(self.dockWidgetContents)
        self.progressBarDis.setObjectName(u"progressBarDis")
        self.progressBarDis.setEnabled(False)
        sizePolicy.setHeightForWidth(self.progressBarDis.sizePolicy().hasHeightForWidth())
        self.progressBarDis.setSizePolicy(sizePolicy)
        self.progressBarDis.setValue(24)

        self.gridLayout.addWidget(self.progressBarDis, 6, 2, 1, 1)

        self.label_9 = QLabel(self.dockWidgetContents)
        self.label_9.setObjectName(u"label_9")
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setMinimumSize(QSize(0, 0))
        self.label_9.setMaximumSize(QSize(16777215, 16777215))
        self.label_9.setFont(font)

        self.gridLayout.addWidget(self.label_9, 7, 0, 1, 1)

        self.lineH = QFrame(self.dockWidgetContents)
        self.lineH.setObjectName(u"lineH")
        sizePolicy.setHeightForWidth(self.lineH.sizePolicy().hasHeightForWidth())
        self.lineH.setSizePolicy(sizePolicy)
        self.lineH.setMinimumSize(QSize(0, 0))
        self.lineH.setMaximumSize(QSize(16777215, 16777215))
        self.lineH.setFrameShape(QFrame.HLine)
        self.lineH.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.lineH, 7, 1, 1, 1)

        self.lineHDis = QFrame(self.dockWidgetContents)
        self.lineHDis.setObjectName(u"lineHDis")
        self.lineHDis.setEnabled(False)
        sizePolicy.setHeightForWidth(self.lineHDis.sizePolicy().hasHeightForWidth())
        self.lineHDis.setSizePolicy(sizePolicy)
        self.lineHDis.setFrameShape(QFrame.HLine)
        self.lineHDis.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.lineHDis, 7, 2, 1, 1)

        self.label_10 = QLabel(self.dockWidgetContents)
        self.label_10.setObjectName(u"label_10")
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMinimumSize(QSize(0, 0))
        self.label_10.setMaximumSize(QSize(16777215, 16777215))
        self.label_10.setFont(font)

        self.gridLayout.addWidget(self.label_10, 8, 0, 1, 1)

        self.lineV = QFrame(self.dockWidgetContents)
        self.lineV.setObjectName(u"lineV")
        sizePolicy.setHeightForWidth(self.lineV.sizePolicy().hasHeightForWidth())
        self.lineV.setSizePolicy(sizePolicy)
        self.lineV.setMinimumSize(QSize(0, 50))
        self.lineV.setMaximumSize(QSize(16777215, 16777215))
        self.lineV.setFrameShape(QFrame.VLine)
        self.lineV.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.lineV, 8, 1, 1, 1)

        self.lineVDis = QFrame(self.dockWidgetContents)
        self.lineVDis.setObjectName(u"lineVDis")
        self.lineVDis.setEnabled(False)
        sizePolicy.setHeightForWidth(self.lineVDis.sizePolicy().hasHeightForWidth())
        self.lineVDis.setSizePolicy(sizePolicy)
        self.lineVDis.setMinimumSize(QSize(0, 50))
        self.lineVDis.setFrameShape(QFrame.VLine)
        self.lineVDis.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.lineVDis, 8, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 9, 0, 1, 1)

        self.label_37 = QLabel(self.dockWidgetContents)
        self.label_37.setObjectName(u"label_37")
        sizePolicy.setHeightForWidth(self.label_37.sizePolicy().hasHeightForWidth())
        self.label_37.setSizePolicy(sizePolicy)
        self.label_37.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_37, 10, 0, 1, 3)

        self.label_2 = QLabel(self.dockWidgetContents)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QSize(0, 0))
        self.label_2.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)

        self.calendarWidgetDis = QCalendarWidget(self.dockWidgetContents)
        self.calendarWidgetDis.setObjectName(u"calendarWidgetDis")
        self.calendarWidgetDis.setEnabled(False)
        sizePolicy.setHeightForWidth(self.calendarWidgetDis.sizePolicy().hasHeightForWidth())
        self.calendarWidgetDis.setSizePolicy(sizePolicy)
        self.calendarWidgetDis.setMaximumSize(QSize(350, 16777215))
        self.calendarWidgetDis.setFont(font1)

        self.gridLayout.addWidget(self.calendarWidgetDis, 4, 2, 1, 1)

        DockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidget)
        self.progressBar.valueChanged.connect(self.progressBarDis.setValue)
        self.calendarWidget.currentPageChanged.connect(self.calendarWidgetDis.setCurrentPage)
        self.calendarWidget.clicked.connect(self.calendarWidgetDis.setSelectedDate)

        QMetaObject.connectSlotsByName(DockWidget)
    # setupUi

    def retranslateUi(self, DockWidget):
        DockWidget.setWindowTitle(QCoreApplication.translate("DockWidget", u"Displays", None))
#if QT_CONFIG(tooltip)
        self.textBrowser.setToolTip(QCoreApplication.translate("DockWidget", u"This is a tool tip", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.textBrowser.setStatusTip(QCoreApplication.translate("DockWidget", u"This is a status tip", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.textBrowser.setWhatsThis(QCoreApplication.translate("DockWidget", u"This is \"what is this\"", None))
#endif // QT_CONFIG(whatsthis)
        self.textBrowser.setHtml(QCoreApplication.translate("DockWidget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Cantarell';\">Testing</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Cantarell';\"><br /></p></body></html>", None))
        self.label_77.setText(QCoreApplication.translate("DockWidget", u"Enabled", None))
        self.label_78.setText(QCoreApplication.translate("DockWidget", u"Disabled", None))
#if QT_CONFIG(tooltip)
        self.label_3.setToolTip(QCoreApplication.translate("DockWidget", u"This is a tool tip", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.label_3.setStatusTip(QCoreApplication.translate("DockWidget", u"This is a status tip", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.label_3.setWhatsThis(QCoreApplication.translate("DockWidget", u"This is \"what is this\"", None))
#endif // QT_CONFIG(whatsthis)
        self.label_3.setText(QCoreApplication.translate("DockWidget", u"Label", None))
        self.label_79.setText(QCoreApplication.translate("DockWidget", u"Testing", None))
#if QT_CONFIG(tooltip)
        self.label_4.setToolTip(QCoreApplication.translate("DockWidget", u"This is a tool tip", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.label_4.setStatusTip(QCoreApplication.translate("DockWidget", u"This is a status tip", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.label_4.setWhatsThis(QCoreApplication.translate("DockWidget", u"This is \"what is this\"", None))
#endif // QT_CONFIG(whatsthis)
        self.label_4.setText(QCoreApplication.translate("DockWidget", u"TextBrowser", None))
        self.textBrowserDis.setHtml(QCoreApplication.translate("DockWidget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Cantarell';\">Testing</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.label_5.setToolTip(QCoreApplication.translate("DockWidget", u"This is a tool tip", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.label_5.setStatusTip(QCoreApplication.translate("DockWidget", u"This is a status tip", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.label_5.setWhatsThis(QCoreApplication.translate("DockWidget", u"This is \"what is this\"", None))
#endif // QT_CONFIG(whatsthis)
        self.label_5.setText(QCoreApplication.translate("DockWidget", u"GraphicsView", None))
#if QT_CONFIG(tooltip)
        self.graphicsView.setToolTip(QCoreApplication.translate("DockWidget", u"This is a tool tip", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.graphicsView.setStatusTip(QCoreApplication.translate("DockWidget", u"This is a status tip", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.graphicsView.setWhatsThis(QCoreApplication.translate("DockWidget", u"This is \"what is this\"", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.label_6.setToolTip(QCoreApplication.translate("DockWidget", u"This is a tool tip", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.label_6.setStatusTip(QCoreApplication.translate("DockWidget", u"This is a status tip", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.label_6.setWhatsThis(QCoreApplication.translate("DockWidget", u"This is \"what is this\"", None))
#endif // QT_CONFIG(whatsthis)
        self.label_6.setText(QCoreApplication.translate("DockWidget", u"CalendarWidget", None))
#if QT_CONFIG(tooltip)
        self.calendarWidget.setToolTip(QCoreApplication.translate("DockWidget", u"This is a tool tip", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.calendarWidget.setStatusTip(QCoreApplication.translate("DockWidget", u"This is a status tip", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.calendarWidget.setWhatsThis(QCoreApplication.translate("DockWidget", u"This is \"what is this\"", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.label_7.setToolTip(QCoreApplication.translate("DockWidget", u"This is a tool tip", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.label_7.setStatusTip(QCoreApplication.translate("DockWidget", u"This is a status tip", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.label_7.setWhatsThis(QCoreApplication.translate("DockWidget", u"This is \"what is this\"", None))
#endif // QT_CONFIG(whatsthis)
        self.label_7.setText(QCoreApplication.translate("DockWidget", u"LCDNumber", None))
#if QT_CONFIG(tooltip)
        self.lcdNumber.setToolTip(QCoreApplication.translate("DockWidget", u"This is a tool tip", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.lcdNumber.setStatusTip(QCoreApplication.translate("DockWidget", u"This is a status tip", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.lcdNumber.setWhatsThis(QCoreApplication.translate("DockWidget", u"This is \"what is this\"", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.label_8.setToolTip(QCoreApplication.translate("DockWidget", u"This is a tool tip", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.label_8.setStatusTip(QCoreApplication.translate("DockWidget", u"This is a status tip", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.label_8.setWhatsThis(QCoreApplication.translate("DockWidget", u"This is \"what is this\"", None))
#endif // QT_CONFIG(whatsthis)
        self.label_8.setText(QCoreApplication.translate("DockWidget", u"ProgressBar", None))
#if QT_CONFIG(tooltip)
        self.progressBar.setToolTip(QCoreApplication.translate("DockWidget", u"This is a tool tip", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.progressBar.setStatusTip(QCoreApplication.translate("DockWidget", u"This is a status tip", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.progressBar.setWhatsThis(QCoreApplication.translate("DockWidget", u"This is \"what is this\"", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.label_9.setToolTip(QCoreApplication.translate("DockWidget", u"This is a tool tip", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.label_9.setStatusTip(QCoreApplication.translate("DockWidget", u"This is a status tip", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.label_9.setWhatsThis(QCoreApplication.translate("DockWidget", u"This is \"what is this\"", None))
#endif // QT_CONFIG(whatsthis)
        self.label_9.setText(QCoreApplication.translate("DockWidget", u"Line - H", None))
#if QT_CONFIG(tooltip)
        self.lineH.setToolTip(QCoreApplication.translate("DockWidget", u"This is a tool tip", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.lineH.setStatusTip(QCoreApplication.translate("DockWidget", u"This is a status tip", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.lineH.setWhatsThis(QCoreApplication.translate("DockWidget", u"This is \"what is this\"", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.label_10.setToolTip(QCoreApplication.translate("DockWidget", u"This is a tool tip", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.label_10.setStatusTip(QCoreApplication.translate("DockWidget", u"This is a status tip", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.label_10.setWhatsThis(QCoreApplication.translate("DockWidget", u"This is \"what is this\"", None))
#endif // QT_CONFIG(whatsthis)
        self.label_10.setText(QCoreApplication.translate("DockWidget", u"Line - V", None))
#if QT_CONFIG(tooltip)
        self.lineV.setToolTip(QCoreApplication.translate("DockWidget", u"This is a tool tip", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.lineV.setStatusTip(QCoreApplication.translate("DockWidget", u"This is a status tip", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.lineV.setWhatsThis(QCoreApplication.translate("DockWidget", u"This is \"what is this\"", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.label_37.setToolTip(QCoreApplication.translate("DockWidget", u"This is a tool tip", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.label_37.setStatusTip(QCoreApplication.translate("DockWidget", u"This is a status tip", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.label_37.setWhatsThis(QCoreApplication.translate("DockWidget", u"This is \"what is this\"", None))
#endif // QT_CONFIG(whatsthis)
        self.label_37.setText(QCoreApplication.translate("DockWidget", u"Inside DockWidget", None))
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip(QCoreApplication.translate("DockWidget", u"This is a tool tip", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.label_2.setStatusTip(QCoreApplication.translate("DockWidget", u"This is a status tip", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.label_2.setWhatsThis(QCoreApplication.translate("DockWidget", u"This is \"what is this\"", None))
#endif // QT_CONFIG(whatsthis)
        self.label_2.setText(QCoreApplication.translate("DockWidget", u"Testing", None))
    # retranslateUi

