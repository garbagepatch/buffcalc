from ui.recipewidget import Ui_Form
from PySide2.QtSql import QSqlTableModel
from PySide2.QtWidgets import QApplication, QWidget, QTableView, QAbstractItemView, QVBoxLayout
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtSql import *
from PySide2.QtWidgets import QWidget
import qdarkstyle
from data.connection import createBufferList, createHAList, createAList
from data.connection import sqlite3con
from PySide2 import QtWidgets, QtCore, QtGui
from math import log10
"""import pyqtgraph.opengl as gl"""
from PySide2.QtGui import QIcon, QImage, QPixmap
from PySide2.QtWidgets import  QMainWindow, QAction, QMessageBox
from qt_material import apply_stylesheet
from datetime import date
"""from opensimplex import OpenSimplex"""
import sys
from data.connection import createConnection

class RepairBuffer(QWidget, Ui_Form):
    def __init__(self):
        super(RepairBuffer, self).__init__()
        self.setupUi(self)
        self.connection = sqlite3con()
        self.bufferId = 0
        self.buffers = createBufferList(self.connection)
        self.mwHA = 0.00
        self.mwA = 0.00
        self.totMol = 0.00
        self.haMol = 0.00
        self.HA =0.00
        self.customHAMW.setVisible(0)
        self.customAMW.setVisible(0)
        self.label_13.setVisible(0)
        self.label_14.setVisible(0)
        self.A =0.00
        self.aMol = 0.00
        self.pKa = 0.00
        self.targetpH = 0.00
        self.initpH = 0.00
        self.molrat = 0.00
        self.pkavar= 0.00
        self.comboBox_2.addItems(self.buffers)
        self.comboBox_2.currentTextChanged.connect(self.SetBuffer)
        self.checkBox.stateChanged.connect(self.Custom)
        self.isCustom = False
        self.calculateButton.clicked.connect(self.Calculate)
       
    def Custom(self):
       
        if(self.checkBox.isChecked()):
            self.label_13.setVisible(True)
            self.label_14.setVisible(True)
            self.customAMW.setVisible(True)
            self.customHAMW.setVisible(True)
            self.comboBox_2.setVisible(False)
        else:
            self.label_13.setVisible(False)
            self.label_14.setVisible(False)
            self.customAMW.setVisible(False)
            self.customHAMW.setVisible(False)
            self.comboBox_2.setVisible(True)
    def SetBuffer(self):

        buffer = self.comboBox_2.currentText()
        cursor = self.connection.cursor()
        
        
        self.bufferId, _, self.pKa = ses.fetchone()
        self.setHAs()
        self.setAs()
        
    def setHAs(self):
        cursor = self.connection.cursor()
        mwe = cursor.execute("SELECT MW FROM Chemical WHERE COMP = 'HA' AND BufferId = ?", (self.bufferId,))
        (mw) = mwe.fetchall()[0]
        self.mwHA = mw[0]
        
    def setAs(self):
        cursor = self.connection.cursor()
        mwe = cursor.execute("SELECT MW FROM Chemical WHERE COMP = 'A' AND BufferId = ?", (self.bufferId,))
        (mw) = mwe.fetchall()[0]
        self.mwA = mw[0]
       
    def Calculate(self):
        if(self.checkBox.isChecked()):
            self.mwHA = float(self.customHAMW.text())
            self.mwA = float(self.customAMW.text())
        initialHA = float(self.initialAmountHALineEdit.text())
        initialA = float(self.initialAmountALineEdit.text())
        self.initpH = float(self.measuredPHLineEdit.text())
        self.targetpH = float(self.targetpHLineEdit.text())
        self.totMol = float(self.molarityOfBufferLineEdit.text())
     
        if(self.bufferId ==1):
            self.pkavar = self.initpH - log10(initialA/self.mwA) +log10(self.mwHA * initialHA/1000)
            
        else:
            self.pkavar = self.initpH - log10(initialA/self.mwA) + log10(initialHA/self.mwHA)
        self.molrat = 10**(self.targetpH-self.pkavar)
        self.filloutStuff()
    def filloutStuff(self):
        if(self.bufferId==1):
            self.haResults.setText(str((self.totMol/(1+self.molrat))*1000/self.mwHA))
        else:
            self.haResults.setText(str(self.totMol*self.mwHA/(1+self.molrat)))
            
        self.aResults.setText(str(self.molrat*self.totMol*self.mwA/(1+self.molrat)))
        
         
    