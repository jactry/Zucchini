#!/usr/bin/env python
#! -*-coding: utf-8-*-
import sys
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import Qt, SIGNAL
from PyQt4 import QtGui, QtCore
import Login
from weibopy.api import API
import json
import urllib2
import xml.dom.minidom
from LoginWindow import LoginWindow
import os
from weibopy.auth import OAuthHandler , BasicAuthHandler

        
if __name__ == "__main__":

    def get_auth(auth):
        
        Login.get_token(auth)
        
        
    
    def create_tray():
        tray=QtGui.QSystemTrayIcon(QtGui.QApplication.desktop())
        icon=QtGui.QIcon("./logo.png")
        tray.setIcon(icon)
        tray.show()
        tray.showMessage(u"Hello World!",
                         u"Master,I am here ^o^",QtGui.QSystemTrayIcon.MessageIcon(1),
                         2000)
    
    
    path = os.path.expanduser('~')+"/.config/.zucchini.conf"
    app=QApplication(sys.argv)
    Login_Window=LoginWindow()
    QtCore.QObject.connect(Login_Window,SIGNAL("to_auth(PyQt_PyObject)"),get_auth)
    Login_Window.show()
    create_tray() 
    
    
    sys.exit(app.exec_())
        
        
        
        


