#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import with_statement
#from weibopy.auth import OAuthHandler
#from weibopy.api import API
#import urllib2
#import xml.dom.minidom
from weibopy.auth import OAuthHandler , BasicAuthHandler
from weibopy.api import API
import os
import sys
from LoginWindow import LoginWindow
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import Qt, SIGNAL
from PyQt4 import QtGui, QtCore
import ConfigParser

    

        
def get_auth(token,tokenSecret):
    global auth
    auth = OAuthHandler("2839869753","e38cb74f0f38eb33a1e0e25b7adde7cb")
    auth.setToken(token,tokenSecret)
    return auth


def get_token(path):
    config = ConfigParser.ConfigParser()
    global token,tokenSecret
    with open(path,'rw') as cfgfile:
        config.readfp(cfgfile)
        token = config.get('user','key')
        tokenSecret = config.get('user','secret')
    return token,tokenSecret   


