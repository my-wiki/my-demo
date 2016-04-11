#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore

#QtCore.QObject objects can emit signals - we create an external object, carrying the signal
class Communicate(QtCore.QObject):
    
    closeApp = QtCore.pyqtSignal()  #we create a new signal, called closeApp
    

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):
    
        col = QtGui.QColor(0, 0, 0)
        
        self.btn = QtGui.QPushButton('Dialog', self)
        self.btn.move(20, 20)
        
        self.btn.clicked.connect(self.showDialog)
        
        self.frm = QtGui.QFrame(self)
        self.frm.setStyleSheet("QWidget { background-color: %s }")
        self.frm.setGeometry(130, 22, 100, 100)
        
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Color dialog')
        self.show()
        
    def showDialog(self):
    
        col = QtGui.QColorDialog.getColor()
        
        if col.isValid():   #if we select a valid color and click ok (don't click cancel...)
            self.frm.setStyleSheet("QWidget { background-color: %s }" % col.name())
        
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
        main()
