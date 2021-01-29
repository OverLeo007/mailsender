# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newGUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import os
import sys


def resource_path(relative):
    # функция позволяющая импортироать файлы при компиляции
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative)
    else:
        return os.path.join(os.path.abspath("."), relative)


class Ui_App(object):
    def setupUi(self, App):
        App.setObjectName("App")
        App.resize(1074, 370)
        App.setMinimumSize(QtCore.QSize(1074, 370))
        App.setMaximumSize(QtCore.QSize(1074, 370))
        self.layoutWidget = QtWidgets.QWidget(App)
        self.layoutWidget.setGeometry(QtCore.QRect(200, 20, 671, 331))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.delayText_1 = QtWidgets.QLabel(self.layoutWidget)
        self.delayText_1.setStyleSheet("color: rgb(0, 255, 0);\n"
                                       "background-color: rgb(0, 0, 0);\n"
                                       "border: 1px solid green;\n"
                                       "")
        self.delayText_1.setMidLineWidth(0)
        self.delayText_1.setWordWrap(False)
        self.delayText_1.setObjectName("delayText_1")
        self.verticalLayout_2.addWidget(self.delayText_1)
        self.delayTime_1 = QtWidgets.QLineEdit(self.layoutWidget)
        self.delayTime_1.setStyleSheet("color: rgb(0, 255, 0);\n"
                                       "background-color: rgb(0, 0, 0);\n"
                                       "border: 1px solid green;")
        self.delayTime_1.setObjectName("delayTime_1")
        self.verticalLayout_2.addWidget(self.delayTime_1)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.delayText_2 = QtWidgets.QLabel(self.layoutWidget)
        self.delayText_2.setStyleSheet("color: rgb(0, 255, 0);\n"
                                       "background-color: rgb(0, 0, 0);\n"
                                       "border: 1px solid green;\n"
                                       "")
        self.delayText_2.setWordWrap(False)
        self.delayText_2.setObjectName("delayText_2")
        self.verticalLayout.addWidget(self.delayText_2)
        self.delayTime_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.delayTime_2.setStyleSheet("color: rgb(0, 255, 0);\n"
                                       "background-color: rgb(0, 0, 0);\n"
                                       "border: 1px solid green;")
        self.delayTime_2.setObjectName("delayTime_2")
        self.verticalLayout.addWidget(self.delayTime_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.hmText = QtWidgets.QLabel(self.layoutWidget)
        self.hmText.setStyleSheet("color: rgb(0, 255, 0);\n"
                                  "background-color: rgb(0, 0, 0);\n"
                                  "border: 1px solid green;\n"
                                  "")
        self.hmText.setObjectName("hmText")
        self.verticalLayout_3.addWidget(self.hmText)
        self.hmMails = QtWidgets.QLineEdit(self.layoutWidget)
        self.hmMails.setStyleSheet("color: rgb(0, 255, 0);\n"
                                   "background-color: rgb(0, 0, 0);\n"
                                   "border: 1px solid green;\n"
                                   "")
        self.hmMails.setObjectName("hmMails")
        self.verticalLayout_3.addWidget(self.hmMails)
        self.startButton = QtWidgets.QPushButton(self.layoutWidget)
        self.startButton.setAutoFillBackground(False)
        self.startButton.setStyleSheet("color: rgb(0, 255, 0);\n"
                                       "background-color: rgb(0, 0, 0);\n"
                                       "border: 1px solid green;")
        self.startButton.setObjectName("startButton")
        self.verticalLayout_3.addWidget(self.startButton)
        self.log_browser = QtWidgets.QTextBrowser(self.layoutWidget)
        self.log_browser.setStyleSheet("color: rgb(170, 170, 0);\n"
                                       "background-color: rgb(0, 0, 0);\n"
                                       "border: 1px solid green;")
        self.log_browser.setObjectName("log_browser")
        self.verticalLayout_3.addWidget(self.log_browser)
        self.megu_1 = QtWidgets.QLabel(App)
        self.megu_1.setGeometry(QtCore.QRect(640, 0, 431, 371))
        self.megu_1.setStyleSheet("")
        self.megu_1.setText("")
        self.megu_1.setPixmap(QtGui.QPixmap(resource_path("megu4.png")))
        self.megu_1.setObjectName("megu_1")
        self.megu_2 = QtWidgets.QLabel(App)
        self.megu_2.setGeometry(QtCore.QRect(-230, -20, 481, 411))
        self.megu_2.setText("")
        self.megu_2.setPixmap(QtGui.QPixmap(resource_path("megu4.1.png")))
        self.megu_2.setObjectName("megu_2")
        self.bga = QtWidgets.QLabel(App)
        self.bga.setEnabled(True)
        self.bga.setGeometry(QtCore.QRect(-80, -60, 1201, 701))
        self.bga.setText("")
        self.bga.setPixmap(QtGui.QPixmap(resource_path("bga.jpg")))
        self.bga.setObjectName("bga")
        self.bga.raise_()
        self.layoutWidget.raise_()
        self.megu_1.raise_()
        self.megu_2.raise_()

        self.retranslateUi(App)
        QtCore.QMetaObject.connectSlotsByName(App)

    def retranslateUi(self, App):
        _translate = QtCore.QCoreApplication.translate
        App.setWindowTitle(_translate("App", "Mail spammer [by Raez]"))
        self.delayText_1.setText(_translate("App", "From email delay time (secodns)"))
        self.delayTime_1.setText(_translate("App", "0"))
        self.delayText_2.setText(_translate("App", "One post delay time (secodns)"))
        self.delayTime_2.setText(_translate("App", "0"))
        self.hmText.setText(_translate("App", "How many mails from one address"))
        self.hmMails.setText(_translate("App", "1"))
        self.startButton.setToolTip(_translate("App",
                                               "<html><head/><body><p>Синонимы: </p><p>abc#def#ghi</p><p>Предложения - синонимы: </p><p>{abc d/boo 1/vam ban}</p><p>Обязательно обе скобки на одной строке!</p></body></html>"))
        self.startButton.setText(_translate("App", "Start sending"))
