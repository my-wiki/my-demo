#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore

#QtCore.QObject objects can emit signals - we create an external object, carrying the signal
class Communicate(QtCore.QObject):
    
    closeApp = QtCore.pyqtSignal()  #we create a new signal, called closeApp
    

class Example(QtGui.QMainWindow):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        
        self.textEdit = QtGui.QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()
        
        openFile = QtGui.QAction(QtGui.QIcon('icon.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new file')
        openFile.triggered.connect(self.showDialog)
        
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)
        
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('File dialog')
        self.show()
        
    def showDialog(self):
    
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file')
        
        f = open(fname, 'r')
        
        with f:
            data = f.read()
            self.textEdit.setText(data)
        
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
        main()
