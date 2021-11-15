from PySide2.QtSql import QSqlTableModel
from PySide2.QtWidgets import QApplication, QWidget, QTableView, QAbstractItemView, QVBoxLayout
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtSql import *
from PySide2.QtWidgets import QWidget
import qdarkstyle
from ui.calculator import Ui_MainWindow
from data.connection import createBufferList, createHAList, createAList
from data.connection import sqlite3con
from PySide2 import QtWidgets, QtCore, QtGui

"""import pyqtgraph.opengl as gl"""
from PySide2.QtGui import QIcon, QImage, QPixmap
from PySide2.QtWidgets import  QMainWindow, QAction, QMessageBox
from qt_material import apply_stylesheet
from datetime import date
"""from opensimplex import OpenSimplex"""
import sys
from data.connection import createConnection
class  BufferCalculator(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(BufferCalculator, self).__init__()
        self.setupUi(self)
        sys.stdout = self
        self.bufferId = 0
        self.createMenu()
        self.Calculate.clicked.connect(self.DoCalculation)
        self.setWindowTitle("Sup")
        self.pH = 0.0
        self.cond = 0.0
        self.delRow = -1
        self.totMol = 0.0
        self.connection = sqlite3con()
        self.zones = createBufferList(self.connection)
        self.pkaVar = 0.0
        self.bufferTypeComboBox.addItems(self.zones)
        self.bufferTypeComboBox.currentTextChanged.connect(self.SetBuffer)
        self.aChoiceCombo.setCurrentText("Sodium Acetate Anhydrous")
        self.haChoiceCombo.setCurrentText("Glacial Acetic Acid")
        self.naclMol = 0.0
        self.haMol = 0.0
        self.hasmw = 0.0
        self.asmw = 0.0
        self.aMol = 0.0
        self.pKa = 0.0

    def SetBuffer(self):
        buffer = self.bufferTypeComboBox.currentText()
        cursor = self.connection.cursor()
        ses = cursor.execute("SELECT * from Buffer where Type=?", (buffer,))
        
        
        self.bufferId, _, self.pKa = ses.fetchone()
        self.setHAs()
        self.setAs()
        
    def setAs(self):
        self.aChoiceCombo.clear()
        aas= createAList(self.connection, self.bufferId)
        self.aChoiceCombo.addItems(aas)
        self.aChoiceCombo.setCurrentText(aas[0])
    def setHAs(self):
        self.haChoiceCombo.clear()
        has = createHAList(self.connection, self.bufferId)
        
            
        self.haChoiceCombo.addItems(has)
        self.haChoiceCombo.setCurrentText(has[0])
    def exit_app(self):
        self.close()
    def DoCalculation(self):
        self.totMol = float(self.totalBufferMolarityLineEdit.text())
        self.naclMol = float(self.sodiumChlorideMolarityLineEdit.text())
        self.aResultBox_2.setText(str(self.naclMol*58.44))
        self.pH = float(self.targetPHLineEdit.text())
        self.temp = float(self.targetTemperatureLineEdit.text())
        self.tempDiff = self.temp - 25.0
        if(self.bufferId == 1): 
          self.pkaVar= float(4.76424) - float(0.0002) * self.tempDiff-float(0.76796)*((((self.totMol)-self.totMol/(float(10.0)**(self.pH-float(4.76424))+float(1.0)))+self.naclMol)**0.5)/(((self.totMol-(self.totMol/(10.0**(self.pH-4.76424)+1.0))+self.naclMol)**0.5)+1.0)+0.10870*((self.totMol-(self.totMol/(10.0**(self.pH-4.76424)+1.0))+self.naclMol)**0.5)
        if(self.bufferId== 2):
            self.pkaVar=  6.980686 -0.0028 *self.tempDiff-1.015071*((((self.totMol-(self.totMol/(10.0**(self.pH-7.24)+1.0))+self.naclMol)**0.5)/(((self.totMol-(self.totMol/(10.0**(self.pH-7.24)+1.0))+self.naclMol)**0.5)+1.0)))-0.251942*((self.totMol-(self.totMol/(10.0**(self.pH-7.24)+1.0))+self.naclMol))
        if(self.bufferId == 3):
            self.pkaVar = 8.089118 -0.028*self.tempDiff+ 0.286552*((((self.totMol-(self.totMol/(10.0**(self.pH-8.06)+1.0))+self.naclMol)**0.5)/(((self.totMol-(self.totMol/(10.0**(self.pH-8.06)+1.0))+self.naclMol)**0.5)+1.0)))+ 0.005268*((self.totMol-(self.totMol/(10.0**(self.pH-8.06)+1.0))+self.naclMol))  
        if(self.bufferId == 4): 
            self.pkaVar = 7.221505 -1.197193*((((self.totMol-(self.totMol/(10.0**(self.pH-7.2)+1.0))+self.naclMol)**0.5)/(((self.totMol-(self.totMol/(10.0**(self.pH-7.2)+1.0))+self.naclMol)**0.5)+1.0)))+0.870906*((self.totMol-(self.totMol/(10.0**(self.pH-7.2)+1.0))+self.naclMol))
        if(self.bufferId == 5):
            self.pkaVar = 6.147523 - -0.011*self.tempDiff-0.194272*((((self.totMol-(self.totMol/(10.0**(self.pH-6.21)+1.0))+self.naclMol)**0.5)/(((self.totMol-(self.totMol/(10.0**(self.pH-6.21)+1.0))+self.naclMol)**0.5)+1.0)))-0.023826*((self.totMol-(self.totMol/(10.0**(self.pH-6.21)+1.0))+self.naclMol)**0.5)
        if(self.bufferId ==6):      
            self.pkaVar = 7.731165 -0.835113 * self.naclMol -0.033846  * self.pH + -1.197864*self.totMol+   0.101651  * self.pH* self.naclMol +    0.504814 *self.totMol* self.naclMol +  0.163069*self.totMol* self.pH +    0.002898 * self.pH*self.totMol* self.naclMol
        self.finishCalc()
    def titrateCalculate(self):
        if(self.comboBox.currentText() == "10N Sodium Hydroxide"):
            if(self.bufferId == 1):
                self.titratename.setText("mL/L")
            self.titrantEdit.setText("g/mL")
            self.titrantEdit.setText(str(self.aMol/10 *1000))
            
            self.bufferEdit.setText(str(self.totMol * self.hasmw))
            self.buffercomp.setText(self.haChoiceCombo.currentText())
        elif(self.comboBox.currentText() =="6N Hydrochloric Acid"):
            self.titrantEdit.setText("g/mL")
            self.titrantEdit.setText(str(self.haMol/6*1000))
            self.bufferEdit.setText(str(self.totMol * self.asmw))
            self.buffercomp.setText(self.aChoiceCombo.currentText())
            
    
    def finishCalc(self):
        cursor = self.connection.cursor()
        mwe = cursor.execute("SELECT MW FROM Chemical WHERE Name = ?", (self.haChoiceCombo.currentText(),))
        (mw) = mwe.fetchall()[0]
        if(self.bufferId==1):
            self.haResultBox.setText(str(1000*self.totMol/(10.0**(self.pH-self.pkaVar)+1.0)/mw[0]))
            self.haMol = float(self.haResultBox.text())/1000 * 17.4
            self.hasmw = mw[0]
        else:
            self.haResultBox.setText(str(mw[0]*self.totMol/(10.0**(self.pH-self.pkaVar)+1.0)))
        self.titrateCalculate()
        self.seriouslyFinish()
    def seriouslyFinish(self):
        cursor = self.connection.cursor()
        mwe = cursor.execute("SELECT MW FROM Chemical WHERE Name = ?", (self.aChoiceCombo.currentText(),))
        (mw) = mwe.fetchall()[0]
        self.aResultBox.setText(str(mw[0]*(self.totMol-self.totMol/(10.0**(self.pH-self.pkaVar)+1.0))))
        self.aMol = float(self.aResultBox.text())/mw[0]
        self.asmw = mw[0]
        self.solveConductivity()
    def solveConductivity(self):
        HA_1 = float(self.aResultBox.text())
        HA = float(self.haResultBox.text())
        if(self.bufferId == 1):
            self.conductivityMSCmLineEdit.setText(str(66700*((2*self.naclMol + 2*float(self.aResultBox.text())/82.03)/2)**(0.991)/1000))
        if(self.bufferId == 2):
            cursor = self.connection.cursor()
            mwe = cursor.execute("SELECT MW FROM Chemical WHERE Name = ?", (self.haChoiceCombo.currentText(),))
            (mwha) = mwe.fetchall()[0]
            mwp = cursor.execute("SELECT MW FROM Chemical WHERE Name = ?", (self.aChoiceCombo.currentText(),))
            (mwa) = mwp.fetchall()[0]
            self.conductivityMSCmLineEdit.setText(str(66700*((6*HA_1/mwa[0] + 2*self.naclMol +2*HA/mwha[0])/2)**(0.991)/1000))
        if(self.bufferId==3):
            self.conductivityMSCmLineEdit.setText(str(66700*(((2*HA/157.6+2*self.naclMol)/2)**(0.911))/1000)) 
    def createMenu(self):
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('File')
        
        editMenu = mainMenu.addMenu('Edit')
        fontMenu = mainMenu.addMenu('Font')
        helpMenu = mainMenu.addMenu('Help')
 
 
        openAction = QAction(QIcon('open.png'), "Open", self)
        openAction.setShortcut('Ctrl+O')
 
 
        saveAction = QAction(QIcon('save.png'), "Save", self)
        saveAction.setShortcut('Ctrl+S')
 
        exitAction = QAction(QIcon('exit.png'), "Exit", self)
        exitAction.setShortcut('Ctrl+X')
        editAction = QAction(QIcon('save.png'), "edit", self)
        editAction.setShortcut('Ctrl+R')
 
 
 
        exitAction.triggered.connect(self.exit_app)
 

 

        fileMenu.addAction(openAction)
        fileMenu.addAction(saveAction)
       
        fileMenu.addAction(exitAction)
        editMenu.addAction(editAction)
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    createConnection()
    app.setStyle('Fusion')
    apply_stylesheet(app, theme='dark_amber.xml')
    main = BufferCalculator()

    main.show()
    """main.animation()"""
    sys.exit(app.exec_())
    