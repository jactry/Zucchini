#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4.QtCore import Qt, SIGNAL
from PyQt4.QtGui import *
from ui_login import Ui_Form
import ConfigParser
from weibopy.auth import OAuthHandler , BasicAuthHandler
import json
from weibopy.api import API
import urllib2
from urllib2 import Request, urlopen, URLError, HTTPError
import xml.dom.minidom
import os
import re
from PyQt4 import QtGui, QtCore

class LoginWindow(QWidget,Ui_Form):
    to_auth = QtCore.pyqtSignal(OAuthHandler)
    def __init__(self,parent=None):
        QWidget.__init__(self,parent)
        self.setupUi(self)
        self.label_link.setOpenExternalLinks(True)
        self.connect(self.pushButton_login,SIGNAL("clicked()"),self.login)
        self.connect(self.pushButton_quit,SIGNAL("clicked()"),self.exit)
        self.connect(self.pushButton_pic,SIGNAL("clicked()"),self.open_link)
        self.lineEdit_pwd.setEchoMode(QLineEdit.Password)
        self.pushButton_login.setAutoDefault(True)
        self.move_to_center()
        
        
    def open_link(self):
        #os.system("gnome-open http://www.weibo.com")
        QtGui.QMessageBox.about(self,u"About Zuicchini",
                          "<h2>Zuicchini</h2>")
        
        
    def move_to_center(self):
        screen=QDesktopWidget().screenGeometry()
        size=self.geometry()
        self.move((screen.width()-size.width())/2,
                  (screen.height()-size.height())/2)
    def network_error(self):
        con = os.popen("ping -c 1 weibo.com")
        info = con.read()
        con.close()
        error_str = 'ping unknown host weibo.com\Z'
        if re.match(info, error_str):
            return True
        else:
            return False
        
    def return_code(self,auth,username,password):
        auth_url = auth.get_authorization_url()
        auth_url += "&oauth_callback=xml&userId="+username+"&passwd="+password
        req=urllib2.Request(auth_url)
        try:
            urllib2.urlopen(auth_url)
        except URLError,e: 
            if hasattr(e, 'reason'):  
                return 0  
            elif hasattr(e, 'code'):  
                return 0
            else:  
                return 1 
                
    def get_auth(self,auth,username,password): 
        code = self.return_code(auth,username,password)
        if code == 0: 
            return 1
        else:
            auth_url = auth.get_authorization_url()
            auth_url += "&oauth_callback=xml&userId="+username+"&passwd="+password
            result = urllib2.urlopen(auth_url)
            xmls = result.read()
            doc = xml.dom.minidom.parseString(xmls)
            root = doc.documentElement
            verifier = root.getElementsByTagName("oauth_verifier")[0]
            oauth_verifier = ""
            for node in verifier.childNodes:
                oauth_verifier = node.data
            auth.get_access_token(oauth_verifier)
            return auth
    
    def login(self):
        if self.network_error():
            self.label_warming.setText("<font color=red><b>Please check your network.</b></font>")
        elif self.lineEdit_user.text().isEmpty():
            self.label_warming.setText("<font color=red><b>Please type your username!</b></font>")
        elif self.lineEdit_pwd.text().isEmpty():
            self.label_warming.setText("<font color=red><b>Please type your password!</b></font>")
        else:       
            username=str(self.lineEdit_user.text())
            password=str(self.lineEdit_pwd.text())
            self.auth=OAuthHandler("2302181135","fbcf36a8412d628d9c1fc27e4cbbe06d")
            self.auth=self.get_auth(self.auth, username, password)
            if self.auth == 1:
                self.label_warming.setText("<font color=red><b>Please check your username and password.</b></font>")
            else:
            
                self.to_auth.emit(self.auth)
                self.hide()
            
             
          
        
    def exit(self):
         self.close()
         


