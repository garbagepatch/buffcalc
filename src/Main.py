from PySide2.QtSql import QSqlTableModel
from PySide2.QtWidgets import QApplication, QWidget, QTableView, QAbstractItemView, QVBoxLayout, QTabWidget
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtSql import *
from PySide2.QtWidgets import QWidget
import qdarkstyle
from ui.calculator import Ui_MainWindow
from data.connection import createBufferList, createHAList, createAList
from data.connection import sqlite3con
from PySide2 import QtWidgets, QtCore, QtGui
from qt_material import apply_stylesheet

"""import pyqtgraph.opengl as gl"""
from PySide2.QtGui import QIcon, QImage, QPixmap
from PySide2.QtWidgets import  QMainWindow, QAction, QMessageBox
from math import log10
from BufferCalculator import BufferCalculator
from datetime import date
from repairbuffer import RepairBuffer
"""from opensimplex import OpenSimplex"""
import sys
from data.connection import createConnection
class  Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)
        sys.stdout = self
        self.createMenu()
        self.setWindowTitle("Sup")
        self.connection = sqlite3con()
        self.calc = BufferCalculator()
        self.repair = RepairBuffer()
        self.tabWidget.removeTab(0)
        self.tabWidget.removeTab(0)
        self.tabWidget.addTab(self.calc, "Buffer Calculator")
        self.tabWidget.addTab(self.repair, "Recipe Repair")
        

    def exit_app(self):
        self.close()
    
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
 
 
        editAction.triggered.connect(self.editstuff)
        exitAction.triggered.connect(self.exit_app)
        

 

        fileMenu.addAction(openAction)
        fileMenu.addAction(saveAction)
       
        fileMenu.addAction(exitAction)
        editMenu.addAction(editAction)
    def editstuff(self):
        self.editthings = RepairBuffer()
        self.editthings.show()
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    createConnection()
    app.setStyle('Fusion')
    apply_stylesheet(app, theme='dark_amber.xml')
    main = Main()

    main.show()
    """main.animation()"""
    sys.exit(app.exec_())
    