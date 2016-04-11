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
        
        vbox = QtGui.QVBoxLayout()
        
        self.btn = QtGui.QPushButton('Dialog', self)
        self.btn.setSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        self.btn.move(20, 20)
        
        vbox.addWidget(self.btn)
        
        self.btn.clicked.connect(self.showDialog)
        
        self.lbl = QtGui.QLabel('Knowledge only matters', self)
        self.lbl.move(130, 20)
        
        vbox.addWidget(self.lbl)
        self.setLayout(vbox)
        
        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('Font dialog')
        self.show()
        
    def showDialog(self):
    
        font, ok = QtGui.QFontDialog.getFont()
        if ok:
            self.lbl.setFont(font)
        
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
        main()
