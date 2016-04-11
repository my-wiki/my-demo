#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        
        self.lbl = QtGui.QLabel("Ubuntu", self)
        
        combo = QtGui.QComboBox(self)   #create ComboBox widget
        combo.addItem("Ubuntu")
        combo.addItem("Mandriva")
        combo.addItem("Fedora")
        combo.addItem("Red Hat")
        combo.addItem("Mint")
        
        combo.move(50, 50)
        self.lbl.move(50, 150)
        
        #Send the activated combo option name(string) to onActivated method:
        combo.activated[str].connect(self.onActivated)
        
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QComboBox')
        self.show()  

    def onActivated(self, text):
    
        self.lbl.setText(text)
        self.lbl.adjustSize()
        
               
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
        main()
