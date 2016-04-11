# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 300)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(80, 90, 66, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalSlider = QtGui.QSlider(Form)
        self.verticalSlider.setGeometry(QtCore.QRect(270, 60, 17, 160))
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName(_fromUtf8("verticalSlider"))
        self.dial = QtGui.QDial(Form)
        self.dial.setGeometry(QtCore.QRect(90, 210, 50, 64))
        self.dial.setObjectName(_fromUtf8("dial"))

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.dial, QtCore.SIGNAL(_fromUtf8("dialMoved(int)")), self.label.setNum)
        QtCore.QObject.connect(self.verticalSlider, QtCore.SIGNAL(_fromUtf8("sliderMoved(int)")), self.label.setNum)
        QtCore.QObject.connect(self.dial, QtCore.SIGNAL(_fromUtf8("dialMoved(int)")), self.verticalSlider.setValue)
        QtCore.QObject.connect(self.verticalSlider, QtCore.SIGNAL(_fromUtf8("sliderMoved(int)")), self.dial.setValue)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "TextLabel", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

