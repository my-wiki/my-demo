#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore

class Example(QtGui.QMainWindow):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        
        cb = QtGui.QCheckBox('Show title', self)
        cb.move(20, 20)
        cb.toggle()
        cb.stateChanged.connect(self.changeTitle)
        
        cb2 = QtGui.QCheckBox('Yoyoo', self)
        cb2.move(20, 100)
        cb2.stateChanged.connect(self.message)
        
        self.statusBar().showMessage('waiting')
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Check boxes')
        self.show()
        
    def changeTitle(self, state):
        
        if state == QtCore.Qt.Checked:
            self.setWindowTitle('QtGui.Q.CheckBox')
            
        else:
            self.setWindowTitle('')
            
    def message(self,gg):
        if gg == QtCore.Qt.Checked:
            self.statusBar().showMessage('cb2 checked')
            
        else:
            self.statusBar().showMessage('cb2 not checked')
        
        
        
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
        main()
