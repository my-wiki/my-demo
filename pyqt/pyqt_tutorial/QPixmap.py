#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        
        hbox = QtGui.QHBoxLayout(self)
        pixmap = QtGui.QPixmap("slika.png")     #create QPixmap object
        
        lbl = QtGui.QLabel(self)
        lbl.setPixmap(pixmap)       #put pixmap into QLabel widget
        hbox.addWidget(lbl)
        self.setLayout(hbox)
        
        self.move(300, 200)
        self.setWindowTitle('QPixmap')
        self.show()
        
    #reimplement timerEvent:
    def showDate(self, date):
        
        self.lbl.setText(date.toString())
        
               
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
        main()
