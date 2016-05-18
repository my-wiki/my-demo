#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode PyQt4 tutorial

This is a Tetris game clone.

author: Jan Bodnar
website: zetcode.com
last edited: October 2013
"""

import sys
from PyQt4 import QtGui
from board import Board


class Tetris(QtGui.QMainWindow):

    def __init__(self):
        super(Tetris, self).__init__()

        self.initUI()

    def initUI(self):

        self.tboard = Board(self)
        self.setCentralWidget(self.tboard)

        self.statusbar = self.statusBar()
        self.tboard.msg2Statusbar[str].connect(self.statusbar.showMessage)

        self.tboard.start()

        self.resize(180, 380)
        self.center()
        self.setWindowTitle('Tetris')
        self.show()

    def center(self):

        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move(  (screen.width()-size.width())/2,
                    (screen.height()-size.height())/2)


def main():
    app = QtGui.QApplication([])
    tetris = Tetris()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
