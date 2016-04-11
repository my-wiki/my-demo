#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui

class Example(QtGui.QMainWindow):

    def __init__(self):
        #super(Example, self) returns parent class
        super(Example, self).__init__() # == QtGui.QWidget.__init__(), without explicitly referring to parent class
        
        self.initUI()
        
    def initUI(self):
        #first call: Creates statusBar
        #subsequent calls: return statusBar object
        self.statusBar().showMessage('Ready')
        
        self.resize(250, 150)
        self.center()
        self.setWindowTitle('status bar')
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        
        self.show()
        
    def center(self):
        
        qr = self.frameGeometry()   #geometry of our rectangle frame
        #QtDesktopWidget() provides information about user desktop
        cp = QtGui.QDesktopWidget().availableGeometry().center() #get center point of desktop resolution
        qr.moveCenter(cp)       #move our rectangle frame center to desktop center
        self.move(qr.topLeft()) #move the top-left point of widget to top-left point of qr rectangle
    
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()