from PySide2 import QtSql, QtGui
import sqlite3
import re
from PySide2.QtCore import QFile

def createConnection():
    db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("Buffers.db")
    if not db.open():
        QtGui.QMessageBox.critical(None, QtGui.qApp.tr("Cannot open database"),
                QtGui.qApp.tr("Unable to establish a database connection.\n"
                              "This example needs SQLite support. Please read "
                              "the Qt SQL driver documentation for information "
                              "how to build it.\n\nClick Cancel to exit."),
                QtGui.QMessageBox.Cancel, QtGui.QMessageBox.NoButton)
        return False

    return True
def sqlite3con():
    try:
        con = sqlite3.connect("Buffers.db")
    except Exception as e:
        print(e)
        sqlfile = open(".sql")
        sqlfilestr = sqlfile.read()
        sqlite3.Cursor.executescript(sqlfilestr)
        con = sqlite3.connect("Buffers.db")


    return con
def createBufferList(con):
    cur = con.cursor()
    buffers = []
    cur.execute("SELECT Type FROM Buffer")
    rows = cur.fetchall()
    for row in rows:
        a = row
        (Type, ) =a
        buffers.append(Type)

    return  buffers
def createHAList(con, buffid):
    cur = con.cursor()
    HAs = []
    cur.execute("SELECT * FROM Chemical WHERE COMP='HA' AND BufferId=?", (buffid,))
    rows = cur.fetchall()
    for row in rows:
        a = row
        (Name, _, _, _  ) = a
        HAs.append(Name)
        
    return HAs
def createAList(con, buffid):
    cur = con.cursor()
    As = []
    cur.execute("SELECT * FROM Chemical WHERE COMP='A' AND BufferId=?", (buffid,))
    rows = cur.fetchall()
    for row in rows:
        a = row
        (Name, _, _, _  ) = a
        As.append(Name)
        
    return As
def remove(list):
    pattern = '[0-9]'
    list = [re.sub(pattern, '', i) for i in list]
    return list
        
def find_replace_multi(string, dictionary):
    for item in dictionary.keys():
        # sub item for item's paired value in string
        string = re.sub(item, dictionary[item], string)
    return string
       


