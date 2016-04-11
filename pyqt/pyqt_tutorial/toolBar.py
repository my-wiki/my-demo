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
        
        #QtGui.QAction -> action performed in menubar, toolbar or with a custom keyboard shortcut
        exitAction = QtGui.QAction(QtGui.QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(QtGui.qApp.quit)   #actually trigger the exit action
        
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)
        
        
        self.setGeometry(300,300, 300, 200)
        self.setWindowTitle('Toolbar')
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        
        self.show()
    
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()