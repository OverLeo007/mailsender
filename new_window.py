# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NewGUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_App(object):
    def setupUi(self, App):
        App.setObjectName("App")
        App.resize(510, 330)
        App.setMinimumSize(QtCore.QSize(510, 330))
        App.setMaximumSize(QtCore.QSize(510, 330))
        self.widget = QtWidgets.QWidget(App)
        self.widget.setGeometry(QtCore.QRect(12, 10, 481, 311))
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.delayText_1 = QtWidgets.QLabel(self.widget)
        self.delayText_1.setObjectName("delayText_1")
        self.verticalLayout_2.addWidget(self.delayText_1)
        self.delayTime_1 = QtWidgets.QLineEdit(self.widget)
        self.delayTime_1.setObjectName("delayTime_1")
        self.verticalLayout_2.addWidget(self.delayTime_1)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.delayText_2 = QtWidgets.QLabel(self.widget)
        self.delayText_2.setObjectName("delayText_2")
        self.verticalLayout.addWidget(self.delayText_2)
        self.delayTime_2 = QtWidgets.QLineEdit(self.widget)
        self.delayTime_2.setObjectName("delayTime_2")
        self.verticalLayout.addWidget(self.delayTime_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.hmText = QtWidgets.QLabel(self.widget)
        self.hmText.setObjectName("hmText")
        self.verticalLayout_3.addWidget(self.hmText)
        self.hmMails = QtWidgets.QLineEdit(self.widget)
        self.hmMails.setObjectName("hmMails")
        self.verticalLayout_3.addWidget(self.hmMails)
        self.startButton = QtWidgets.QPushButton(self.widget)
        self.startButton.setObjectName("startButton")
        self.verticalLayout_3.addWidget(self.startButton)
        self.log_browser = QtWidgets.QTextBrowser(self.widget)
        self.log_browser.setObjectName("log_browser")
        self.verticalLayout_3.addWidget(self.log_browser)

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
        self.startButton.setText(_translate("App", "Start sending"))
