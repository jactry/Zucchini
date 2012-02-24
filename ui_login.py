# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ui_login.ui'
#
# Created: Wed Feb 22 22:24:21 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(391, 235)
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Zucchini", None, QtGui.QApplication.UnicodeUTF8))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.horizontalLayoutWidget = QtGui.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(100, 30, 281, 81))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_user = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_user.setStyleSheet(_fromUtf8(""))
        self.label_user.setText(QtGui.QApplication.translate("Form", "Username:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_user.setObjectName(_fromUtf8("label_user"))
        self.verticalLayout_2.addWidget(self.label_user)
        self.label_pwd = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_pwd.setText(QtGui.QApplication.translate("Form", "Password:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_pwd.setObjectName(_fromUtf8("label_pwd"))
        self.verticalLayout_2.addWidget(self.label_pwd)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lineEdit_user = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_user.setStyleSheet(_fromUtf8("border-style:oytset;\n"
"border:2px solid gray;\n"
"border-radius:10px;\n"
"padding:0 8px;\n"
"background: white;\n"
"selection-background-color:darkgray;"))
        self.lineEdit_user.setObjectName(_fromUtf8("lineEdit_user"))
        self.verticalLayout.addWidget(self.lineEdit_user)
        self.lineEdit_pwd = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_pwd.setStyleSheet(_fromUtf8("border-style:oytset;\n"
"border:2px solid gray;\n"
"border-radius:10px;\n"
"padding:0 8px;\n"
"background: white;\n"
"selection-background-color:darkgray;"))
        self.lineEdit_pwd.setObjectName(_fromUtf8("lineEdit_pwd"))
        self.verticalLayout.addWidget(self.lineEdit_pwd)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.pushButton_login = QtGui.QPushButton(Form)
        self.pushButton_login.setGeometry(QtCore.QRect(210, 190, 81, 31))
        self.pushButton_login.setStyleSheet(_fromUtf8(""))
        self.pushButton_login.setText(QtGui.QApplication.translate("Form", "Login", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_login.setObjectName(_fromUtf8("pushButton_login"))
        self.pushButton_quit = QtGui.QPushButton(Form)
        self.pushButton_quit.setGeometry(QtCore.QRect(300, 190, 81, 31))
        self.pushButton_quit.setStyleSheet(_fromUtf8(""))
        self.pushButton_quit.setText(QtGui.QApplication.translate("Form", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_quit.setObjectName(_fromUtf8("pushButton_quit"))
        self.pushButton_pic = QtGui.QPushButton(Form)
        self.pushButton_pic.setGeometry(QtCore.QRect(10, 30, 81, 81))
        self.pushButton_pic.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/button_logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_pic.setIcon(icon1)
        self.pushButton_pic.setIconSize(QtCore.QSize(81, 81))
        self.pushButton_pic.setObjectName(_fromUtf8("pushButton_pic"))
        self.label_link = QtGui.QLabel(Form)
        self.label_link.setGeometry(QtCore.QRect(10, 210, 67, 17))
        self.label_link.setText(QtGui.QApplication.translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"http://weibo.com/signup/signup.php\"><span style=\" font-size:9pt; text-decoration: underline; color:#0000ff;\">注册新帐号</span></a></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_link.setObjectName(_fromUtf8("label_link"))
        self.label_warming = QtGui.QLabel(Form)
        self.label_warming.setGeometry(QtCore.QRect(100, 110, 281, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.label_warming.setFont(font)
        self.label_warming.setStyleSheet(_fromUtf8(""))
        self.label_warming.setText(_fromUtf8(""))
        self.label_warming.setObjectName(_fromUtf8("label_warming"))
        self.label_user.setBuddy(self.lineEdit_user)
        self.label_pwd.setBuddy(self.lineEdit_pwd)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.lineEdit_user, self.lineEdit_pwd)
        Form.setTabOrder(self.lineEdit_pwd, self.pushButton_login)
        Form.setTabOrder(self.pushButton_login, self.pushButton_quit)
        Form.setTabOrder(self.pushButton_quit, self.pushButton_pic)

    def retranslateUi(self, Form):
        pass

import images_rc
