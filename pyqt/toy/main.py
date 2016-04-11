import sys
import os

import design
from PyQt4 import QtGui, QtCore


class ExampleApp(QtGui.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        # `super` allows us to access variables, methods etc in the design.py file
        super(self.__class__, self).__init__()
        # It sets up layout and widgets that are defined
        self.setupUi(self)  # This is defined in design.py file automatically
        self.initUI()

    def initUI(self):
        # Center the window on the screen.
        self.center()
        # menubar
        self.exitAction()
        # When the button is pressed Execute browse_folder function
        self.btnBrowse.clicked.connect(self.browse_folder)
        # Showing a tooltip
        self.setToolTip('This is a <b>brnBrowse</b> widget')
        # Closing a windows.
        self.close.clicked.connect(QtCore.QCoreApplication.instance().quit)
        # status bar
        self.author_submit.clicked.connect(self.buttonClicked)
        self.btnBrowse.clicked.connect(self.buttonClicked)
        self.statusBar()#.showMessage('Ready')
        # QLineEdit
        self.title_submit.clicked.connect(self.getChange)
        # signal & slot
        self.signalSlot()
        # input dialog
        self.author_submit.clicked.connect(self.showDialog)
        # checkbox
        self.checkBox.stateChanged.connect(self.statusBox)
        # toggle
        self.toggle()
        # process bar
        self.progressBtn.clicked.connect(self.proBar)
        self.timer = QtCore.QBasicTimer()
        self.step = 0
        # combine box
        self.combine()

    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def exitAction(self):
        self.actionExit.setShortcut('Ctrl+Q')
        self.actionExit.setStatusTip('Exit application')
        self.actionExit.triggered.connect(QtCore.QCoreApplication.instance().quit)

    def browse_folder(self):
        # In case there are any existing elements in the list
        self.listWidget.clear()
        directory = QtGui.QFileDialog.getExistingDirectory(self,
                                                           "Pick a folder")
        # execute getExistingDirectory dialog and set the directory variable to be equal to the user selected directory
        if directory: # if user didn't pick a directory don't continue
            for file_name in os.listdir(directory): # for all files, if any, in the directory
                self.listWidget.addItem(file_name)  # add file to the listWidget

    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, 'Message',
                                            "Are you sure to quit?", QtGui.QMessageBox.Yes |
                                            QtGui.QMessageBox.No, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def signalSlot(self):
        self.hsld.valueChanged.connect(self.nlcd.display)

    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')

    def statusBox(self, state):
        sender = self.sender()
        if state == QtCore.Qt.Checked:
            self.statusBar().showMessage(sender.text() + ' was pressed')
        else:
            self.statusBar().showMessage(sender.text() + ' was not pressed')

    def showDialog(self):
        text, ok = QtGui.QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')
        if ok:
            print str(text)
            self.content_author.setText(str(text))

    def getChange(self):
        le = self.content_title.text()
        print le

    def toggle(self):
        self.col = QtGui.QColor(0, 0, 0)
        self.red.setCheckable(True)
        self.green.setCheckable(True)
        self.blue.setCheckable(True)

        self.red.clicked[bool].connect(self.setColor)
        self.green.clicked[bool].connect(self.setColor)
        self.blue.clicked[bool].connect(self.setColor)
        self.square.setGeometry(150, 20, 100, 100)
        self.square.setStyleSheet("QFrame { background-color: %s  }" % self.col.name())

    def setColor(self, pressed):
        source = self.sender()
        val = 255 if pressed else 0
        if source.text() == "red":
            self.col.setRed(val)
        elif source.text() == "green":
            self.col.setGreen(val)
        else:
            self.col.setBlue(val)
        self.square.setStyleSheet("QFrame { background-color: %s  }" % self.col.name())

    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()
            self.progressBtn.setText('Finished')
            return
        self.step = self.step + 1
        self.progressBar.setValue(self.step)

    def proBar(self):
        if self.timer.isActive():
            self.timer.stop()
            self.progressBtn.setText('Start')
        else:
            self.timer.start(100, self)     #launch timer, defining its timeout step
            self.progressBtn.setText('Stop')

    def combine(self):
        def onActivated(text):
            print text
        self.comboBox.addItem("1")
        self.comboBox.addItem("2")
        self.comboBox.addItem("3")
        self.comboBox.addItem("4")
        self.comboBox.activated[str].connect(onActivated)

def main():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = ExampleApp()  # We set the form to be our ExampleApp (design)
    form.show()  # Show the form
    app.exec_()  # and execute the app


if __name__ == '__main__':  # if we're running file directly and not importing it
    main()  # run the main function
