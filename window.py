# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reqd.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_App(object):
    def setupUi(self, App):
        App.setObjectName("App")
        App.resize(510, 290)
        App.setMinimumSize(QtCore.QSize(510, 290))
        App.setMaximumSize(QtCore.QSize(510, 290))
        App.setBaseSize(QtCore.QSize(50, 50))
        self.widget = QtWidgets.QWidget(App)
        self.widget.setGeometry(QtCore.QRect(9, 9, 491, 268))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.from_label = QtWidgets.QLabel(self.widget)
        self.from_label.setObjectName("from_label")
        self.verticalLayout.addWidget(self.from_label)
        self.from_text = QtWidgets.QLineEdit(self.widget)
        self.from_text.setText("")
        self.from_text.setClearButtonEnabled(False)
        self.from_text.setObjectName("from_text")
        self.verticalLayout.addWidget(self.from_text)
        self.startButton = QtWidgets.QPushButton(self.widget)
        self.startButton.setCheckable(False)
        self.startButton.setAutoDefault(False)
        self.startButton.setObjectName("startButton")
        self.verticalLayout.addWidget(self.startButton)
        self.log_browser = QtWidgets.QTextBrowser(self.widget)
        self.log_browser.setOverwriteMode(True)
        self.log_browser.setObjectName("log_browser")
        self.verticalLayout.addWidget(self.log_browser)

        self.retranslateUi(App)
        QtCore.QMetaObject.connectSlotsByName(App)

    def retranslateUi(self, App):
        _translate = QtCore.QCoreApplication.translate
        App.setWindowTitle(_translate("App", "Form"))
        self.from_label.setText(_translate("App", "From:"))
        self.startButton.setText(_translate("App", "Start sending"))
        self.log_browser.setHtml(_translate("App", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\';\"><br /></p></body></html>"))
