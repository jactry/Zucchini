#!/usr/bin/env python
#! -*-coding: utf-8-*-


# Zucchini - a little tool of weibo
# Copyright (c) 2012 - Jactry Zeng <jactry92@gmail.com>

import sys
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import Qt, SIGNAL
from PyQt4.QtCore import QObject
from PyQt4 import QtGui, QtCore
from PyQt4.QtNetwork import QLocalSocket, QLocalServer
from weibopy.api import API
import json
import urllib2
import xml.dom.minidom
from LoginWindow import LoginWindow
from Tray import Tray
import os
from weibopy.auth import OAuthHandler , BasicAuthHandler
from gi.repository import Unity, Gio, GObject, Dbusmenu


        
if __name__ == "__main__":
    
    
    def get_auth(auth):
        
        api = API(auth)
        
        
        def have_new():                
            
            count = api.unread()
            number = count.dm+count.mentions+count.comments
    
            launcher.set_property("count",number)
            launcher.set_property("count_visible", True)
            if globals().has_key("news"):
                if number < news:
                    news = number
                elif number > news :
                    body="Mester,you have "+str(count.dm)+" message(s),"+str(count.mentions)+" mention(s),and "+str(count.comments)+" comment(s)."
                    tray.showMessage("News",body,QtGui.QSystemTrayIcon.MessageIcon(1),500)
                    if launcher.get_property("urgent") :
                        launcher.set_property("urgent", False)
                        news = number
                    else:
                        launcher.set_property("urgent", True)
                        news = number
            else:
                global news
                news = 0
            
                
        QtCore.QObject.connect(timer, SIGNAL("timeout()"),have_new)
        timer.start(10000)
    
    #path = os.path.expanduser('~')+"/.config/.zucchini.conf"
    app=QApplication(sys.argv)
    app.connect(app, SIGNAL( "lastWindowClosed()" ), app.quit)
    server_Name = ('JiaJia')  
    socket = QLocalSocket()  
    socket.connectToServer(server_Name)  
      

    if socket.waitForConnected(500):  
        os.system("gnome-open http://www.weibo.com")
        sys.exit()

    local_Server = QLocalServer()       
    local_Server.listen(server_Name) 
    
    try:
        
        Login_Window=LoginWindow()
        QtCore.QObject.connect(Login_Window,SIGNAL("to_auth(PyQt_PyObject)"),get_auth)
        Login_Window.show()
        tray=Tray()
        tray.show()
        tray.showMessage(tray.trUtf8("Hello World!"),
                         tray.trUtf8("Master,I am here ^o^"),QtGui.QSystemTrayIcon.MessageIcon(1),
                         500)
        timer=QtCore.QTimer()
        launcher=Unity.LauncherEntry.get_for_desktop_id("zucchini.desktop")
        sys.exit(app.exec_())
        
    finally:  
        local_Server.close() 
        
    app.exit()


