#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PyQt4.QtCore import Qt, SIGNAL
from PyQt4.QtGui import *
from ui_login import Ui_Form
import ConfigParser
from weibopy.auth import OAuthHandler , BasicAuthHandler
"""import json
from weibopy.api import API
import urllib2
import xml.dom.minidom"""
import os
from PyQt4 import QtGui, QtCore

class LoginWindow(QWidget,Ui_Form):
    to_auth = QtCore.pyqtSignal(OAuthHandler)
    def __init__(self,parent=None):
        QWidget.__init__(self,parent)
        self.setupUi(self)
        
        self.connect(self.pushButton_login,SIGNAL("clicked()"),self.login)
        self.connect(self.pushButton_quit,SIGNAL("clicked()"),self.exit)
        self.lineEdit_pwd.setEchoMode(QLineEdit.Password)
        self.move_to_center()
        
        
       
            
    def move_to_center(self):
        screen=QDesktopWidget().screenGeometry()
        size=self.geometry()
        self.move((screen.width()-size.width())/2,
                  (screen.height()-size.height())/2)
    
    
    def get_Token(self,username,password):
    
         self.auth = OAuthHandler("2839869753","e38cb74f0f38eb33a1e0e25b7adde7cb")        
         #path = os.path.expanduser('~')+"/.config/.zucchini.conf"
         auth_url=self.auth.get_authorization_url()

         
    
    def login(self):
        
        if (self.lineEdit_user.text().isEmpty()):
            self.label_warming.setText("<font color=red><b>Please type your username!</b></font>")
        elif(self.lineEdit_pwd.text().isEmpty()):
            self.label_warming.setText("<font color=red><b>Please type your password!</b></font>")
        else:       
            username=str(self.lineEdit_user.text())
            password=str(self.lineEdit_pwd.text())
            self.get_Token(username,password)
            self.to_auth.emit(self.auth)
            
             
          
        
    def exit(self):
         self.close()
         


