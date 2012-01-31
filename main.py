#!/usr/bin/env python
#! -*-coding: utf-8-*-
import sys
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import Qt, SIGNAL
from PyQt4 import QtGui, QtCore
import Login
from weibopy.api import API
from LoginWindow import LoginWindow
import os


        
if __name__ == "__main__":
    
    
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
    Login_Window.show()
    create_tray() 
    
    
        
    
    sys.exit(app.exec_())
        
        
        
        


