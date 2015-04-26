# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ptchat.ui'
#
# Created: Sun Apr 26 15:13:45 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
import socket
import cPickle
import os

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
    def __init__(self):
        host = "sunucuip"
        port = 6666
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.connect((host, port))
        self.server.send("mrb")
        self.server.recv(1024)
        self.name = raw_input("User Name: ")
        self.server.sendall(self.name)
        data = self.server.recv(1024)
        if data != "#gir":
            sys.exit(1)

    def text_isle(self):
        msg = str(self.lineEdit.text())
        self.server.sendall(msg)
        data = cPickle.loads(self.server.recv(1024))
        ymetin = ""
        for i in data:
            ymetin += str.format("{}: {}\n", i['client'][1], i['message'])
        self.textBrowser.setText(ymetin)

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(417, 485)
        self.textBrowser = QtGui.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 411, 441))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(60, 450, 301, 25))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 450, 56, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(360, 450, 51, 26))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        Form.connect(self.pushButton, QtCore.SIGNAL("pressed()"), self.text_isle)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Ptchat v0.1", None))
        self.label.setText(_translate("Form", "Mesajınız", None))
        self.pushButton.setText(_translate("Form", "Gönder", None))

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    form = QtGui.QWidget()
    win = Ui_Form()
    win.setupUi(form)
    form.show()
    app.exec_()


