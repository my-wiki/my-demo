#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui

class Example(QtGui.QWidget):

    def __init__(self):
        #super(Example, self) returns parent class
        super(Example, self).__init__() # == QtGui.QWidget.__init__(), without explicitly referring to parent class
        
        self.initUI()
        
    def initUI(self):
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Message box')
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        
        self.show()
        
    def closeEvent(self, event):    #event called when quitting QtGui.QWidget
        
        reply = QtGui.QMessageBox.question(self, 'Message',
            "Are you sure you want to quit?", QtGui.QMessageBox.Yes |
            QtGui.QMessageBox.No, QtGui.QMessageBox.No
        )
        #first string: message title
        #second string: message text
        #third object: combination of buttons
        #fourth object: default option
        #result is stored in the (reply) value
        
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()