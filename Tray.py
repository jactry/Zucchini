#!/usr/bin/env python
#coding=utf-8

from PyQt4 import QtGui,QtCore

class Tray(QtGui.QSystemTrayIcon):
    def __init__(self,parent=None):
        QtGui.QSystemTrayIcon.__init__(self,parent)
        self.Tray_Icon=QtGui.QIcon(":/images/logo.png")
        self.setIcon(self.Tray_Icon)
        self.quit_Action=QtGui.QAction("&Quit",self,triggered=QtGui.qApp.quit)
        self.Tray_Menu=QtGui.QMenu()
        self.Tray_Menu.addAction(self.quit_Action)
        self.setContextMenu(self.Tray_Menu)
        