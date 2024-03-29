# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './src/dialog_notifi.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_notifiDialog(object):
    def setupUi(self, notifiDialog):
        notifiDialog.setObjectName("notifiDialog")
        notifiDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        notifiDialog.resize(400, 200)
        notifiDialog.setMinimumSize(QtCore.QSize(400, 200))
        notifiDialog.setMaximumSize(QtCore.QSize(400, 200))
        notifiDialog.setStyleSheet("QWidget {\n"
"    background-color: rgb(32, 26, 25);\n"
"    color: rgb(237, 224, 221);\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(217, 217, 217);\n"
"    color: rgb(53, 44, 44);\n"
"    border-radius: 24;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(236, 236, 236);\n"
"    color: rgb(53, 44, 44);\n"
"    border-radius: 24;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(195, 195, 195);\n"
"    color: rgb(53, 44, 44);\n"
"    border-radius: 24;\n"
"}\n"
"\n"
"QTextBrowser {\n"
"    border: none;\n"
"    padding: 16;\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(notifiDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 33, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.textNotifiTextBrowser = QtWidgets.QTextBrowser(notifiDialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.textNotifiTextBrowser.setFont(font)
        self.textNotifiTextBrowser.setObjectName("textNotifiTextBrowser")
        self.verticalLayout.addWidget(self.textNotifiTextBrowser)
        spacerItem1 = QtWidgets.QSpacerItem(20, 32, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.okBtn = QtWidgets.QPushButton(notifiDialog)
        self.okBtn.setMinimumSize(QtCore.QSize(128, 48))
        self.okBtn.setMaximumSize(QtCore.QSize(128, 48))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.okBtn.setFont(font)
        self.okBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.okBtn.setStyleSheet("outline: none")
        self.okBtn.setObjectName("okBtn")
        self.horizontalLayout.addWidget(self.okBtn)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem4 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem4)

        self.retranslateUi(notifiDialog)
        QtCore.QMetaObject.connectSlotsByName(notifiDialog)

    def retranslateUi(self, notifiDialog):
        _translate = QtCore.QCoreApplication.translate
        notifiDialog.setWindowTitle(_translate("notifiDialog", "Уведомление"))
        self.textNotifiTextBrowser.setHtml(_translate("notifiDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Какое - то важное уведомление, которое не помещается на одну строку!</span></p></body></html>"))
        self.okBtn.setText(_translate("notifiDialog", "OK"))
