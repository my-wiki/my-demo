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
        
        self.btn = QtGui.QPushButton("Dialog", self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)
        
        self.le = QtGui.QLineEdit(self)
        self.le.move(130, 20)
        
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Emit signal')
        self.show()
        
    def showDialog(self):
    
        # shows input dialog, frist string: dialog title, second string: message
        text, ok = QtGui.QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')
        # ok is true if we click the ok button on the pop-up dialog
        
        if ok:
            self.le.setText(str(text))
        
        #the closeApp signal is emitted on mouse press
        self.c.closeApp.emit()
        
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
        main()
