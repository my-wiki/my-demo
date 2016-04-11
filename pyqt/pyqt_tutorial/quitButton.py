#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):

    def __init__(self):
        #super(Example, self) returns parent class
        super(Example, self).__init__() # == QtGui.QWidget.__init__(), without explicitly referring to parent class
        
        self.initUI()
        
    def initUI(self):
        
        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')
        
        #BUTTONS
        qbtn = QtGui.QPushButton('Quit', self)
        #
        #QtCore.QCoreApplication is created with QtGui.QApplication, contains main event loop
        qbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        #
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50,50)
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Quit button')
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        
        self.show()
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()