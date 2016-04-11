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
        
        #connect the close() slot of QtGui.QMainWindow to closeApp signal
        self.c = Communicate()
        self.c.closeApp.connect(self.close) 
        
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Emit signal')
        self.show()
        
    def mousePressEvent(self, event):
        
        #the closeApp signal is emitted on mouse press
        self.c.closeApp.emit()
        
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
        main()
