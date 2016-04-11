#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        
        okButton = QtGui.QPushButton("OK")
        cancelButton = QtGui.QPushButton("Quit", self)
        cancelButton.clicked.connect(QtGui.qApp.quit)
       
        
        hbox = QtGui.QHBoxLayout()  #to create horizontal spacing
        hbox.addStretch(1)  #adds (stretchable - max possible width) empty space
        # -> next insert is aligned right
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)
        
        vbox = QtGui.QVBoxLayout()  # for vertical spacing
        vbox.addStretch(1)  #adds (stretchable - max height) empty space
        # -> next insert is aligned bottom
        vbox.addLayout(hbox)    #place hbox inside this vbox
        
        self. setLayout(vbox)
        
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Box layout')
        self.show()
        
def main():
        
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
        
if __name__ == '__main__':
    main()
        
        