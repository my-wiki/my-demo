#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui

def main():
    
    app = QtGui.QApplication(sys.argv)  #create application object  
    
    w = QtGui.QWidget()     #QWidget with default (no) constructor -> window
    w.resize(250, 150)      #set window w size   
    w.move(300, 300)        #position window w
    w.setWindowTitle('Simple')  #set window w title
    w.show()                #display w in screen
    
    sys.exit(app.exec_())   #mainloop ends when sys.exit() is called
    
if __name__ == '__main__':
    main()